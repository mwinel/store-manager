import re


class Validation:

    def user_validation(self, username, email, password):
        if not username:
            return "username field missing."
        if not email:
            return "email field missing."
        if not password:
            return "password field missing."
        if username == " " or email == " " or password == " ":
            return "fields cannot be left empty."
        if not re.match("^[a-zA-Z0-9_.-]+$", username):
            return "username should not have spaces."
        if len(password) <= 5:
            return "password too short."

    def product_validation(self, name, description, quantity, price):
        if not name:
            return "name field missing."
        if not description:
            return "description field missing."
        if not quantity:
            return "quantity field missing."
        if not price:
            return "price field missing."
        if name == " " or description == " ":
            return "fields cannot be empty."
        if quantity == " " or price == " ":
            return "fields cannot be empty."
