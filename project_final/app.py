from flask import Flask, render_template

from controllers.visit_controller import visits_blueprint
from controllers.instructor_controller import instructors_blueprint
from controllers.lesson_controller import lessons_blueprint
from controllers.member_controller import members_blueprint
from controllers.location_controller import locations_blueprint

import repositories.lesson_repository as lesson_repository
import repositories.visit_repository as visit_repository

app = Flask(__name__)

app.register_blueprint(visits_blueprint)
app.register_blueprint(instructors_blueprint)
app.register_blueprint(lessons_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(locations_blueprint)

@app.route('/')
def home():
    lessons = lesson_repository.select_all()
    return render_template('index.html', lessons=lessons)

if __name__ == '__main__':
    app.run(debug=True)