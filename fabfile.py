# -*- coding: utf-8 -*-
from __future__ import with_statement
import os
from fabric.api import abort, cd, local, env, run, settings, sudo


env.hosts.extend([
    '<REPLACE:IP>',
])


project_name = '<REPLACE:PROJECT_NAME>'
path = '/home/%s' % project_name

config = {
    'path': path,
    'project': project_name,
}

def _get_services():
    service_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'services')
    services = [d
        for d in os.listdir(service_dir)
        if os.path.isdir(os.path.join(service_dir, d)) and \
            os.path.exists(os.path.join(service_dir, d, 'run'))]
    return services

def _services():
    for service in _get_services():
        service_config = {
            'service': service,
            'service_name': '%s-%s' % (config['project'], service),
        }
        service_config.update(config)
        yield service_config

def update():
    '''
    Push current local commit to server and update the checkout.
    '''
    local('bzr push --no-strict bzr+ssh://%s%s' % (env['host'], path))
    with cd(path):
        run('bzr update')

def syncdb():
    '''
    * run syncdb
    * run migrate
    '''
    run('%sbin/django syncdb --noinput' % path)

def restart():
    '''
    * restart all services
    '''
    with cd(path):
        run('./restartfcgi')

def restart_webserver():
    '''
    * restart nginx
    '''
    sudo('pkill nginx')
    sudo('/opt/nginx/sbin/nginx')

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
        run('test -e bin/buildout || python bootstrap.py')
        run('bin/buildout')

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
        'cp -p src/website/local_settings.example.py src/website/local_settings.py && '
        '%s src/website/local_settings.py' % _replace_secret_key())
    local('bin/django syncdb --noinput')
    local('bin/django loaddata config/adminuser.json')

def replace(**kwargs):
    for key, value in kwargs.items():
        local(r'find -type f | grep -v "^\./\." | xargs sed -i "s/<REPLACE:%s>/%s/g"' % (
            key,
            value.replace('"', r'\"'),
        ))
