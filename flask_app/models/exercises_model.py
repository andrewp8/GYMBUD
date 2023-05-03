# models talk to the DB and init
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash


class Exercise:
    def __init__(self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.muscle_group = data["muscle_group"]
        self.exercise_name = data["exercise_name"]
        self.rep = data["rep"]
        self.num_set = data["num_set"]
        self.max_weight = data["max_weight"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # ? ======== CREATE EXERCISE ========
    @classmethod
    def create_exercise(cls, data):
        query = """
        INSERT INTO exercises (user_id, muscle_group, exercise_name, rep, num_set, max_weight)
        VALUES (%(user_id)s, %(muscle_group)s, %(exercise_name)s, %(rep)s, %(num_set)s, %(max_weight)s);
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return results
        else:
            return False

    # ? ======== READ EXERCISES (get by ID & CURRENT DATE YYYY_MM_DD FORMAT) ========
    @classmethod
    def get_theday_exercises(cls, data):
        # * https://stackoverflow.com/questions/16531116/python-valueerror-unsupported-format-character-y-0x59
        query = """
          SELECT * FROM exercises
          WHERE user_id = %(user_id)s AND DATE_FORMAT(created_at, '%%%%Y-%%%%m-%%%%d') = %(current_date)s
          ORDER BY muscle_group;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        all_exercises = []
        if results:
            for row in results:
                this_exercise = cls(row)
                all_exercises.append(this_exercise)
        return all_exercises

    # ? ======== EXERCISE VALIDATION ========
    @staticmethod
    def exercise_validate(data):
        is_valid = True
        rep = data["rep"]
        num_set = data["num_set"]
        max_weight = data["max_weight"]
        if len(data["muscle_group"]) < 1:
            is_valid = False
            flash("'Muscle group' is required")
        if len(data["exercise_name"]) < 1:
            is_valid = False
            flash("'Exercise name' is required")
        if int(rep) < 1:
            is_valid = False
            flash("'# of rep' is required")
        if int(num_set) < 1:
            is_valid = False
            flash("'# of set' is required")
        if int(max_weight) < 1:
            is_valid = False
            flash("'Max weight' is required")
        return is_valid
