from db.run_sql import run_sql
from models.location import Location


def save(location):
    sql = "INSERT INTO locations (name) VALUES (%s) RETURNING id"
    values = [location.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    location.id = id
