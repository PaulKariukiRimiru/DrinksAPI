from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
"""
Setup the APP
"""
APP = Flask(__name__)
APP.config.from_object('config')

DB = SQLAlchemy(APP)
API = Api(APP)
