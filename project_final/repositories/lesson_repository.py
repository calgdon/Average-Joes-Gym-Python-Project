from db.run_sql import run_sql
from models.lesson import Lesson
from models.member import Member

import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository

# Save a single lesson

def save(lesson):
    sql = "INSERT INTO lessons (name, time, date, location_id, instructor_id, capacity) values ( %s, %s, %s, %s, %s, %s) returning id"
    values = [lesson.name, lesson.time, lesson.date, lesson.location.id, lesson.instructor.id, lesson.capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    lesson.id = id

# Select a single lesson by ID

def select(id):
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        instructor = instructor_repository.select(result["instructor_id"])
        location = location_repository.select(result["location_id"])
        lesson = Lesson(result['name'], result['time'], result['date'], location, instructor, result['capacity'], result['id'])
    return lesson


# Select all lessons

def select_all():
    lessons = []
    sql = "SELECT * FROM lessons"
    results = run_sql(sql)
    for result in results:
        instructor = instructor_repository.select(result["instructor_id"])
        location = location_repository.select(result["location_id"])
        lesson = Lesson(result['name'], result['time'], result['date'], location, instructor, result['capacity'], result['id'])
        lessons.append(lesson)
    return lessons


# Update a lesson

def update(lesson):
    sql = "UPDATE lessons SET(name, time, date, location_id, instructor_id, capacity) = ( %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [lesson.name, lesson.time, lesson.date, lesson.location.id, lesson.instructor.id, lesson.capacity, lesson.id]
    run_sql(sql, values)


# Delete a lesson by id

def delete(id):
    sql = "DELETE FROM lessons WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Delete all lessons

def delete_all():
    sql = "DELETE FROM lessons"
    run_sql(sql)


# Check capacity of the lesson - this is returning a list

def get_capacity(lesson):
    sql = "SELECT lessons.capacity FROM lessons INNER JOIN visits ON visits.lesson_id = lessons.id WHERE lessons.id = %s"
    values = [lesson.id]
    results = run_sql(sql, values)
    return results[0]

    

