from db.run_sql import run_sql
from models.instructor import Instructor

# Save a new instructor

def save(instructor):
    sql = "INSERT INTO instructors (name) VALUES (%s) RETURNING id"
    values = [instructor.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    instructor.id = id

# Select an instructor by ID

def select(id):
    sql = "SELECT * FROM instructors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        instructor = Instructor(result['name'], result['id'])
    return instructor


# Select all instructors

def select_all():
    instructors = []
    sql = "SELECT * FROM instructors ORDER BY name"
    results = run_sql(sql)
    for result in results:
        instructor = Instructor(result['name'], result['id'])
        instructors.append(instructor)
    return instructors


# Update an instructor

def update(instructor):
    sql = "UPDATE instructors SET (name) = (%s) WHERE id = %s"
    values = [instructor.name, instructor.id]
    run_sql(sql, values)


# Delete a instructor by id

def delete(id):
    sql = "DELETE FROM instructors WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Delete all instructors

def delete_all():
    sql = "DELETE FROM instructors"
    run_sql(sql)
