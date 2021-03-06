DCOS Valkiria Subcommand
==========================

The Valkiria DCOS subcommand allow you to install agents of https://github.com/Stratio/valkiria/ and do the next operations to interact with them:

- install Establish an SSH connection to the master or agent nodes and install Valkiria on them.

- uninstall Establish an SSH connection to the master or agent nodes and uninstall Valkiria on them

- tasks Establish an SSH connection to the master or agent nodes and list the killables tasks.

- kill Establish an SSH connection to the master or agent nodes and kill the task with a specific taskId.

- start Establish an SSH connection to the master or agent nodes and start the Valkiria agent process on them.

- stop Establish an SSH connection to the master or agent nodes and stop the Valkiria agent process on them.

- status Establish an SSH connection to the master or agent nodes and get the status of the Valkiria agent process on them.



Setup
-----
#. Run from source or run from binary. If you would like to run from a binary, continue to 'Binary' section below.
#. Make sure you meet requirements for installing packages_
#. Clone git repo for the dcos command cli::

    git clone git@github.com:stratio/dcos-valkiria.git

#. Change directory to the repo directory::

    cd dcos-valkiria

#. Make sure that you have virtualenv installed. If not type::

    sudo pip install virtualenv

#. Create a virtualenv for the project::

    make env

Configure Environment and Run
-----------------------------

#. TODO: Talk about how to configure the root dcos cli

#. :code:`source` the setup file to add the :code:`dcos-valkiria` command line interface to your
   :code:`PATH`::

    source env/bin/activate

#. Get started by calling the DCOS command CLI's help::

    dcos command --help


Binary:
-----------

Create Binary:
##############

#. Install pyinstaller::

   pip install pyinstaller

#. Create command cli binary::

   make binary

Run Binary:
###########

#. Update `PATH` to have the dcos-command binary. The created binary is is in folder `dist`::

   PATH=/path/to/binary:$PATH

Running Tests:
--------------

Setup
#####

Tox, our test runner, tests against both Python 2.7 and Python 3.4 environments.

If you're using OS X, be sure to use the officially distributed Python 3.4 installer_ since the
Homebrew version is missing a necessary library.

Running
#######

Tox will run unit and integration tests in both Python environments using a temporarily created
virtualenv.

You should ensure :code:`DCOS_CONFIG` is set and that the config file points to the Marathon
instance you want to use for integration tests.

There are two ways to run tests, you can either use the virtualenv created by :code:`make env`
above::

    make test

Or, assuming you have tox installed (via :code:`sudo pip install tox`)::

    tox

Other Useful Commands
#####################

#. List all of the supported test environments::

    tox --listenvs

#. Run a specific set of tests::

    tox -e <testenv>

.. _packages: https://packaging.python.org/en/latest/installing.html#installing-requirements
