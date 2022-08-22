from flask import Blueprint, Flask, redirect, render_template, request
from models.location import Location

import repositories.visit_repository as visit_repository
import repositories.lesson_repository as lesson_repository
import repositories.members_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository


locations_blueprint = Blueprint("locations", __name__)


# Index page for displaying all locations

@locations_blueprint.route("/locations")
def locations():
    locations = location_repository.select_all()
    return render_template("locations/all_locations.html", locations=locations)


# Viewing a single locations

@locations_blueprint.route("/locations/<id>")
def show_single_location(id):
    location = location_repository.select(id)
    return render_template("locations/single_location.html", location=location)


# Edit a single location

@locations_blueprint.route("/locations/<id>/edit")
def edit_location(id):
    location = location_repository.select(id)
    return render_template("locations/edit_location.html", location=location)


# Update the location

@locations_blueprint.route("/locations/<id>/edit", methods=["POST"])
def edit_location_post(id):
    name = request.form["name"]
    capacity = request.form["capacity"]
    id = id
    updated_room = Location(name, capacity, id)
    location_repository.update(updated_room)
    return redirect("/locations")



# Delete a single location

@locations_blueprint.route("/locations/<id>/delete", methods=["GET"])
def delete_location(id):
    location_repository.delete(id)
    return redirect("/locations")


# Add a new location

@locations_blueprint.route("/locations/new")
def new_location():
    return render_template("locations/new_location.html")


# Post of new location

@locations_blueprint.route("/locations/new", methods=["POST"])
def add_new_location():
    name = request.form["name"]
    capacity = request.form["capacity"]
    new_location = Location(name, capacity)
    location_repository.save(new_location)
    return redirect("/locations")
