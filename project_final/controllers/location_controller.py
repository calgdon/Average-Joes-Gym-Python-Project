from flask import Blueprint, Flask, redirect, render_template, request

import repositories.visit_repository as visit_repository
import repositories.lesson_repository as lesson_repository
import repositories.members_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository


locations_blueprint = Blueprint("locations", __name__)


@locations_blueprint.route("/locations")
def locations():
    locations = location_repository.select_all()
    return render_template("locations/all_locations.html", locations=locations)
