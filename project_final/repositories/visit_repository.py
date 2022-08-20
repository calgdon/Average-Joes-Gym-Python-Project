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


# View all members in a certain lesson

def select_all_members_in_lesson(lesson):
    attendees = []
    sql = "SELECT members.id FROM members INNER JOIN visits ON members.id = visits.member_id WHERE visits.lesson_id = %s"
    values = [lesson.id]
    results = run_sql(sql, values)

    for row in results:
        attendee = member_repository.select(row[0])
        attendees.append(attendee)
    return attendees


# Check a member can be added to a lesson

# def check_capacity_if_member_can_be_added_to_lesson(lesson):
#     current_capacity = select_all_members_in_lesson(lesson)
#     class_capacity = lesson_repository.get_capacity(lesson)





# Delete a visit by id

def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Delete all visits

def delete_all():
    sql = "DELETE FROM visits"
    run_sql(sql)
