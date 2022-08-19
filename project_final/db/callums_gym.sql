drop table members
drop table classes
drop table class_members

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    date_of_birth VARCHAR(255),
    address VARCHAR(255),
    tel_number VARCHAR(255),
    email VARCHAR(255),
    platinum_member BOOLEAN
)

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    time VARCHAR(255),
    date VARCHAR(255),
    location VARCHAR(255),
    instructor VARCHAR(255),
    capacity VARCHAR(255),
)