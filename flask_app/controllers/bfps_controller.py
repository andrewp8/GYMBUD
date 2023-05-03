from datetime import datetime
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.controllers import users_controller
from flask_app.models import bfps_model, users_model, images_model
from flask import flash


@app.route("/bfp/<int:id>", methods=["POST", "GET"])
def bfp(id):
    print(">>>print form JS>>>\n", request.form, "\n")
    if request.method == "POST":
        if not bfps_model.Bfp.bfp_validate(request.form):
            return redirect(f"/bfp/{id}")
        data = {**request.form, "user_id": session["user_id"]}
        bfps_model.Bfp.save_calculation(data)
        return redirect(f"/bfp/{id}")
    else:
        if "user_id" not in session:
            flash("⚠️Invalid attempt. Please log in or register.")
            return redirect("/")
        current_date = datetime.now().date()
        formatted_date = current_date.strftime("%Y-%m-%d")
        data = {"id": session["user_id"]}
        user = users_model.User.get_by_id(data)
        image = images_model.Image.get_one_image_by_id(data)
        return render_template(
            "bfp.html", user=user, formatted_date=formatted_date, image=image
        )


@app.route("/bfp/calculate/<int:id>", methods=["POST"])
def calculate_bfp(id):
    if request.method == "POST":
        print("NOTHIONG>>>>>>>>>>>>>>>>>>", request.form)

        return redirect(f"/bfp/{id}")
