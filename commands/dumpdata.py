# -*- coding: utf-8 -*-
'''
A simple script to dump all data of a django project installation into a single
directory. Run this script on a frequent base and backup the created file with
a cronjob to have always an up-to-date database backup.

Created and maintained by Gregor Müllegger <gregor at muellegger dot de>

2010-01-04 -- Initial version
'''
import os, sys
import subprocess
import re

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# set to 'python manage.py' or 'django-admin.py' if you use don't use buildout
MANAGE_COMMAND = 'bin/python manage.py'

# path to your settings file that contains the INSTALLED_APPS
SETTINGS_FILE = 'src/website/settings.py'

# paths that should be in sys.path to execute the settings file properly
PYTHONPATH = (
    os.path.join(path, 'src'),
    os.path.join(path, 'src/website'))

# where shall the dumps go?
OUTPUT_PATH = os.path.join(path, 'backups')

# listed apps will not be backuped, so becarefull
# you must specify the exact string you use in your INSTALLED_APPS and not only
# the last part
EXCLUDE_APPS = (
    # 'django.contrib.sessions',
    # 'django.contrib.admin',
)

# Overwrites parts of the internal app dict.
# You can combine two apps into one dump like in the example below.
OVERWRITE_APPS = {
    # 'sessions admin': 'sessions_and_admin.json',
}

# this file will be used to store a complete dump
# set to None if you don't want to have a complete dump.
COMPLETE_DUMP_NAME = '__all__.json'

# Set to True if you want to hide the warnings that are displayed if the dump
# of an app was empty.
IGNORE_WARNINGS = False

# Hide warnings only of specific apps. Specify only the last part of the app
# module (e.g. admin instead of django.contrib.admin)
IGNORE_WARNINGS_ON_APPS = (
    'django_extensions',
    'website',
)


def main():
    os.chdir(path)

    sys.path = list(PYTHONPATH) + list(sys.path)
    settings = {
        '__file__': os.path.abspath(SETTINGS_FILE),
    }
    execfile(SETTINGS_FILE, settings)

    apps = {}
    for app in settings['INSTALLED_APPS']:
        app = app.split('.')[-1]
        apps[app] = '%s.json' % app
    apps.update(OVERWRITE_APPS)

    if COMPLETE_DUMP_NAME:
        apps[''] = COMPLETE_DUMP_NAME

    for app, filename in apps.items():
        filename = os.path.join(OUTPUT_PATH, filename)
        subprocess.call(['%s dumpdata %s > %s 2> /dev/null' % (
            MANAGE_COMMAND, app, filename)], shell=True)
        # remove the dump if file only contains [] (an empty dump)
        f = file(filename)
        fcontents = f.read()
        f.close()
        if re.match(r'^\s*(?:\[])?\s*$', fcontents):
            os.unlink(filename)
            if not IGNORE_WARNINGS and app not in IGNORE_WARNINGS_ON_APPS:
                sys.stderr.write("Warning: Dump of '%s' does not contain data.\n" % app)
    subprocess.call(['%s dumpdata %s > %s 2> /dev/null' % (
        MANAGE_COMMAND, app, filename)], shell=True)


if __name__ == '__main__':
    main()
