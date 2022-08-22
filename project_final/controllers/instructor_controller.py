from flask import Blueprint, Flask, redirect, render_template, request

import repositories.visit_repository as visit_repository
import repositories.lesson_repository as lesson_repository
import repositories.members_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository

from models.instructor import Instructor


instructors_blueprint = Blueprint("instructors", __name__)


# Index page for displaying all instructors

@instructors_blueprint.route("/instructors")
def instructors():
    instructors = instructor_repository.select_all()
    return render_template("instructors/all_instructors.html", instructors=instructors)


# Viewing a single instructor

@instructors_blueprint.route("/instructors/<id>")
def show_single_instructor(id):
    instructor = instructor_repository.select(id)
    return render_template("instructors/single_instructor.html", instructor=instructor)


# Edit an instructor

@instructors_blueprint.route("/instructors/<id>/edit")
def edit_instructor(id):
    instructor = instructor_repository.select(id)
    return render_template("instructors/edit_instructor.html", instructor=instructor)


# Update the instructor

@instructors_blueprint.route("/instructors/<id>/edit", methods=["POST"])
def post_updated_instructor(id):
    name = request.form["name"]
    id = id
    updated_instructor = Instructor(name, id)
    instructor_repository.update(updated_instructor)
    return redirect("/locations")


# Delete a single instructor

@instructors_blueprint.route("/instructors/<id>/delete", methods=["GET"])
def delete_instructor(id):
    instructor_repository.delete(id)
    return redirect("/instructors")


# Add a new instructor

@instructors_blueprint.route("/instructors/new", methods=["GET"])
def add_instructor():
    return render_template("instructors/new_instructor.html")


# Post new instructor

@instructors_blueprint.route("/instructors/new", methods=["POST"])
def post_new_instructor():
    name = request.form["name"]
    new_instructor = Instructor(name)
    instructor_repository.save(new_instructor)
    return redirect("/instructors")
