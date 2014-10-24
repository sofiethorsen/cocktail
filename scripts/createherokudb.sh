#!/bin/bash
DATABASE=$HEROKUDB

echo "Drop old tables..."
psql -d $DATABASE -f ../cocktail/sql/droptables.sql

# create the database schema
echo "Creating tables..."
psql -d $DATABASE -f ../cocktail/sql/schema.sql

echo "Inserting systembolaget articles..."
# insert systembolaget articles
python systemet_to_sql.py < articles.txt | psql -d $DATABASE -f - > /dev/null 2>&1

echo "Removing duplicate rows..."
psql -d $DATABASE -f ../cocktail/sql/removeduplicates.sql

echo "Inserting resource items..."
python ../cocktail/insert_resource_items.py

echo "Mapping systembolaget articles to recipe ingredients..."
python ../cocktail/map_articles_to_ingredients.py

# create indexes
psql -d $DATABASE -f ../cocktail/sql/indexes.sql
