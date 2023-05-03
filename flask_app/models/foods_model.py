# models talk to the DB and init
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash


class Food:
    def __init__(self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.meal_type = data["meal_type"]
        self.meal_name = data["meal_name"]
        self.calories = data["calories"]
        self.protein = data["protein"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # ? ======== CREATE EXERCISE ========
    @classmethod
    def create_food(cls, data):
        query = """
        INSERT INTO foods (user_id, meal_type, meal_name, calories, protein)
        VALUES (%(user_id)s, %(meal_type)s, %(meal_name)s, %(calories)s, %(protein)s);
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return results
        else:
            return False

    # ? ======== READ FOODS (get by USER_ID & CURRENT DATE YYYY_MM_DD FORMAT) ========
    @classmethod
    def get_theday_foods(cls, data):
        query = """
          SELECT * FROM foods
          WHERE user_id = %(user_id)s AND DATE_FORMAT(created_at, '%%%%Y-%%%%m-%%%%d') = %(current_date)s
          ORDER BY meal_type;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        all_foods = []
        if results:
            for row in results:
                this_food = cls(row)
                all_foods.append(this_food)
        return all_foods

    # ? ======== FOOD CALCULATOR ========
    @classmethod
    def calculate_foods(cls, data):
        query = """
        SELECT SUM(calories), SUM(protein)
        FROM foods 
        WHERE user_id = %(user_id)s AND DATE_FORMAT(created_at, '%%%%Y-%%%%m-%%%%d') = %(current_date)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return results[0]
        else:
            return False

    # ? ======== FOOD VALIDATION ========
    @staticmethod
    def food_validate(data):
        is_valid = True
        if len(data["meal_type"]) < 1:
            is_valid = False
            flash("'Meal type' is required")
        if len(data["meal_name"]) < 1:
            is_valid = False
            flash("'Meal name' is required")
        if len(data["calories"]) < 1:
            is_valid = False
            flash("'Calories' is required")
        if len(data["protein"]) < 1:
            is_valid = False
            flash("'Protein' is required")
        return is_valid
