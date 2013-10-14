# -*- coding: utf-8 -*-
'''
How to install a server::

    fab install
'''
from __future__ import with_statement
import hashlib
import os
import random
import re
import sys
from fabric.colors import blue, green, red, white, yellow, magenta
from fabric import network
from fabric.api import abort, cd, local, env, settings, sudo, get, put, hide
from fabric.api import run as _fabric_run
from fabric.contrib import files
from fabric.contrib.console import confirm


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
    'domain': project_config.get('project', 'domain'),
    'dbname': project_config.get('project', 'dbname'),
    'project': project_name,
    'user': project_config.get('project', 'user'),
    'repo_url': project_config.get('project', 'repository'),
    'services': _services,
    'port': project_config.get('django', 'port'),
    'local_settings': project_config.get('django', 'local_settings'),
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
        if not files.exists(config['local_settings']):
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
    with settings(warn_only=True):
        sass_compile()
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

def bower_install():
    '''
    * install JS dependencies
    '''
    with cd(path):
        run('bower install')

def sass_compile():
    '''
    * compiling sass files into css.
    '''
    with cd(path):
        with cd('static/sass'):
            run('mkdir -p ../css/')
            run('sass screen.scss:../css/screen.min.css --style exanded')

def deploy():
    '''
    * upload source
    * build static files
    * restart services
    '''
    update()
    bower_install()
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
        with cd(path):
            run('svn info')
        for service_config in _services():
            sudo('svstat /etc/service/%(service_name)s' % service_config)


def conf(operation='get', filename=SERVER_SETTINGS_FILE):
    if operation == 'get':
        get(os.path.join(config['path'], config['local_settings']), SERVER_SETTINGS_FILE)
    if operation == 'put':
        put(SERVER_SETTINGS_FILE, os.path.join(config['path'], config['local_settings']))


def loaddata(apps=None):
    if apps is None:
        apps = project_config.get('development', 'loaddata_apps')
        apps = ' '.join(apps.split())
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
    local('rsync -r %s@%s:%s/media/media/ media/media/' % (
        env.user,
        env['hosts'][0],
        config['path']))


##############################
# Installation on new server #
##############################


def create_user():
    with settings(warn_only=True):
        sudo('useradd --home %(path)s %(user)s' % config)
        sudo('gpasswd -a www-data %(user)s' % config)
        sudo('gpasswd -a gregor %(user)s' % config)
        sudo('gpasswd -a angelo %(user)s' % config)
        sudo('gpasswd -a martin %(user)s' % config)

def setup_fs_permissions():
    with cd(path):
        sudo('chown %(user)s:%(user)s -R .' % config)
        sudo('chmod u+rw,g+rw -R .')
        sudo('chmod g+s -R .')
        sudo('chmod +x restart')
        for service in config['services']:
            with settings(warn_only=True):
                sudo('chmod +x services/%s' % service)

def _determine_port():
    port = config['port']
    if port:
        return port
    port_available = re.compile(u'Connection refused\s*$', re.IGNORECASE)
    while True:
        port = random.randint(10000, 11000)
        with settings(hide('warnings', 'stdout', 'running'), warn_only=True):
            result = sudo('echo | telnet localhost %d' % port)
            if port_available.search(result):
                return port

def _ascii_art(art, color=magenta):
    clips = {
        'killer': '''
    _/        _/  _/  _/
   _/  _/        _/  _/    _/_/    _/  _/_/
  _/_/      _/  _/  _/  _/_/_/_/  _/_/
 _/  _/    _/  _/  _/  _/        _/
_/    _/  _/  _/  _/    _/_/_/  _/
'''
    }
    clip = clips[art]
    print color(clip)

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

    # just in case its already on there ...
    stop()

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

    create_database(mysql_root_password)
    setup(mysql_root_password)

    syncdb()

    with cd(path):
        run('bin/python manage.py loaddata config/adminuser.json')

    collectstatic()
    start()
    reload_webserver()
    setup_fs_permissions()

    conf('get')
    url = u'http://%(domain)s/\n' % config

    _ascii_art('killer')

    print(
        green(u'Success!\n') +
        url + u'\n' +
        yellow(
            u'The project should be up and running. You will find the '
            u'local_settings.py used on the server on your local machine as ') +
        blue(u'server_settings.py') +
        yellow(u' in the current working directory. Modify it '
            u'as needed and upload again with:\n') +
        blue(u'fab conf:put')
    )

def uninstall():
    if not confirm(u'Do you really want to delete the project from the server?'):
        print red(u'Aborting')
        sys.exit(0)
    delete_db = confirm(u'Do you want to delete the associated database?')
    mysql_root_password = None
    while delete_db and not mysql_root_password:
        mysql_root_password = raw_input(u'Please enter the mysql root password: ')
    with settings(warn_only=True):
        conf(u'get')

    stop()
    teardown()

    with settings(warn_only=True):
        sudo(u'rm -rf %(path)s' % config)
        sudo(u'deluser --remove-home %(user)s' % config)
        sudo(u'delgroup %(user)s' % config)

    if delete_db:
        sudo((
            'echo "DROP DATABASE %(dbname)s;" | '
            'mysql --user=root --password=%(root_password)s'
        ) % {
            'dbname': config['dbname'],
            'root_password': mysql_root_password,
        })

    print(
        green(u'The project was deleted successfully.\n')
    )
    if not delete_db:
        print(
            yellow(u'The database is still in place. Consider deleting it by hand.')
        )

def _get_mysql_password(root_password):
    user_password = hashlib.sha1('%s-%s' % (config['dbname'], root_password)).hexdigest()
    user_password = user_password[::-2]
    return user_password

def create_database(root_password):
    user_password = _get_mysql_password(root_password)
    sudo(
        'echo "CREATE DATABASE IF NOT EXISTS %(dbname)s CHARACTER SET utf8;"'
        ' | mysql --user=root --password=%(root_password)s' % {
            'dbname': config['dbname'],
            'root_password': root_password,
        })
    sudo(
        'echo "'
            'GRANT ALL ON %(dbname)s.* TO %(dbname)s IDENTIFIED BY \'%(user_password)s\';'
        '"'
        ' | mysql --user=root --password=%(root_password)s' % {
            'dbname': config['dbname'],
            'root_password': root_password,
            'user_password': user_password,
        })
    return user_password

def setup(mysql_root_password=None):
    '''
    * symlink services to /etc/service/<project_name>-<service>
    * symlink and nginx config to /etc/nginx/sites-available
    * symlink and nginx config from /etc/nginx/sites-available to
      /etc/nginx/sites-enabled
    * reload nginx
    '''
    port = _determine_port()
    template_config = {
        u'USER': config['user'],
        u'PROJECT_NAME': project_name,
        u'DOMAIN': config['domain'],
        u'PORT': port,
        u'DBNAME': config['dbname'],
        u'DBUSER': config['dbname'],
    }
    with cd(path):
        if not files.exists(config['local_settings']):
            if mysql_root_password:
                mysql_user_password = _get_mysql_password(mysql_root_password)
                context = template_config.copy()
                context.update({
                    u'DBPASSWORD': mysql_user_password,
                    u'SECRET_KEY': _generate_secret_key(),
                })
                files.upload_template(
                    u'src/website/local_settings.example.py',
                    context=context,
                    destination=config['local_settings'])
        context = template_config.copy()
        files.upload_template(
            u'config/nginx.conf.template',
            context=context,
            destination=u'config/nginx.conf')
        for service in config['services']:
            files.upload_template(
                u'services/%s.template' % service,
                context=context,
                destination=u'services/%s' % service)

    for service_config in _services():
        local_config = config.copy()
        local_config.update(service_config)
        if not files.exists('/etc/service/%(service_name)s/run' % local_config):
            sudo('mkdir -p /etc/service/%(service_name)s' % local_config)
            sudo('ln -s %(path)s/services/%(service)s /etc/service/%(service_name)s/run' % local_config)
    if not files.exists('/etc/nginx/sites-available/%(project)s.conf' % config):
        sudo('ln -s %(path)s/config/nginx.conf /etc/nginx/sites-available/%(project)s.conf' % config)
    if not files.exists('/etc/nginx/sites-enabled/%(project)s.conf' % config):
        sudo('ln -s /etc/nginx/sites-available/%(project)s.conf /etc/nginx/sites-enabled' % config)

    setup_fs_permissions()
    reload_webserver()
    restart()

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
    if not os.path.exists('src/website/local_settings.py'):
        local(
            'cp -p src/website/local_settings.development.py src/website/local_settings.py',
            capture=False)

def devupdate():
    local('bin/pip install -r requirements/development.txt')
    local('bower install')
    local('cd static/sass; mkdir -p ../css/; sass screen.scss:../css/screen.min.css --style exanded')

def devinit():
    devsetup()
    devupdate()
    local('bin/python manage.py syncdb --noinput --migrate', capture=False)
    local('bin/python manage.py loaddata config/adminuser.json', capture=False)
    local('bin/python manage.py loaddata config/localsite.json', capture=False)

    _ascii_art('killer')

def replace(**kwargs):
    if kwargs:
        for key, value in kwargs.items():
            local(r'find -type f | grep -v "^\./\." | grep -v ".svn" | xargs sed -i "s/<REPLACE:%s>/%s/g"' % (
                key,
                value.replace('"', r'\"'),
            ))
    else:
        local(r'grep -r "<REPLACE:[^>]\+>" . | grep -v ".svn"', capture=False)

def open():
    '''
    Open the live site in the default browser.
    '''
    import webbrowser
    url = 'http://%(domain)s/' % config
    print "opening %s" % url
    webbrowser.open(url)
