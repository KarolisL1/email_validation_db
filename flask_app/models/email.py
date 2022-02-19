from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Email():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_email( emails ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(emails['email']): 
            flash("Invalid email address!")
        is_valid = False
        return is_valid

    @classmethod
    def all(cls):
        query = "SELECT * FROM email"
        results = connectToMySQL('email_schema').query_db(query)
        return results

    @classmethod
    def save_email(cls, data):
        query = "INSERT INTO email ( name, created_at, updated_at ) VALUES ( %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('email_schema').query_db( query, data )