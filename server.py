from flask_app import app

# ! ALWAYS IMPORT THE CONTROLLERS HERE
from flask_app.controllers import (
    bfps_controller,
    users_controller,
    exercises_controller,
    foods_controller,
    calendars_controller,
)

if __name__ == "__main__":
    app.run(debug=True, port=5001)


# pipenv install flask pymysql flask-bcrypt
