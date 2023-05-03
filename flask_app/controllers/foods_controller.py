from datetime import datetime
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.controllers import users_controller
from flask_app.models import users_model, foods_model, images_model
from flask import flash


@app.route("/food/<int:id>", methods=["POST", "GET"])
def food(id):
    print("food>>>>>\n", request.form, "\n")
    if request.method == "POST":
        if not foods_model.Food.food_validate(request.form):
            return redirect(f"/food/{id}")
        data = {**request.form, "user_id": session["user_id"]}
        foods_model.Food.create_food(data)
        return redirect(f"/food/{id}")
    else:
        if "user_id" not in session:
            flash("⚠️Invalid attempt. Please log in or register.")
            return redirect("/")
        current_date = datetime.now().date()
        formatted_date = current_date.strftime("%Y-%m-%d")
        data = {"id": session["user_id"]}
        user = users_model.User.get_by_id(data)
        food_data = {"user_id": session["user_id"], "current_date": formatted_date}
        foods = foods_model.Food.get_theday_foods(food_data)
        calculates = foods_model.Food.calculate_foods(food_data)
        print("foods>>>>>>", calculates)
        image = images_model.Image.get_one_image_by_id(data)
        return render_template(
            "food.html",
            user=user,
            calculates=calculates,
            foods=foods,
            formatted_date=formatted_date,
            image=image,
        )
