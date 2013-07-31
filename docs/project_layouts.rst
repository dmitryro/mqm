Project layouts
===============

This skeleton project is used as a base for all django projects at M/A. The
current approach is using **pip** for handling python dependencies and
**virtualenv** to work in an isolated environment.

To start working on a project you always run the command ``fab devinit``
first. This will create the virtualenv, download dependencies, update any
other stuff that needs to be ready for developing. It will also create you a
``local_settings.py`` file in ``src/website/`` so that you can start
developing right away.

To run any django related commands, you will need to use the ``manage.py``
file in the base directory. However you will not need to activate the
virtualenv. That is done programmatically in the ``manage.py``. Have a look at
it's source code to see how it's done.

Directory layout
----------------

The usual django project contains a lot of directories:

``config/``
    This contains configuration for the server, including ``nginx.conf`` and
    some other utility stuff.

``logs/``
    Will be created on the first run of the project, is not part of the code
    repository but will hold important logs from gunicorn etc, that are
    project related.

``media/``
    It's the media directory where uploaded files will go to.

``static/``
    That's the base directory where ``STATIC_ROOT`` is pointing to.

``templates/``
    Self explanatory for a django project.

``src/``
    This directory contains all the python code necessary to run the project.
    It is always available in the ``sys.path`` and can contain forked
    libraries. The most important subdirectory here is ``src/website/``. It
    holds all the project related django code, like project specific apps, the
    settings file etc.

using fabric for deployment
---------------------------

We use fabric for deployment. Please make yourself comfortable with it and
read throught the commands defined in ``fabfile.py``. They will always be
handy when working with a django project in M/A.

To deploy changes to a project that is already up and running on the server,
just type::
    
    fab deploy

However this will only work if your local username is the same as the one on
the server. Your username on the server is usually your firstname in
lowercase. So to change the username that will be used to connect to the
server you specify the ``-u`` option, like::

    fab -u <my-username> deploy

Legacy projects
---------------

Some of the django projects we developed don't use **pip** and **virtualenv**.
They rely on **buildout** for seperating the environments and dependency
handling.

These projects won't have a ``manage.py`` file. But after you setup the
project, you will be able to use ``bin/django`` as a replacement, like::

    bin/django migrate
    bin/django shell
    bin/django runserver
    etc..

The dependencies are listed in ``buildout.cfg``. If you change some of them,
you need to run ``bin/buildout`` to download new dependencies.

However the ``fab`` commands will work in most of the legacy projects as
expected. So you can usually still use ``fab deploy`` for pushing changes to
the server, or ``fab devinit`` to setup your local development environment.
