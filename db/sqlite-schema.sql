DROP TABLE IF EXISTS person;

CREATE TABLE person (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT,
  email TEXT NOT NULL
);