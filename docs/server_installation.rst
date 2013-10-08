::

        _/      _/    _/_/    
       _/_/  _/_/  _/    _/   
      _/  _/  _/  _/_/_/_/    
     _/      _/  _/    _/     
    _/      _/  _/    _/      
                        

Install a new server
====================

Install these packages::

    subversion
    git
    python
    python-dev
    ipython
    mysql-server
    python-mysqldb
    python-imaging
    daemontools
    ruby
    rubygems
    node (maybe from a ppa)

Install more stuff with::

    sudo gem install sass
    sudo npm install -g bower

Put the following into /etc/init/svscan.conf::

    # svscan - daemontools
    #
    # This service starts daemontools from the point the system is
    # started until it is shut down again.

    start on startup

    start on runlevel 1
    start on runlevel 2
    start on runlevel 3
    start on runlevel 4
    start on runlevel 5
    start on runlevel 6

    stop on shutdown

    exec svscanboot

Append ``/var/lib/gems/1.8/bin`` to ``$PATH`` in ``/etc/environment``

And run::

    sudo start svscan
