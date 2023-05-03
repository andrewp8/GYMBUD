from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Image:
    def __init__(self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.filename = data["filename"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # ? ======== UPLOAD IMAGE ========
    @classmethod
    def save(cls, data):
        query = """
        SELECT * FROM images WHERE user_id = %(user_id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            query = """
            UPDATE images
            SET filename = %(filename)s 
            WHERE user_id = %(user_id)s;
        """
            results = connectToMySQL(DATABASE).query_db(query, data)
        else:
            query = """
            INSERT INTO images (user_id, filename)
            VALUES (%(user_id)s, %(filename)s);
        """
            results = connectToMySQL(DATABASE).query_db(query, data)

    # ? ======== GET ONE PICTURE (by ID) ========
    @classmethod
    def get_one_image_by_id(cls, data):
        query = """
        SELECT * FROM images WHERE user_id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        print("get_one_image_by_id>>>>>>>>>>>>", results)
        if len(results) > 0:
            image = cls(results[0])
            return image
        else:
            return False
