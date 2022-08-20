from db.run_sql import run_sql

from models.visit import Visit
from models.lesson import Lesson
from models.member import Member

import repositories.lesson_repository as lesson_repository
import repositories.members_repository as member_repository

def save(visit):
    sql = "INSERT INTO visits (member_id, lesson_id) VALUES (%s, %s) RETURNING id"
    values = (visit.member.id, visit.lesson.id)
    results = run_sql(sql, values)
    visit.id = results[0]['id']
    return visit


# Delete a visit by id

def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Delete all visits

def delete_all():
    sql = "DELETE FROM visits"
    run_sql(sql)
