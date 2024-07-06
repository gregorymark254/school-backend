from extensions import db


class Enquiry(db.Model):
    __tablename__ = 'enquiry'
    enquiry_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    course = db.Column(db.String(255), nullable=False)
    about = db.Column(db.String(255), nullable=False)
    enquiry_date = db.Column(db.DateTime, nullable=False)