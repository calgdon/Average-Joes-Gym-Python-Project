from flask import Blueprint, Flask, redirect, render_template, request

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





# Delete a single lesson

@lessons_blueprint.route("/lessons/<id>/delete", methods=["POST"])
def delete_lesson(id):
    lesson_repository.delete(id)
    return redirect("/lessons")
