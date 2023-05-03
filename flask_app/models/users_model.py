# models talk to the DB and init
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re

NAME_REGEX = re.compile(r"^[a-zA-Z]{2}")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
PASSWORD_REGEX = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$")


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # ? ======== CREATE USER ========
    @classmethod
    def register(cls, data):
        query = """
      INSERT INTO users (first_name, last_name, email, password)
      VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
  """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return results
        else:
            return False

    # ? ======== READ ONE (get by EMAIL) =========
    @classmethod
    def get_by_email(cls, data):
        query = """
            SELECT * FROM users 
            WHERE email = %(email)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        else:
            return cls(results[0])

    # ? ======== READ ONE (get by ID) ========
    @classmethod
    def get_by_id(cls, data):
        query = """
            SELECT * FROM users 
            WHERE id = %(id)s
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        else:
            return cls(results[0])

    # ? ======== UPDATE ONE (get by ID) ========
    @classmethod
    def update_by_id(cls, data):
        query = """
            UPDATE users
            SET first_name = %(first_name)s,
                last_name = %(last_name)s,
                email = %(email)s,
                password = %(password)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    # ? ======== REGISTER VALIDATION ========
    @staticmethod
    def validate(data):
        is_valid = True
        if not NAME_REGEX.match(data["first_name"]):
            flash("⚠️First name must be at least 2 characters and only letter!")
            is_valid = False

        if not NAME_REGEX.match(data["last_name"]):
            flash("⚠️Last name must be at least 2 characters and only letter!")
            is_valid = False

        if not EMAIL_REGEX.match(data["email"]):
            flash("⚠️Invalid email address!")
            is_valid = False
        else:
            check_in_email = {"email": data["email"]}
            db_email = User.get_by_email(check_in_email)
            if db_email:
                is_valid = False
                flash("⚠️Email already taken.")

        if not PASSWORD_REGEX.match(data["password"]):
            is_valid = False
            flash(
                "⚠️You have to have at least 8 characters in your password, 1 number, and 1 uppercase letter"
            )
        elif not data["password"] == data["confirm_password"]:
            is_valid = False
            flash("⚠️Password doesn't match")

        return is_valid
