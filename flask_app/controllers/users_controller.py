from flask_app.models import users_model, images_model
from flask_app.controllers import images_controllers
from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask import flash


bcrypt = Bcrypt(app)

# ========== LOGIN / REGISTER PAGE - VIEW - RENDER =========
@app.route("/")
def index():
    return render_template("welcome.html")


# ========= REGISTER - method - ACTION ========
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        print("request.form>>>>>>>>>\n", request.form, "\n")
        if not users_model.User.validate(request.form):
            return redirect("/register")
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        data = {**request.form, "password": pw_hash}
        user_id = users_model.User.register(data)
        session["user_id"] = user_id
        print(f"\nuser_id >>>>>>>> {user_id}")
        print(f"\nsession['user_id'] >>>>>>>> {session['user_id']}")
        return redirect("/home")
    else:
        return render_template("regis_login.html")


# ======== LOGIN - method - ACTION ========
@app.route("/login", methods=["POST"])
def login():
    data = {"email": request.form["email"]}
    user_in_db = users_model.User.get_by_email(data)
    if not user_in_db:
        flash("⚠️Invalid credentials")
        return redirect("/register")
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("⚠️Invalid credentials")
        return redirect("/")
    session["user_id"] = user_in_db.id
    return redirect("/home")


# ======== HOME PAGE - VIEW -RENDER ========
@app.route("/home")
def home():
    if "user_id" not in session:
        flash("⚠️Invalid attempt. Please log in or register.")
        return redirect("/")
    data = {"id": session["user_id"]}
    user = users_model.User.get_by_id(data)
    # all_recipes = Recipe.recipes_dashboard()
    image = images_model.Image.get_one_image_by_id(data)
    return render_template("home.html", user=user, image=image)


# ======== PROFILE - ACTION========
@app.route("/profile/<int:id>", methods=["POST", "GET"])
def profile(id):
    print("PROFILE request.form>>>>>>>>>\n", request.form, "\n")
    if request.method == "POST":
        if not users_model.User.validate(request.form):
            return redirect(f"/profile/{id}")
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        data = {**request.form, "password": pw_hash, "id": session["user_id"]}
        users_model.User.update_by_id(data)
        return redirect(f"/profile/{id}")
    else:
        data = {"id": session["user_id"]}
        user = users_model.User.get_by_id(data)
        image = images_model.Image.get_one_image_by_id(data)
        return render_template("profile.html", user=user, image=image)


# ======== LOGOUT - ACTION ========
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
