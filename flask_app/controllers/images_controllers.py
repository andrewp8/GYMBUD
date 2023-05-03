import os
from werkzeug.utils import secure_filename

from flask_app import app
from flask import render_template, request, flash, redirect, session
from flask_app.models import images_model
from flask_app.controllers import users_controller

UPLOAD_FOLDER = "flask_app\\static\\img"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ======== PROFILE/IMAGE - UPLOAD========
@app.route("/profile/<int:id>/image", methods=["POST"])
def profile_picture(id):
    print("picture files>>>>>>\n", request.files["file"], "\n")
    # check if the post request has a file part
    if "file" not in request.files:
        flash("No file part")
        return redirect("/")

    # if file part exists in form, save to variable
    file = request.files["file"]

    # if the user does not select a file, browser submits an empty part without filename
    if file.filename == "":
        flash("No selected file")
        return redirect("/")

    # if valid file submitted, save into local folder (does *NOT* save in database!)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        # saves the image into the static/img folder
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        # saves img filename in SQL db for reference
        data = {"user_id": session["user_id"], "filename": filename}
        new_file_id = images_model.Image.save(data)
        # session["image_id"] = new_file_id
        # print("session[image_id]>>>>>>", session["image_id"])

        # *NOTE* if storing images on 3rd party site, the file.save() command will instead be a call to the image hosting site to save it, store the image host URL instead of filename, and use image host URL directly in img tag for src attribute

    return redirect(f"/profile/{id}")


# ======== VIEW PROFILE IMAGE BY IMAGE ID ========


""" 

    # ? Get image from FORM as save to MySQL as BLOB datatype
    img = request.files["image"]  # Get the uploaded image
    img = Image.open(io.BytesIO(img.read()))  # Open the image with Pillow
    img = img.convert("RGB")  # Convert the image to RGB
    img_bytes = io.BytesIO()  # Convert the image to bytes
    img.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()
    print("img_bytes>>>>>>\n", img_bytes, "\n")
 """


""" 

    # Read the image from the request object
    img_bytes = io.BytesIO(request.files["image"].read())
    img = Image.open(img_bytes)

    # Convert the image to JPEG format
    output = io.BytesIO()
    img.save(output, format="JPEG")
    jpeg_image = output.getvalue()
 """


""" 

   # Retrieve the image from the Flask request object
    image_file = request.files["image"]

    # Read the image data from the file object
    image_data = image_file.read()

    # Convert the image data to a Pillow image object
    image = Image.open(io.BytesIO(image_data))
    image = image.convert("RGB")
    # Convert the image to a byte string
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    image_bytes = buffered.getvalue()

 """
