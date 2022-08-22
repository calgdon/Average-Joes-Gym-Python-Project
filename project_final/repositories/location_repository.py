from db.run_sql import run_sql
from models.location import Location

# Save a single location

def save(location):
    sql = "INSERT INTO locations (name, capacity) VALUES (%s, %s) RETURNING id"
    values = [location.name, location.capacity]
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
        location = Location(result['name'], result['capacity'], result['id'])
    return location


# Select all locations

def select_all():
    locations = []
    sql = "SELECT * FROM locations ORDER BY name"
    results = run_sql(sql)
    for row in results:
        location = Location(row['name'], row['capacity'], row['id'])
        locations.append(location)
    return locations


# Update a location

def update(location):
    sql = "UPDATE locations SET (name, capacity) = (%s, %s) WHERE id = %s"
    values = [location.name, location.capacity, location.id]
    run_sql(sql, values)


# Delete a location by id

def delete(id):
    sql = "DELETE FROM locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Delete all locations

def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)
