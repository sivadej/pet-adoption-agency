from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models/schema
# Remember to db.create_all() if tables do not yet exist
class Demo(db.Model):
    __tablename__ = 'demos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_required_unique_string = db.Column(db.String(50), nullable=False, unique=True)
    an_optional_number = db.Column(db.Integer, nullable=True)
    a_required_default_ten = db.Column(db.Integer, nullable=False, default=10)