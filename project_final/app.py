from flask import Flask, render_template

from controllers.visit_controller import visits_blueprint
from controllers.instructor_controller import instructors_blueprint
from controllers.lesson_controller import lessons_blueprint
from controllers.member_controller import members_blueprint
from controllers.location_controller import locations_blueprint

app = Flask(__name__)

app.register_blueprint(visits_blueprint)
app.register_blueprint(instructors_blueprint)
app.register_blueprint(lessons_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(locations_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)