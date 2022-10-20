# Average Joes Gym Booking Application

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
    
Extensions that I completed:    

    - Classes could have a maximum capacity, and users can only be added while there is space remaining.
    - Users cannot be added twice to one class
    - The app has Instructors who can be assigned to a class

I modelled the web application on Average Joe's Gym from the film Dodgeball.

## Required Software

- Flask
    - pip3 install Flask
- Psycopg2
    - pip3 psycopg

## How to launch the application:

All commands to be entered into the Terminal:

1. Clone the repository:

    - git clone https://github.com/calgdon/Average-Joes-Gym-Python-Project.git 
    
2. Drop the database if previously cloned or you happen to have a similar database called callums_gym:

    - dropdb callums_gym
    
3. Create the database:

    - psql -f callums_gym -f db/callums_gym.sql
    
4. Populate the database:

    - python3 console.py
    
5. Load the webpage:

    - flask run
    
6. Open the webpage by copying http://127.0.0.1:4999/ into your browser

## Screenshots

### Homepage
<img width="1280" alt="Screenshot 2022-10-07 at 16 43 57" src="https://user-images.githubusercontent.com/108418393/194594519-9cf0bf2c-c3c2-4cdd-87ca-5ed5a157f616.png">

### Selected members page displaying their details and classes currently enrolled in
<img width="1280" alt="Screenshot 2022-10-07 at 16 43 39" src="https://user-images.githubusercontent.com/108418393/194594600-eaee4f04-220f-4633-83a8-a6d014ac9cce.png">

### Select a member to add to a lesson
<img width="1280" alt="Screenshot 2022-10-07 at 16 42 56" src="https://user-images.githubusercontent.com/108418393/194594837-652ce832-2d69-4cbd-843e-e5e8bae48923.png">

### Select the lesson to add the selected member to
<img width="1280" alt="Screenshot 2022-10-07 at 16 43 20" src="https://user-images.githubusercontent.com/108418393/194594932-7e753dfb-9c4d-4239-bb18-4bca9ea60d43.png">

### View all members in a selected lesson
<img width="1280" alt="Screenshot 2022-10-07 at 16 48 01" src="https://user-images.githubusercontent.com/108418393/194595111-c1e79519-9771-47c1-b956-662d9c45df1b.png">

