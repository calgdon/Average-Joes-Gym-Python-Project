from db.run_sql import run_sql
from models.instructor import Instructor

def save(instructor):
    sql = "INSERT INTO instructors (name) VALUES (%s) RETURNING id"
    values = [instructor.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    instructor.id = id