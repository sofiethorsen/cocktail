CREATE TABLE articles(name TEXT,
					  name2 TEXT,
					  category TEXT);

CREATE TABLE recipes(_id SERIAL PRIMARY KEY,
					 name TEXT UNIQUE,
					 description TEXT);

CREATE TABLE recipe_items(_id SERIAL PRIMARY KEY,
						   recipe_id INTEGER,
						   name TEXT,
						   amount TEXT,
						   is_type BOOLEAN);

CREATE TABLE ingredients(_id SERIAL PRIMARY KEY,
						 name TEXT,
						 name2 TEXT,
						 type TEXT);