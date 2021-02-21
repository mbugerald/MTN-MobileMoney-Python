from app import db, ma
from sqlalchemy import func
from datetime import datetime


# Momo payment request
class MomoPaymentRequest(db.Model):
    __tablename__ = "momo_payment_request"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    transaction_id = db.Column(db.VARCHAR(60), nullable=False)
    amount = db.Column(db.Float, default=0)
    currency = db.Column(db.CHAR(4), nullable=False)
    payer_party_id = db.Column(db.VARCHAR(30), nullable=False)  # Payment method used by the individual
    payer_party = db.Column(db.VARCHAR(30), nullable=False)     # Phone number or credential of the individual
    status = db.Column(db.CHAR(10), nullable=False)     # Status of payment approval transaction end party
    product_id = db.Column(db.VARCHAR(100), nullable=False)     # Expected product id
    date_added = db.Column(db.DateTime(timezone=True), server_default=func.now())
    date_modified = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=datetime.now)

    def __int__(self, transaction_id: str):
        self.transaction_id = transaction_id


class MomoPaymentRequestSchema(ma.Schema):
    class Meta:
        fields = []