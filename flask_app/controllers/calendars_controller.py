from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.controllers import users_controller
from flask_app.models import users_model, images_model
from flask import flash


@app.route("/calendar/<int:id>")
def calendar(id):
    if "user_id" not in session:
        flash("⚠️Invalid attempt. Please log in or register.")
        return redirect("/")
    data = {"id": session["user_id"]}
    user = users_model.User.get_by_id(data)
    image = images_model.Image.get_one_image_by_id(data)
    return render_template("calendar.html", user=user, image=image)
