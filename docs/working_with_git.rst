::

        _/      _/    _/_/    
       _/_/  _/_/  _/    _/   
      _/  _/  _/  _/_/_/_/    
     _/      _/  _/    _/     
    _/      _/  _/    _/      
                        

Installing git
==============

On Mac OS, make sure you have MacPorts installed. Then run::

    sudo port install git-core +svn +doc +bash_completion +gitweb

Setting up your environment
===========================

Step 1 - Signup with bitbucket
------------------------------

M/A manages its repositories on https://bitbucket.org/
You are going to need an account there to work with any of the git based M/A
projects.

Step 2 - Get a member of the M/A team
-------------------------------------

Ask an adminstrator of the M/A team on bitbucket to add you.

Step 3 - Create an SSH key
--------------------------

In order to work with git in general or on bitbucket you need to have an SSH
key. Make sure you have an SSH key in your home directory. You can check
with::

    cat ~/.ssh/id_rsa.pub

If that displays anything on your screen (except an error message), then you
already have a key. If it displays something like ``File or Directory not
found``, you are going to execute the following command::

    ssh-keygen

It is going to ask you some questions, but its safe to just press enter. It's
going to ask for a passphrase but you can leave that empty if you want.

Step 4 - Make bitbucket to now your public ssh key
--------------------------------------------------

* Go to your bitbucket account page: https://bitbucket.org/account/
* Click on *SSH keys* on the left
* Click *Add key*
* Enter the name of your computer into the field *Label*
* And put your public key into the field *Key*. Your public key is exactly
  that what the ``cat ~/.ssh/id_rsa.pub`` command prints out.
* Click *Add key*

Step 5 - Configure git
----------------------

Run the following commands (and please change the name and email to represent
your own ones ;-))::

    git config --global user.name "John Doe"
    git config --global user.email johndoe@example.com

Congratulations. Your inital setup is ready to be used now!

Working with git and bitbucket
==============================

Ok lets assume there is already a project on bitbucket that you want to get a
local copy of to work with. First, go to the M/A team page on bitbucket and
have a look at the repositories there: https://bitbucket.org/mawork

Choose the one you want to work on.

You will see a box on the right that tells you the URL of the repo. Make sure
that you select SSH from the dropdown left to it. It is going to look
something like this: ``git@bitbucket.org:mawork/project-name.git``

Copy this URL, we need it to checkout the repository. In git, this is called
*clone*.

Step 1 - Clone the repository
-----------------------------

Execute on the command-line (<REPO-URL> is the one you copied from the
bitbucket page)::

    git clone <REPO-URL>

Nice! You now have a local checkout, that you can use like any project. Run
``fab devinit`` etc. and make the changes you need to make.

Step 2 - Committing changes
---------------------------

Now that you have made some changes to the code base, you can try to commit
them. There is also a command in git called ``commit``. However this isn't
transfering anything into the repository, since you need to tell git exactly
what you want to commit. This process in git is called *staging*. To stage a
file (marking it as *should beeing committed*) you can use::

    git add <filename>
    
You don't need to mention all the files, you can stage directories with::

    git add <directory>

Or just simply add all your changes you made to your local checkout with::

    git add --update

Ok, now you are ready to commit::

    git commit -m "<message>"

The message is mandatory. Make sure to choose a good one, describing your
changes.

Step 3 - Pushing your changes to bitbucket
------------------------------------------

Git is a so called *distributed* version control system. That means, that you
can use your local copy of the repo offline and don't even need a central
server like you have it with svn.

We won't go into much detail of this principle, however the consequence is,
that all your commits are just local commits. So now change is made yet to the
so called *upstream* repository on bitbucket.

You can push your changes to bitbucket with::

    git push

Step 4 - Updating your local repository
---------------------------------------

The ``push`` command from above might fail. The reason for this is that
someone else might already pushed some changes to the repo since you last
updated your local clone. The solution to this is to ``pull`` the newest
changes from the server to your computer. You can do this by using::

    git pull --rebase

Now you have the latest version of the project on your computer. All the
commits that you have already made locally but not yet pushed to the server,
are still there! Its safe now to ``git push`` them.

Step 5 - Become a git wizard!
-----------------------------

Git is a very powerful tool. However with great power comes great
responsibility.

Get to learn git better by reading the following book (available online for
free). Read at least chapter 1 and 2 (Getting Started, Git Basics):

* http://git-scm.com/book/

When you already have a basic understanding of git, try this page:

* http://gitready.com/

Working with branches
=====================

Sometimes there is a need that the changes you want to make to the project
won't affect the main line of development. This is what branches of a
repository are for. By default you work on the ``master`` branch in git. That
is also where the normal development happens.

To check what branch your local clone is currently working with, type::

    git branch

This will return something like::

      adminwork
      master
    * staging

The line with the asterisk in front of it is the branch that you are currently
working on. The other names are the other local branches that you have.

Create a new branch
-------------------

TODO ...

Push the branch to the server
-----------------------------

TODO ...

Change to a different branch
----------------------------

If you want to change your local repo to work on a different branch, then use::

    git checkout <branch-name>

Working on a branch
-------------------

If the branch you want to work on is already on bitbucket, then you need to
get it first into your local copy. By default there will only be the master
branch from the server available locally. Fetch it by using::

    git fetch --all

Then change into the branch you want to work with::

    git checkout <branch-name>

Now you can work like you are used to work with git. After you've done your
changes, you stage them, you commit them and push them to the server::

    git add <filename>
    git commit -m "my recent changes"
    git push

This will update the branch on the server.
