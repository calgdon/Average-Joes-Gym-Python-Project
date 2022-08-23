from pickle import TRUE
from db.run_sql import run_sql

from models.visit import Visit
from models.lesson import Lesson
from models.member import Member

import repositories.lesson_repository as lesson_repository
import repositories.members_repository as member_repository
import repositories.location_repository as location_repository
import repositories.instructor_repository as instructor_repository


# Add a member into a lesson

def save(visit):
    sql = "INSERT INTO visits (member_id, lesson_id) VALUES (%s, %s) RETURNING id"
    values = [visit.member.id, visit.lesson.id]
    results = run_sql(sql, values)
    visit.id = results[0]['id']
    return visit


# Select all visits

def select_distinct_lessons():
    visits = []
    sql = "SELECT * lesson_id FROM visits"
    results = run_sql(sql)
    for result in results:
        lesson = lesson_repository.select(result['lesson_id'])
        member = member_repository.select(result['member_id'])
        visit = Visit(member, lesson, result['id'])
        print(visit)
        visits.append(visit)
    return visits



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


# Get the number of members in a certain lesson

def number_of_members_in_lesson(lesson):
    result = select_all_members_in_lesson(lesson)
    return len(result)


# Check which classes have spaces:

def check_which_classes_have_spaces():
    classes_with_spaces = []
    lessons = lesson_repository.select_all()
    for lesson in lessons:
        if check_if_member_can_be_added_to_lesson(lesson):
            classes_with_spaces.append(lesson)
    return classes_with_spaces


# Check if there is space to add member to a lesson

def check_if_member_can_be_added_to_lesson(lesson):
    current_members_in_lesson = number_of_members_in_lesson(lesson)
    capacity_of_lesson = lesson_repository.get_capacity(lesson)
    space_for_members = int(capacity_of_lesson) - \
        int(current_members_in_lesson)
    if space_for_members >= 1:
        return True


# Return the number of spaces available

def number_of_spaces_available_per_lesson(lesson):
    current_members_in_lesson = number_of_members_in_lesson(lesson)
    capacity_of_lesson = lesson_repository.get_capacity(lesson)
    space_for_members = int(capacity_of_lesson) - \
        int(current_members_in_lesson)
    return space_for_members


# Return all the classes and their available spaces


# Get all classes that a member is currently in

def get_all_classes_member_in(member):
    current_lessons = []
    sql = "SELECT lesson_id FROM visits WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)
    for result in results:
        current_lesson = lesson_repository.select(result[0])
        current_lessons.append(current_lesson)
    return current_lessons


# Get all the classes that a member IS NOT currently in:

def get_lessons_member_not_in(member):
    available_lessons = []
    sql = "SELECT DISTINCT lesson_id FROM visits WHERE lesson_id NOT IN (SELECT lesson_id FROM visits WHERE member_id = %s)"
    values = [member.id]
    results = run_sql(sql, values)
    for result in results:
        available_lesson = lesson_repository.select(result[0])
        available_lessons.append(available_lesson)
    return available_lessons



# Delete by member and lesson id

def delete_by_ids(member, lesson):
    sql = "DELETE FROM visits WHERE member_id = %s AND lesson_id = %s"
    values = [member.id, lesson.id]
    run_sql(sql, values)


def find_visits_id(member, lesson):
    sql = "SELECT id FROM visits WHERE member_id = %s AND lesson_id = %s"
    values = [member.id, lesson.id]
    results = run_sql(sql, values)
    result = results[0]['id']
    return result


# Get all the bookings by the member id 

def all_booking_by_member(member_id):
    visits = []
    sql = "SELECT * FROM visits WHERE member_id = %s"
    values = [member_id]
    results = run_sql(sql, values)
    for result in results:
        lesson = lesson_repository.select(result['lesson_id'])
        member = member_repository.select(result['member_id'])
        visit = Visit(member, lesson, result['id'])
        visits.append(visit)
    return visits


# Get all the bookings by lesson id

def all_booking_by_lesson(lesson_id):
    visits = []
    sql = "SELECT * FROM visits WHERE lesson_id = %s"
    values = [lesson_id]
    results = run_sql(sql, values)
    for result in results:
        lesson = lesson_repository.select(result['lesson_id'])
        member = member_repository.select(result['member_id'])
        visit = Visit(member, lesson, result['id'])
        visits.append(visit)
    return visits




# Delete all members from a visit by id

def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Delete all visits

def delete_all():
    sql = "DELETE FROM visits"
    run_sql(sql)
