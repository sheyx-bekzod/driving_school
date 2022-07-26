from flask import Flask, render_template, redirect, request, json, jsonify, flash, url_for, session, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_migrate import Migrate


app = Flask(__name__)


from Modules.models import *
from Modules.config import *
from Modules.routes.routes import *

db = setup(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()
