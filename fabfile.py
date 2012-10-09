# -*- coding: utf-8 -*-
'''
How to install a server::

    fab install
'''
from __future__ import with_statement
import os
import sys
from fabric.colors import blue, green, red, white, yellow
from fabric import network
from fabric.api import abort, cd, local, env, settings, sudo, get, put
from fabric.api import run as _fabric_run
from fabric.contrib import files


def _project_config():
    from ConfigParser import SafeConfigParser
    config_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'project.ini')
    project_config = SafeConfigParser()
    project_config.read(config_file)
    return project_config
project_config = _project_config()


env.hosts.extend([
    project_config.get('project', 'host'),
])


project_name = project_config.get('project', 'name')


_services = project_config.get('project', 'services')
_services = _services.split()

config = {
    'path': project_config.get('project', 'path'),
    'project': project_name,
    'user': project_name,
    'repo_url': project_config.get('project', 'repository'),
    'services': _services,
}

del _services

path = config['path']


SERVER_SETTINGS_FILE = 'server_settings.py'


def run(command):
    '''
    Overwriting run command to execute tasks as project user.
    '''
    command = command.encode('string-escape')
    sudo('su %s -c "%s"' % (config['user'], command))


def update():
    '''
    * Update the checkout.
    '''
    with cd(path):
        run('svn update')
        run('mkdir -p logs')
    setup_fs_permissions()

def syncdb():
    '''
    * run syncdb --migrate
    '''
    with cd(path):
        run('bin/python manage.py syncdb --noinput --migrate')

def reload_webserver():
    '''
    * reload nginx
    '''
    sudo('/etc/init.d/nginx reload')

def restart_webserver():
    '''
    * restart nginx
    '''
    sudo('/etc/init.d/nginx restart')

def test():
    # test if the project.ini file is filled correctly
    required_config = (
        ('project', 'name'),
        ('project', 'repository'),
        ('project', 'host'),
        ('project', 'domain'),
        ('project', 'path'),
        ('django', 'port'),
    )
    missing_values = []
    for config_name in required_config:
        value = project_config.get(*config_name)
        if not value:
            missing_values.append(config_name)
    if missing_values:
        print(
            red(u'Error: ') +
            u'Please modify ' + yellow('project.ini') +
            u' to contain all the necessary information. ' +
            u'The following options are missing:\n'
        )
        for section, key in missing_values:
            print(yellow(u'\t%s.%s' % (section, key)))
        sys.exit(1)

    # check if project is already set up on the server
    if not files.exists(config['path']):
        print(
            red(u'Error: ') +
            u'The project is not yet installed on the server. ' +
            u'Please run ' + blue(u'fab install')
        )
        sys.exit(1)

    # check if project has a local_settings file
    with cd(path):
        if not files.exists('src/website/local_settings.py'):
            print(
                red(u'Error: ') +
                u'The project has no ' + yellow(u'local_settings.py') +
                u' configuration file on the server yet. ' +
                u'Please run ' + blue(u'fab install') + u'.'
            )
            sys.exit(1)

    print(
        green(u'Congratulations. Everything seems fine so far!\n') +
        u'You can run ' + yellow(u'fab deploy') + ' to update the server.'
    )

def collectstatic():
    '''
    * run bin/python manage.py collectstatic
    '''
    with cd(path):
        run('bin/python manage.py collectstatic -v0 --noinput')

def setup_virtualenv():
    '''
    * setup virtualenv
    '''
    with cd(path):
        run('virtualenv . --system-site-packages')

def pip_install():
    '''
    * install dependcies
    '''
    with cd(path):
        run('bin/pip install -r requirements/live.txt')

def deploy():
    '''
    * upload source
    * build static files
    * restart services
    '''
    update()
    pip_install()
    syncdb()
    collectstatic()
    restart()

def _services():
    for service in config['services']:
        service_config = {
            'service': service,
            'service_name': '%s-%s' % (config['project'], service),
        }
        service_config.update(config)
        yield service_config

def start():
    '''
    * start all services
    '''
    for service_config in _services():
        sudo('svc -u /etc/service/%(service_name)s' % service_config)

def stop():
    '''
    * stop all services
    '''
    for service_config in _services():
        sudo('svc -d /etc/service/%(service_name)s' % service_config)

def restart():
    '''
    * restart all services
    '''
    stop()
    start()
    collectstatic()

def status():
    '''
    * show if services are running
    '''
    with settings(warn_only=True):
        for service_config in _services():
            sudo('svstat /etc/service/%(service_name)s' % service_config)

def conf(operation='get', filename=SERVER_SETTINGS_FILE):
    if operation == 'get':
        get('%s/src/website/local_settings.py' % config['path'], SERVER_SETTINGS_FILE)
    if operation == 'put':
        put(SERVER_SETTINGS_FILE, '%s/src/website/local_settings.py' % config['path'])


def loaddata(apps=None):
    if apps is None:
        apps = project_config.get('development', 'loaddata_apps')
    dump_file = '.dump.json'
    server_dump = os.path.join(config['path'], dump_file)
    with cd(path):
        run('%s/bin/python manage.py dumpdata --indent=2 --natural --all %s > %s' % (
            config['path'],
            apps,
            server_dump))
        get(server_dump, dump_file)
    local('bin/python manage.py loaddata %s' % dump_file)


def loadmedia():
    assert len(env['hosts']) == 1
    local('rsync -r %s:%s/media/media/ media/media/' % (
        env['hosts'][0],
        config['path']))


##############################
# Installation on new server #
##############################


def create_user():
    with settings(warn_only=True):
        sudo('useradd --home %(path)s %(project)s' % config)
        sudo('gpasswd -a www-data %(project)s' % config)
        sudo('gpasswd -a gregor %s' % (config['project']))
        sudo('gpasswd -a angelo %s' % (config['project']))
        sudo('gpasswd -a martin %s' % (config['project']))

def setup_fs_permissions():
    with cd(path):
        sudo('chown %(project)s:%(project)s -R .' % config)
        sudo('chmod u+rw,g+rw -R .')
        sudo('chmod g+s -R .')
        sudo('chmod +x restart')
        for service in config['services']:
            sudo('chmod +x services/%s' % service)

def install(mysql_root_password=None):
    u'''
    * create project user
    * add webserver and ssh user to project user
    * create project directory and push sources to server
    * install everything with pip_install
    * install local_settings.py
    * syncdb
    * load a sample admin user
    * run collectstatic
    * setup the webserver and gunicorn
    * starting the gunicorn server
    * reloading nginx
    * setting the filesystem permissions correctly
    '''
    while not mysql_root_password:
        mysql_root_password = raw_input(u'Please enter the mysql root password: ')

    create_user()

    # create project directory
    dirname = os.path.dirname(config['path'])
    if not files.exists(dirname):
        sudo('mkdir -p %s' % os.path.dirname(config['path']))

    # svn checkout
    sudo('svn checkout %(repo_url)s %(path)s' % config)

    setup_fs_permissions()

    # disconnect from ssh to make new system users/groups available
    network.disconnect_all()

    setup_virtualenv()
    pip_install()

    mysql_user_password = create_database(mysql_root_password)

    with cd(path):
        if files.exists('src/website/local_settings.py'):
            email_user = raw_input(u'Please enter a GMail username for the email setup: ')
            email_password = raw_input(u'Please enter the GMail password: ')
            files.upload_template(
                u'src/website/local_settings.example.py',
                context={
                    u'PROJECT_NAME': project_name,
                    u'MYSQL_PASSWORD': mysql_user_password,
                    u'SECRET_KEY': _generate_secret_key(),
                    u'EMAIL_USER': email_user,
                    u'EMAIL_PASSWORD': email_password,
                },
                destination=u'src/website/local_settings.py')

    syncdb()

    with cd(path):
        run('bin/python manage.py loaddata config/adminuser.json')

    collectstatic()
    setup()
    start()
    reload_webserver()
    setup_fs_permissions()

    conf('get')
    print(
        u'The project should be up and running. You will find the '
        u'local_settings.py used on the server on your local machine as '
        u'`server_settings.py` in the current working directory. Modify it '
        u'as needed and upload again with:\n'
        u'fab conf:put')

def create_database(root_password, user_password=None):
    created = False
    if user_password is None:
        user_password = _pwdgen()
        created = True
    sudo(
        'echo "CREATE DATABASE IF NOT EXISTS %(project)s CHARACTER SET utf8;"'
        ' | mysql --user=root --password=%(root_password)s' % {
            'project': config['project'],
            'root_password': root_password,
        })
    sudo(
        'echo "'
            'GRANT ALL ON %(project)s.* TO %(project)s IDENTIFIED BY \'%(user_password)s\';'
        '"'
        ' | mysql --user=root --password=%(root_password)s' % {
            'project': config['project'],
            'root_password': root_password,
            'user_password': user_password,
        })
    if created:
        print('The project\'s mysql password is: %s' % user_password)
    return user_password

def setup(service=None):
    '''
    * symlink services to /etc/service/<project_name>-<service>
    * symlink and nginx config to /etc/nginx/sites-available
    * symlink and nginx config from /etc/nginx/sites-available to
      /etc/nginx/sites-enabled
    * reload nginx
    '''
    with settings(warn_only=True):
        for service_config in _services():
            local_config = config.copy()
            local_config.update(service_config)
            sudo('mkdir -p /etc/service/%(service_name)s' % local_config)
            sudo('ln -s %(path)s/services/%(service)s /etc/service/%(service_name)s/run' % local_config)
        sudo('ln -s %(path)s/config/nginx.conf /etc/nginx/sites-available/%(project)s.conf' % config)
        sudo('ln -s /etc/nginx/sites-available/%(project)s.conf /etc/nginx/sites-enabled' % config)
    reload_webserver()

def teardown():
    '''
    * stop and remove services
    * remove nginx config files from /etc/nginx/sites-enabled and
      /etc/nginx/sites-available
    * reload nginx
    '''
    with settings(warn_only=True):
        for service_config in _services():
            sudo('svc -dx /etc/service/%(service_name)s' % service_config)
            sudo('rm -r /etc/service/%(service_name)s' % service_config)
        sudo('rm /etc/nginx/sites-available/%(project)s.conf' % config)
        sudo('rm /etc/nginx/sites-enabled/%(project)s.conf' % config)
    reload_webserver()


#######################
# Development helpers #
#######################

def _generate_secret_key():
    import random
    return u''.join([
        random.choice(u'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        for i in range(50)
    ])

def _pwdgen():
    import random
    random.seed()
    allowedConsonants = "bcdfghjklmnprstvwxz"
    allowedVowels = "aeiou"
    allowedDigits = "0123456789"
    pwd = random.choice(allowedConsonants) + random.choice(allowedVowels) \
        + random.choice(allowedConsonants) + random.choice(allowedVowels) \
        + random.choice(allowedConsonants) + random.choice(allowedVowels) \
        + random.choice(allowedDigits) + random.choice(allowedDigits)
    return pwd

def devsetup():
    local('virtualenv . --system-site-packages --python=`which python`')
    local('bin/pip install -r requirements/development.txt')

def devinit():
    devsetup()
    if not os.path.exists('src/website/local_settings.py'):
        local(
            'cp -p src/website/local_settings.development.py src/website/local_settings.py',
            capture=False)
    local('bin/python manage.py syncdb --noinput --migrate', capture=False)
    local('bin/python manage.py loaddata config/adminuser.json', capture=False)
    local('bin/python manage.py loaddata config/localsite.json', capture=False)

def replace(**kwargs):
    if kwargs:
        for key, value in kwargs.items():
            local(r'find -type f | grep -v "^\./\." | grep -v ".svn" | xargs sed -i "s/<REPLACE:%s>/%s/g"' % (
                key,
                value.replace('"', r'\"'),
            ))
    else:
        local(r'grep -r "<REPLACE:[^>]\+>" . | grep -v ".svn"', capture=False)
