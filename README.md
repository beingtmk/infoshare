# INFOShare

INFOShare has a plethora of ways people can collaborate and share information.

The project has five basic apps:

* News (A Twitter-like microblog)
* Articles (A collaborative blog or a Facebook like post)
* Question & Answers (A Stack Overflow-like platform)
* Messeger (A basic chat-a-like tool for asynchronous communication.)
* Groups (which could be a club or event: Coding Club, Alcheringa)

Technology Stack
----------------

* Python_ 3.6.x / 3.7.x
* `Django Web Framework`_ 1.11.x / 2.0.x
* PostgreSQL_
* `Redis 3.2`_
* `Twitter Bootstrap 4`_
* `jQuery 3`_

DEPLOYMENT LOCALLY
------------------

### Make sure to have the following on your host:

* virtualenv

* pip

* PostgreSQL.

* libpq-dev
    $ sudo apt-get libpq-dev

### Follow these steps to get it running on your machine:

* clone the repository
    
    $ git clone https://github.com/beingtmk/infoshare.git

* Create a virtual env
* Activate the virtualenv you have just created
* CD into the project folder
* Install development requirements:

    $ pip install -r requirements/local.txt
    
* Create a new PostgreSQL database and a user 'infoshare'

    $ createdb infoshare
    $ createuser infoshare
 
 * Enter PostgreSQL 
    
    $ sudo -u postgres psql
  
 *  create Role to access database
 
    \# CREATE ROLE infoshare WITH LOGIN PASSWORD 'ultimate';
    
 * Grant all privileges to the user for him to connect to the database
    
    \# GRANT ALL PRIVILEGES infoshare TO infoshare;
    
 * Migrate the database
    
    $ python manage.py migrate
    
* Setup Email Backend - MailHog
    
    url - https://github.com/mailhog/MailHog/releases
    
    * Download the latest MailHog release for your OS.
    * Rename the build to MailHog.
    * Copy the file to the project root.
    * Make it executable.
        $ chmod +x MailHog
    * Spin up another terminal window and start it there:
        $ ./MailHog
    
    
 * Configure Redis Server for websockets used in Notifications
    $ sudo apt-get update
    $ sudo apt install redis-server
    $ redis-server

* Run Server locally to view the project
    
    $ python manage.py runserver 8000


 ## The Server will be deployed at 127.0.0.1:8000
