from flask import Blueprint, Flask, redirect, render_template, request

import repositories.visit_repository as visit_repository
import repositories.lesson_repository as lesson_repository
import repositories.members_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository

visits_blueprint = Blueprint("visits", __name__)

# index page for adding member into a lesson

@visits_blueprint.route("/visits" )
def visits():
    members = member_repository.select_all()
    lessons = lesson_repository.select_all()
    instructors = instructor_repository.select_all()
    locations = location_repository.select_all()
    return render_template("visits/index.html", members=members, lessons=lessons, instructors=instructors, locations=locations)

# index page for when submitting the form to add member to lesson


# @visits_blueprint.route("/visits", methods=["POST"])
# def add_member():

