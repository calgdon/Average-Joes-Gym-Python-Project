from flask import Blueprint, Flask, redirect, render_template, request
from models.lesson import Lesson

import repositories.visit_repository as visit_repository
import repositories.lesson_repository as lesson_repository
import repositories.members_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository


lessons_blueprint = Blueprint("lessons", __name__)


# Index page for displaying all lessons

@lessons_blueprint.route("/lessons")
def lessons():
    lessons = lesson_repository.select_all()
    return render_template("lessons/all_lessons.html", lessons=lessons)


# Viewing a single lesson

@lessons_blueprint.route("/lessons/<id>")
def show_lesson(id):
    lesson = lesson_repository.select(id)
    members = visit_repository.select_all_members_in_lesson(lesson)
    return render_template("lessons/single_lesson.html", lesson=lesson, members=members)


# Edit a lesson

@lessons_blueprint.route("/lessons/<id>/edit")
def edit_lesson(id):
    lesson = lesson_repository.select(id)
    locations = location_repository.select_all()
    instructors = instructor_repository.select_all()
    return render_template("/lessons/edit_lesson.html", lesson=lesson, locations=locations, instructors=instructors)

# Update the lesson

@lessons_blueprint.route("/lessons/<id>/edit", methods=["POST"])
def post_edit_lesson(id):
        name = request.form["name"]
        time = request.form["time"]
        date = request.form["date"]
        location_id = request.form["location_id"]
        instructor_id = request.form["instructor_id"]
        capacity = request.form["capacity"]
        id = id
        location = location_repository.select(location_id)
        instructor = instructor_repository.select(instructor_id)
        updated_lesson = Lesson(name, time, date, location, instructor, capacity, id)
        lesson_repository.update(updated_lesson)
        return redirect("/lessons")


# Delete a single lesson

@lessons_blueprint.route("/lessons/<id>/delete", methods=["GET"])
def delete_lesson(id):
    lesson_repository.delete(id)
    return redirect("/lessons")


# Add a new lesson

@lessons_blueprint.route("/lessons/new")
def add_lesson():
    locations = location_repository.select_all()
    instructors = instructor_repository.select_all()
    return render_template("/lessons/add_lesson.html", locations=locations, instructors=instructors)


# Post the new lesson

@lessons_blueprint.route("/lessons/add", methods=["POST"])
def post_new_lesson():
    name = request.form["name"]
    time = request.form["time"]
    date = request.form["date"]
    location_id = request.form["location_id"]
    instructor_id = request.form["instructor_id"]
    capacity = request.form["capacity"]
    location = location_repository.select(location_id)
    instructor = instructor_repository.select(instructor_id)
    new_lesson = Lesson(name, time, date, location, instructor, capacity)
    lesson_repository.save(new_lesson)
    return redirect("/lessons")


