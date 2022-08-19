DROP TABLE IF EXISTS lessons CASCADE;
DROP TABLE IF EXISTS visits CASCADE;
DROP TABLE IF EXISTS members CASCADE;
DROP TABLE IF EXISTS instructors CASCADE;
DROP TABLE IF EXISTS locations CASCADE;


CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    date_of_birth VARCHAR(255),
    address VARCHAR(255),
    tel_number VARCHAR(255),
    email VARCHAR(255),
    platinum_member BOOLEAN
);


CREATE TABLE instructors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);


CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);


CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    time VARCHAR(255),
    date VARCHAR(255),
    location_id SERIAL NOT NULL REFERENCES locations(id) ON DELETE CASCADE,
    instructor_id SERIAL NOT NULL REFERENCES instructors(id) ON DELETE CASCADE,
    capacity VARCHAR(255)
);


CREATE TABLE visits (
    id SERIAL PRIMARY KEY,
    member_id SERIAL NOT NULL REFERENCES members(id) ON DELETE CASCADE,
    lesson_id SERIAL NOT NULL REFERENCES lessons(id) ON DELETE CASCADE
);