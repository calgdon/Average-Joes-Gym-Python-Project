# Average Joes Gym Booking Application

## About

This solo, full-stack project was undertaken over 6 days on completion of the four week Python module with CodeClan. 

## Tech Stack

The technologies utilised were as follows:

    - HTML
    - CSS
    - Python
    - Flask
    - PostgreSQL
    
 **No JavaScript Allowed**
    
## Aim

The aim of the project was to create a full stack web application to be utilised by staff within a gym to manage memberships, and register members for classes. The MVP for the project was:

    - The app should allow the gym to create and edit Members
    - The app should allow the gym to create and edit Classes
    - The app should allow the gym to book members on specific classes
    - The app should show a list of all upcoming classes
    - The app should show all members that are booked in for a particular class

I modelled the web application on Average Joe's Gym from the film Dodgeball.

## Required Software

- Flask
- Psycopg2

## How to launch the application:

1. Open terminal and type in the following commands:
2. Install Flask
    - pip3 flask
3. Install Psycopg
    - pip3 psycopg
4. Drop the database
    - dropdb callums_gym
5. Create the database
    - psql -d callums_gym -f db/callums_gym.sql
6. Populate the database
    - python3 console.py
7. Load the webpage
    - flask run
8. Open the webpage on http://127.0.0.1:4999/

## Screenshots




