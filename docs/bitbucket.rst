Using Bitbucket
===============

Settings things up
------------------

The following steps are only needed to be done once per computer.

1. Make sure you have a ssh key. Type ``cat ~/.ssh/id_rsa.pub`` and make sure
   you don't get an error. If this file does not exist, execute ``ssh-keygen``
   to create your ssh key.
2. Upload your key to bitbucket. A quick example is shown here (You only need
   to apply Step 6): https://confluence.atlassian.com/display/BITBUCKET/Set+up+SSH+for+Git 

Getting a clone of a repository
-------------------------------

1. Go to the mawork bitbucket site: https://bitbucket.org/mawork
2. Click on one of the repositories of your interest. For example: ma-django-skeleton
3. You'll see a box on the right, the top most thing in there is the URL to
   this repository that you can use with git. So make sure that **SSH** is
   selected in the dropdown, then copy the URL.
4. go to the terminal where you want to put the clone, e.g.::
    
    cd ~/projects/

5. Clone the repository::

    git clone <copied-repo-url>
    # e.g. for the django skeleton:
    git clone git@bitbucket.org:mawork/ma-django-skeleton.git

Hooray! You now have a clone of the repository

Committing changes to the repository
------------------------------------

Now you can work on the cloned repository like with any git repo. Please
consider reading a git tutorial on staging changes and doing commits. But
basically, what you are doing is the following:

1. cd into the project directory, e.g.::

    cd ~/projects/ma-django-skeleton

2. Pull in the latest changes from the repository::

    git pull

3. Do some amazing work on the project.
4. Add your changes to the staging area::

    git add <file-that-you-want-to-commit>
    # for example:
    git add templates/index.html
    # or to stage the whole template directory:
    git add templates

5. Review what files you have changed and what will be committed::

    git status

6. Commit your changes::

    git commit -m "Your commit message here"

7. Push your changes to the bitbucket repository::

    git push
