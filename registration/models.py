from extensions import db


class Registration(db.Model):
    __tablename__ = 'registration'
    id = db.Column(db.Integer, primary_key=True)
    admission_number = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    next_of_kin = db.Column(db.String(50), nullable=False)
    next_of_kin_number = db.Column(db.String(50), nullable=False)
    course = db.Column(db.String(50), nullable=False)
    education_level = db.Column(db.String(50), nullable=False)