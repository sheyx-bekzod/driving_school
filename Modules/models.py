from app import *

db = SQLAlchemy()


def setup(app):
  app.config.from_object('Modules.config')
  db.app = app
  db.init_app(app)
  migrate = Migrate(app, db)
  return db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String())
    password = db.Column(db.String())
    director = db.Column(db.Boolean())
    admin = db.Column(db.Boolean())


class Frames(db.Model):
    __tablename__ = 'frames'
    id = db.Column(db.Integer, primary_key=True)
    frame_name = db.Column(db.String())
    frame_last_name = db.Column(db.String())
    frame_password = db.Column(db.String())
    frame_email = db.Column(db.String())
    frame_jobs = db.relationship("Jobs", backref="frame")

    # frame_job

class Jobs(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String)
    job_frames = db.Column(db.Integer, db.ForeignKey('frames.id'))
