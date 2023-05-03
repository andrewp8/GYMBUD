# models talk to the DB and init
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
