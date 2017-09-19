from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource
from marshmallow import Schema, post_dump
from flask import Flask, request

from app import APP
from app import API
from app import DB

class Users(DB.Model):
    """
    Class defines the attributes of a user
    """
    __tablename__ = "users"
    user_id = DB.Column(DB.Integer, primary_key=True)
    first_name = DB.Column(DB.String(50), nullable=False)
    second_name = DB.Column(DB.String(50), nullable=False)
    email = DB.Column(DB.String(128), nullable=False, unique=True)
    phonenumber = DB.Column(DB.String(20), nullable=False, unique=True)
    password = DB.Column(DB.String(197), nullable=False)

    date_created = DB.Column(DB.DateTime, default=DB.func.current_timestamp())

    date_modified = DB.Column(DB.DateTime, default=DB.func.current_timestamp(),
                              onupdate=DB.func.current_timestamp())

