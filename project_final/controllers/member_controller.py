from flask import Blueprint, Flask, redirect, render_template, request

import repositories.visit_repository as visit_repository
import repositories.lesson_repository as lesson_repository
import repositories.members_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository


members_blueprint = Blueprint("members", __name__)


@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/all_members.html", members=members)
