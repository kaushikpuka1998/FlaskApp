"""
This module defines the rest-api-details
"""
from flask import Blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # pylint: disable=import-error
from marshmallow import fields
from marshmallow import Schema

rest_controller = Flask(__name__)
app_file4 = Blueprint(
    "rest", __name__, template_folder="templates", static_folder="static"
)
rest_controller.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://testuser:1234@localhost:5432/recipes"

rest_controller.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(rest_controller)


"""
This module defines the Recipe model
"""


class Recipe(db.Model):

    """
    Represents a recipe in the database.

    Attributes:
        id (int): The unique identifier of the recipe.
        name (str): The name of the recipe.
        description (str): The description of the recipe.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return self.name

    @classmethod
    def find_by_name(cls, name):
        """
        Find a recipe by name.

        Args:
            name (str): The name of the recipe to find.

        Returns:
            The Recipe object with the given name, or None if not found.
        """
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        """
        Find a recipe by ID.

        Args:
            _id (int): The ID of the recipe to find.

        Returns:
            The Recipe object with the given ID, or None if not found.
        """
        return cls.query.get_or_404(_id)

    @classmethod
    def find_all(cls):
        """
        Find all recipes in the database.

        Returns:
            A list of all Recipe objects in the database.
        """
        return cls.query.all()

    def save(self):
        """
        Save the current recipe to the database.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Delete the current recipe from the database.
        """
        db.session.delete(self)
        db.session.commit()


class RecipeSchema(Schema):

    """
    Represents a marshmallow schema for the Recipe model.

    Attributes:
        id (int): The unique identifier of the recipe.
        name (str): The name of the recipe.
        description (str): The description of the recipe.
    """

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
