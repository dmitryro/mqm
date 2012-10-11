                          
    _/      _/    _/_/    
   _/_/  _/_/  _/    _/   
  _/  _/  _/  _/_/_/_/    
 _/      _/  _/    _/     
_/      _/  _/    _/      
                        

Install python on MacOS
=======================

This is what we currently do with new macs:

* Install latest XCode
* Open XCode and go to "Preferences > Downloads" and install "Command Line Tools"
* Install _`macports <install macports>`
* Make sure macports is installed :)
* Install python using macports::

    sudo port selfupdate
    sudo port install python27
    sudo port select --set python python27
    sudo port install py27-distribute
    sudo port install py27-pip
    sudo port install py27-virtualenv
    sudo port install py27-fabric
    sudo port install py27-pil
    sudo port select --set virtualenv virtualenv27
    sudo ln -s /opt/local/bin/pip-2.7 /opt/local/bin/pip
    sudo ln -s /opt/local/bin/fab-2.7 /opt/local/bin/fab

* Close your current command line and open a new one.
* Now make sure that you use the correct python version::

    which python

This should return something like this::

    /opt/local/bin/python

.. _install macports: http://www.macports.org/install.php
