from flask import Blueprint, Flask, redirect, render_template, request

import repositories.visit_repository as visit_repository
import repositories.lesson_repository as lesson_repository
import repositories.members_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository

from models.member import Member


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
    visits = visit_repository.all_booking_by_member(id)
    return render_template("members/single_member.html", member=member, visits=visits)


# Edit a single member

@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("members/edit_member.html", member=member)


# Update the member

@members_blueprint.route("/members/<id>/edit", methods=["POST"])
def update_member(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    address = request.form["address"]
    tel_number = request.form["tel_number"]
    email = request.form["email"]
    platinum_member = request.form["platinum_member"]
    id = id
    updated_member = Member(first_name, last_name, date_of_birth, address, tel_number, email, platinum_member, id)
    member_repository.update(updated_member)
    return redirect("/members")


# Add a new member

@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new_member.html")


# Post of new member

@members_blueprint.route("/members/new", methods=["POST"])
def add_new_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    address = request.form["address"]
    tel_number = request.form["tel_number"]
    email = request.form["email"]
    platinum_member = request.form["platinum_member"]
    new_member = Member(first_name, last_name, date_of_birth, address, tel_number, email, platinum_member)
    member_repository.save(new_member)
    return redirect("/members")


# Delete a single member

@members_blueprint.route("/members/<id>/delete", methods=["GET"])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")


