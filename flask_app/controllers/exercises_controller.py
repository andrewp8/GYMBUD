from datetime import datetime
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.controllers import users_controller
from flask_app.models import users_model, exercises_model, images_model
from flask import flash


@app.route("/exercise/<int:id>", methods=["POST", "GET"])
def exercise(id):
    print("exercise>>>>>\n", request.form, "\n")
    if request.method == "POST":
        if not exercises_model.Exercise.exercise_validate(request.form):
            return redirect(f"/exercise/{id}")
        data = {**request.form, "user_id": session["user_id"]}
        exercises_model.Exercise.create_exercise(data)
        return redirect(f"/exercise/{id}")
    else:
        if "user_id" not in session:
            flash("⚠️Invalid attempt. Please log in or register.")
            return redirect("/")
        current_date = datetime.now().date()
        formatted_date = current_date.strftime("%Y-%m-%d")
        data = {"id": session["user_id"]}
        user = users_model.User.get_by_id(data)
        exercise_data = {"user_id": session["user_id"], "current_date": formatted_date}
        exercises = exercises_model.Exercise.get_theday_exercises(exercise_data)
        print("exercises>>>>>>", exercises)
        image = images_model.Image.get_one_image_by_id(data)
        return render_template(
            "exercise.html",
            user=user,
            exercises=exercises,
            formatted_date=formatted_date,
            image=image,
        )
