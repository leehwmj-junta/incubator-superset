OS dependencies
---------------

Superset stores database connection information in its metadata database.
For that purpose, we use the ``cryptography`` Python library to encrypt
connection passwords. Unfortunately this library has OS level dependencies.

You may want to attempt the next step
("Superset installation and initialization") and come back to this step if
you encounter an error.

Here's how to install them:

For **Debian** and **Ubuntu**, the following command will ensure that
the required dependencies are installed: ::

    sudo apt-get install build-essential libssl-dev libffi-dev python-dev python-pip libsasl2-dev libldap2-dev



Making your own build
---------------------

For more advanced users, you may want to build Superset from sources. That
would be the case if you fork the project to add features specific to
your environment.::

    # assuming $SUPERSET_HOME as the root of the repo
    cd $SUPERSET_HOME/superset/assets
    yarn
    yarn run build
    cd $SUPERSET_HOME
    python setup.py install


    # Create an admin user (you will be prompted to set username, first and last name before setting a password)
    fabmanager create-admin --app superset

    # Initialize the database
    superset db upgrade

    # Load some data to play with
    superset load_examples

    # Create default roles and permissions
    superset init

    # Start the web server on port 8088, use -p to bind to another port
    superset runserver

    # To start a development web server, use the -d switch
    # superset runserver -d


After installation, you should be able to point your browser to the right
hostname:port `http://localhost:8088 <http://localhost:8088>`_, login using
the credential you entered while creating the admin account, and navigate to
`Menu -> Admin -> Refresh Metadata`. This action should bring in all of
your datasources for Superset to be aware of, and they should show up in
`Menu -> Datasources`, from where you can start playing with your data!