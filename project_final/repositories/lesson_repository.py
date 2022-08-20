from db.run_sql import run_sql
from models.lesson import Lesson
from models.member import Member

import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository

def save(lesson):
    sql = "INSERT INTO lessons (name, time, date, location_id, instructor_id, capacity) values ( %s, %s, %s, %s, %s, %s) returning id"
    values = [lesson.name, lesson.time, lesson.date, lesson.location.id, lesson.instructor.id, lesson.capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    lesson.id = id

# def select(lesson):

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



# def select_all(lesson:)




def update(lesson):
    sql = "UPDATE lessons SET(name, time, date, location_id, instructor_id, capacity) = ( %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [lesson.name, lesson.time, lesson.date, lesson.location.id, lesson.instructor.id, lesson.capacity, lesson.id]
    run_sql(sql, values)


# def delete(lesson):
