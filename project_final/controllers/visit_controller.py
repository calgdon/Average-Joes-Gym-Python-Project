from flask import Blueprint, Flask, redirect, render_template, request

from models.visit import Visit

import repositories.visit_repository as visit_repository
import repositories.lesson_repository as lesson_repository
import repositories.members_repository as member_repository

visits_blueprint = Blueprint("visits", __name__)

# Index

@visits_blueprint.route("/visits")
