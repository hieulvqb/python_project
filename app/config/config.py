import os
basedir = os.path.abspath(os.path.dirname(__file__))

def get_database_uri():
    connection = os.environ.get("DB_CONNECTION")
    protocols = {
        "sqlite": "sqlite://",
        "mysql": "mysql://",
        "mariadb": "mysql+pymsql://"
    }
    db_protocol = protocols.get(connection, None)
    if not db_protocol:
        raise Exception("Database Connection not support")
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', '3306')
    db_database = os.environ.get('DB_DATABASE', '')
    db_username = os.environ.get('DB_USERNAME', 'root')
    db_password = os.environ.get('DB_PASSWORD', '')
    return db_protocol+db_username+':'+db_password+'@'+db_host+':'+db_port+'/'+db_database+'?charset=utf8mb4'


class Config(object):
    # connect database
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get("SECRET_KEY") or 'you-will-never-guess'

    # cấu hình mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
