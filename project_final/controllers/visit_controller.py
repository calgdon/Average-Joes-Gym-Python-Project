from unicodedata import name
from flask import Blueprint, Flask, redirect, render_template, request
from controllers.lesson_controller import lessons

import repositories.visit_repository as visit_repository
import repositories.lesson_repository as lesson_repository
import repositories.members_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository

from models.visit import Visit

visits_blueprint = Blueprint("visits", __name__)


# index page for adding member into a lesson


@visits_blueprint.route("/visits")
def select_member():
    members = member_repository.select_all()
    return render_template("visits/index.html", members=members)


# Post page for sending the selected member

@visits_blueprint.route("/visits", methods=["POST"])
def select_member_post():
    selected_member_id = request.form["member_id"]
    return redirect(f"/visits/{selected_member_id}")


# Get page for adding the member to the class


@visits_blueprint.route("/visits/<id>", methods=["GET"])
def add_lesson_to_member(id):

    member = member_repository.select(id)
    available_lessons = visit_repository.get_lessons_member_not_in(member)
    members_available_lessons = []
    for available_lesson in available_lessons:
        if visit_repository.check_if_member_can_be_added_to_lesson(available_lesson):
            members_available_lessons.append(available_lesson)
    return render_template("visits/add_lesson.html", member=member, lessons=members_available_lessons)


# Add the lesson to the selected member

@visits_blueprint.route("/visits/<id>", methods=["POST"])
def select_class_for_member(id):
    member = member_repository.select(id)
    lesson_id = request.form["lesson_id"]
    lesson = lesson_repository.select(lesson_id)
    new_visit = Visit(member, lesson)
    visit_repository.save(new_visit)
    member = member_repository.select(id)
    return redirect ("/")




@visits_blueprint.route("/visits/<id>/delete", methods=['GET'])
def delete_task(id):
    visit_repository.delete(id)
    return redirect('/')
