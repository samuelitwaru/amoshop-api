import os


class BaseConfig(object):
    """Base config class"""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SECRET_KEY = 'AasHy7I8484K8I32seu7nni8YHHu6786gi'
    TIMEZONE = "Africa/Kampala"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_LOGOS_DEST = "app/models/media/"
    UPLOADED_LOGOS_URL = "app/models/media/"

    # HOST_ADDRESS = "http://192.168.1.117:8000"
    # HOST_ADDRESS = "http://127.0.0.1:8000"
    # HOST_ADDRESS = "https://traveler-ug.herokuapp.com"
    DATETIME_FORMAT = "%B %d %Y, %I:%M %p %z"
    DATE_FORMAT = "%B %d %Y %z"
    DEFAULT_CURRENCY = "UGX"
    

class ProductionConfig(BaseConfig):
    """Production specific config"""
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://samuelitwaru:password@localhost/traveler'  # TODO => MYSQL
    SQLALCHEMY_DATABASE_URI = 'sqlite:///models/database.db'
    

class DevelopmentConfig(BaseConfig):
    """Development environment specific config"""
    DEBUG = True
    MAIL_DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:bratz123@localhost/traveler'  # TODO => MYSQL
    SQLALCHEMY_DATABASE_URI = 'sqlite:///models/database.db'


