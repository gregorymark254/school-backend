from extensions import db


class Receipt(db.Model):
    __tablename__ = 'receipts'
    id = db.Column(db.Integer, primary_key=True)
    receipt_number = db.Column(db.String(255))
    receipt_date = db.Column(db.Date)
    amount_paid = db.Column(db.Integer)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id'))