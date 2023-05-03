# models talk to the DB and init
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash


class Bfp:
    def __init__(self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.bfp = data["bfp"]
        self.weight = data["weight"]
        self.height = data["height"]
        self.age = data["age"]
        self.gender = data["gender"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # ? ======== INSERT CALCULATION RESULT ========
    @classmethod
    def save_calculation(cls, data):
        query = """
        INSERT INTO bfps (user_id, weight, height, age, gender, bfp)
        VALUES (%(user_id)s, %(weight)s, %(height)s, %(age)s, %(gender)s, %(bfp)s);
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return results
        else:
            return False

    # ? ======== BFP VALIDATION ========
    @staticmethod
    def bfp_validate(data):
        is_valid = True
        if len(data["weight"]) < 1:
            is_valid = False
            flash("'weight' is required")
        if len(data["height"]) < 1:
            is_valid = False
            flash("'Height' is required")
        if len(data["age"]) < 1:
            is_valid = False
            flash("'age' is required")
        if "gender" not in data:
            is_valid = False
            flash("'Gender' selection is required")
        return is_valid
