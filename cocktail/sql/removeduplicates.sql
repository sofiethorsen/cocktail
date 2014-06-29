CREATE TABLE tmp(name TEXT, name2 TEXT, category TEXT);
INSERT INTO tmp SELECT DISTINCT * FROM articles;
DROP TABLE articles;
ALTER TABLE tmp RENAME TO articles;