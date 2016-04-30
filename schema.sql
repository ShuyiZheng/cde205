DROP TABLE IF EXISTS messages;


CREATE TABLE messages (
    id integer PRIMARY KEY
    email text not null,
    name text NOT NULL,
    phone integer not null,
    message text NOT NULL
    );