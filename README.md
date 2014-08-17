cocktail
=======================
Gives drink suggestions based on the ingredients you have at home.

Installation
==========
requirements.txt
----------
Install the pip packages using:

    pip install -r requirements.txt
postgres
----------
To run the server you will need postgresql: 

    brew install postgresql

You can start postgres manually with: 

    pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
    
And stop it with:

    pg_ctl -D /usr/local/var/postgres stop -s -m fast
    
You can then create the database with the create_db.sh script:

    ./create_db.sh

Running the application
==========
Make sure the server is running and that you have compiled the CoffeeScript files to the target directory static/js

Then just run: 

    python cocktail.py

    