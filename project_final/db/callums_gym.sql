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

CREATE TABLE instructors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
)


CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
)

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    time VARCHAR(255),
    date VARCHAR(255),
    location_id SERIAL NOT NULL REFERENCES locations(id),
    instructor_id SERIAL NOT NULL REFERENCES instructors(id),
    capacity VARCHAR(255),
)

