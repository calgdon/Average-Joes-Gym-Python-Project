from flask import Blueprint, Flask, redirect, render_template, request

import repositories.visit_repository as visit_repository
import repositories.lesson_repository as lesson_repository
import repositories.members_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository


instructors_blueprint = Blueprint("instructors", __name__)


@instructors_blueprint.route("/instructors")
def instructors():
    instructors = instructor_repository.select_all()
    return render_template("instructors/all_instructors.html", instructors=instructors)
