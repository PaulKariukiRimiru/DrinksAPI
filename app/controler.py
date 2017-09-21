from flask import Flask, request
from flask.ext.restful import Resource, Api
from flask.ext.sqlalchemy import SQLAlchemy
from marshmallow import Schema, post_dump
from werkzeug.security import generate_password_hash

from app import API, DB
from app.models import Users
class UserSchema(Schema):
    class Meta:
        model = Users
    @post_dump(raw=True)
    def wrap_if_many(self, data, many=False):
        if many:
            return {'users':data}
        return data
    def make_object(self, data):
        assert 'email' in data, 'must specify email in data'
        return (Users(first_name=data['first_name'], second_name=data['second_name'],
                      email=data['email'], phonenumber=data['phonenumber'], 
                      password=data['password']))
