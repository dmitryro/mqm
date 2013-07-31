Deploying changes
=================

After you made some changes to the project, you want to update the server. You
can deploy the changes by running the following command on your local
computer, in the base directory of the project::

    fab deploy

This will do a several thing on the server:

1. Update the code base
2. Install all required python libraries
3. Syncdb and run migrations
4. Will build the contents of the static directory by running the django
   ``collectstatic`` command
5. Restart the gunicorn process so that all changes to the website are taken
   into action.

Semi-manual deployment
======================

Sometimes you know that you will need to run some manual commands during a
deploy. But you should still try to run as many things through the ``fab``
comand as possible. Since this is tested with a lot of projects and more
failsafe then always doing stuff just manually.

But if you do stuff manually during an update, follow this description:

1. Run ``fab update`` to update the code base
2. ssh into the server and authenticate as the project's user. The user is
   usually called like the project. All the files in the project's directory
   should belong to this user. Authenticate as this user with: ``sudo su
   <username>``.
3. Do what you have to do
4. Run ``fab deploy`` locally so that all steps of a usual deploy are done
   which will make sure that all general maintainance stuff like
   ``collectstatic`` will be called and that the gunicorn server will be
   restarted.

You can restart the gunicorn server at any point using ``fab restart``. It can
be stopped and started seperatly with ``fab stop`` and ``fab start``.
