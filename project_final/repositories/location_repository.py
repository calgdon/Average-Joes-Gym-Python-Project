from db.run_sql import run_sql
from models.location import Location

# Save a single location

def save(location):
    sql = "INSERT INTO locations (name) VALUES (%s) RETURNING id"
    values = [location.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    location.id = id

# Select a location by ID

def select(id):
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        location = Location(result['name'], result['id'])
    return location


# Delete a location by id

def delete(id):
    sql = "DELETE FROM locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Delete all locations

def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)
