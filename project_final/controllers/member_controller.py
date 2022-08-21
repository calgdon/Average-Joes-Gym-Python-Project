from flask import Blueprint, Flask, redirect, render_template, request

import repositories.visit_repository as visit_repository
import repositories.lesson_repository as lesson_repository
import repositories.members_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository


members_blueprint = Blueprint("members", __name__)


# Index page for displaying all members

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/all_members.html", members=members)


# Viewing a single member

@members_blueprint.route("/members/<id>")
def show_single_member(id):
    member = member_repository.select(id)
    return render_template("members/single_member.html", member=member)


# Edit a single member

@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("members/edit_member.html", member=member)


# Delete a single member

@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")


