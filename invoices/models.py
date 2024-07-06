from extensions import db


class Invoice(db.Model):
    __tablename__ = 'invoice'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    invoice_number = db.Column(db.String(255), unique=True, nullable=False)
    admission_number = db.Column(db.String(255), unique=True, nullable=False)
    tution_fee = db.Column(db.Float, nullable=False)
    registration_fee = db.Column(db.Float, nullable=False)
    library_fee = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    registration_id = db.Column(db.Integer, db.ForeignKey('registration.id'), nullable=False)
