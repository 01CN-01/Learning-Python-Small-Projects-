
CREATE TABLE IF NOT EXISTS users 
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    social      TEXT NOT NULL,
    first_name  TEXT NOT NULL,
    last_name   TEXT NOT NULL,
    email       TEXT NOT NULL,
    password    TEXT NOT NULL
);