#!/bin/bash

XML_FILE="http://www.systembolaget.se/Assortment.aspx?Format=Xml"
DATABASE="drinkapp"
USER="drinkappuser"

# remove the database if it already exists
dropdb $DATABASE

# drop user if it already exist
dropuser $USER

# create user for the database
echo "Creating new user <$USER>..."
createuser -d  -s $USER

# create the database
echo "Creating new database <$DATABASE>..."
createdb $DATABASE -U $USER -W -h localhost -w

# create the database schema
echo "Creating tables..."
psql -d $DATABASE -f ../cocktail/sql/schema.sql

# insert systembolaget articles
curl $XML_FILE | python systemet_to_sql.py | psql -d $DATABASE -f - > /dev/null 2>&1

echo "Removing duplicate rows..."
psql -d $DATABASE -f ../cocktail/sql/removeduplicates.sql

# create indexes
psql -d $DATABASE -f ../cocktail/sql/indexes.sql
