from app import *
import os

SECRET_KEY = os.urandom(24)

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost:5432/driving_school'
SQLALCHEMY_TRACK_MODIFICATIONS = False


