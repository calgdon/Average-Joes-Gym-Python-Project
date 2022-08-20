from db.run_sql import run_sql
from models.instructor import Instructor

# save a new instructor

def save(instructor):
    sql = "INSERT INTO instructors (name) VALUES (%s) RETURNING id"
    values = [instructor.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    instructor.id = id

# select an instructor by ID

def select(id):
    sql = "SELECT * FROM instructors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        instructor = Instructor(result['name'], result['id'])
    return instructor
