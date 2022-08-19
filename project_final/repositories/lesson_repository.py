from db.run_sql import run_sql
from models.lesson import Lesson
from models.member import Member

def save(lesson):
    sql = "INSERT INTO lessons (name, time, date, location_id, instructor_id, capacity) values ( %s, %s, %s, %s, %s, %s) returning id"
    values = [lesson.name, lesson.time, lesson.date, lesson.location.id, lesson.instructor.id, lesson.capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    lesson.id = id

# def select(lesson):



# def select_all(lesson:)




def update(lesson):
    sql = "UPDATE lessons SET(name, time, date, location_id, instructor_id, capacity) = ( %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [lesson.name, lesson.time, lesson.date, lesson.location.id, lesson.instructor.id, lesson.capacity, lesson.id]
    run_sql(sql, values)


# def delete(lesson):
