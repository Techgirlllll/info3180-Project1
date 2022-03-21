import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = 'postgres://sfnpwqxthvcljn:a3f09150eb359e05bb9c277a6dacf441f86fb6d57d974997a3d354ac7a3d6235@ec2-52-22-226-8.compute-1.amazonaws.com:5432/dahlo59pomd91f'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER= './uploads'
    