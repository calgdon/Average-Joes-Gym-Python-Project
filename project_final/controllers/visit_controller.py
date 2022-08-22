from flask import Blueprint, Flask, redirect, render_template, request

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
    # lessons = lesson_repository.select_all()
    # instructors = instructor_repository.select_all()
    # locations = location_repository.select_all()
    return render_template("visits/index.html", members=members)
    # lessons=lessons, instructors=instructors, locations=locations)


# Post page for sending the selected member

@visits_blueprint.route("/visits", methods=["POST"])
def select_member_post():
    selected_member_id = request.form["member_id"]
    return redirect(f"/visits/{selected_member_id}")


@visits_blueprint.route("/visits/<id>", methods=["GET"])
def add_lesson_to_member(id):
    member = member_repository.select(id)
    lesson_id = request.form["lesson_id"]
    new_lesson = lesson_repository.select(lesson_id)
    new_visit = Visit(member, new_lesson)
    return render_template("visits/add_lesson.html")


# Add the lesson to the selected member

# @visits_blueprint.route("/visits/<id>", methods=["GET"])
# def select_class_for_member(id):
#     member =
#     lesson_id = request.form["lesson_id"]
#     new_member = member_repository.select(member)
#     new_lesson = lesson_repository.select(lesson_id)
#     new_visit = Visit(new_member, new_lesson)
#     visit_repository.save(new_visit)
#     member = member_repository.select(id)
#     return render_template("visits/add_lesson.html", member=member)


# Post page for submitting the new visit

# @visits_blueprint.route("/visits/<id>", methods=["GET"])
# def select():
#     member_id = request.form["member_id"]
#     # lesson_id = request.form["lesson_id"]
#     new_member = member_repository.select(member_id)
#     # new_lesson = lesson_repository.select(lesson_id)
#     new_visit = Visit(new_member, new_lesson)
#     visit_repository.save(new_visit)
#     return redirect ("/")
