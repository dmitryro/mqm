# -*- coding: utf-8 -*-
from __future__ import with_statement
import os
from fabric.api import abort, cd, local, env, run, settings, sudo


env.hosts.extend([
    '<REPLACE:IP>',
])


project_name = '<REPLACE:PROJECT_NAME>'
path = '/srv/%s' % project_name
repo_url = 'svn://granger@theobaldgranger.com/svnroot/%s' % project_name


config = {
    'path': path,
    'project': project_name,
    'repo_url': repo_url,
}

def update():
    '''
    * Update the checkout.
    '''
    with cd(path):
        run('svn update')

def syncdb():
    '''
    * run syncdb
    * run migrate
    '''
    with cd(path):
        run('bin/django syncdb --noinput')

def restart():
    '''
    * restart all services
    '''
    with cd(path):
        sudo('./restart')

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
    '''
    * test project and abort if tests have failed
    '''
    local('bin/test', capture=False)

def buildout():
    '''
    * run a buildout
    '''
    with cd(path):
        run('test -e bin/buildout || python bootstrap.py', capture=False)
        run('bin/buildout', capture=False)

def deploy():
    '''
    * test project
    * upload source
    * run buildout on server and run db migrations
    * restart services
    '''
    test()
    update()
    buildout()
    syncdb()
    restart()

def _get_services():
    service_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'services')
    services = [d
        for d in os.listdir(service_dir)
        if os.path.isfile(os.path.join(service_dir, d))]
    return services

def _services():
    for service in _get_services():
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

def status():
    '''
    * show if services are running
    '''
    with settings(warn_only=True):
        for service_config in _services():
            sudo('svstat /etc/service/%(service_name)s' % service_config)


##############################
# Installation on new server #
##############################


def install():
    '''
    * create project user
    * add webserver and ssh user to project user
    * create project directory and push sources to server
    * install everything with buildout
    * install sample local_settings.py
    '''
    with settings(warn_only=True):
        sudo('useradd --home %(path)s %(project)s' % config)
        sudo('gpasswd -a www-data %(project)s' % config)
        sudo('gpasswd -a %s %s' % (env['user'], config['project']))
        sudo('mkdir -p %s' % os.path.dirname(config['path']))
    sudo('svn checkout %(repo_url)s %(path)s' % config)
    sudo('chown %(project)s:%(project)s -R %(path)s' % config)
    sudo('chmod u+rw,g+rw -R %(path)s' % config)
    sudo('chmod g+s -R %(path)s' % config)
    with cd(path):
        run('test -e bin/buildout || python bootstrap.py')
        with settings(warn_only=True):
            run('python %(path)s/bin/buildout' % config)
        run('test -e src/website/local_settings.py && cp -p src/website/local_settings.example.py src/website/local_settings.py')
    print('-' * 30)
    print('Please update local_settings.py in %s%ssrc/website/' % (env['host'], path))

def load_adminuser():
    with cd(path):
        run('bin/django loaddata config/adminuser.json')

def setup_django():
    buildout()
    syncdb()
    load_adminuser()

def create_database(root_password, user_password):
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
        sudo('rm /etc/nginx/sites-available/%(project)s' % config)
        sudo('rm /etc/nginx/sites-enabled/%(project)s' % config)
    reload_webserver()


#######################
# Development helpers #
#######################

def _replace_secret_key():
    from random import choice
    secret_key = ''.join([
        choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        for i in range(50)])
    secret_key = secret_key.replace('&', '\\&')
    return (
        r'''sed -i "s/^SECRET_KEY\s*=\s*[ru]\?['\"].*['\"]\s*$/'''
        r'''SECRET_KEY = '%s'/"''' % secret_key)


def devinit():
    local('test -e bin/buildout || python bootstrap.py', capture=False)
    local('bin/buildout', capture=False)
    local(
        'test -e src/website/local_settings.py || '
        'cp -p src/website/local_settings.example.py src/website/local_settings.py',
        capture=False)
    local('bin/django syncdb --noinput', capture=False)
    local('bin/django loaddata config/adminuser.json', capture=False)
    local('bin/django loaddata config/localsite.json', capture=False)
    local('bin/django build_static --noinput', capture=False)


def replace(**kwargs):
    if kwargs:
        for key, value in kwargs.items():
            local(r'find -type f | grep -v "^\./\." | xargs sed -i "s/<REPLACE:%s>/%s/g"' % (
                key,
                value.replace('"', r'\"'),
            ))
    else:
        local(r'grep -r "<REPLACE:[^>]\+>" .', capture=False)
