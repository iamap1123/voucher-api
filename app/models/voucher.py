from sqlalchemy import Column, String, Integer, DateTime, Boolean, Float
from datetime import datetime
from config.db import Base


class Voucher(Base):
    __tablename__ = "vouchers"
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False)
    discount_amount = Column(Integer(), nullable=False)
    discount_percentage = Column(Float(3, 2), nullable=False)
    effective_date_from = Column(DateTime(), default=datetime.now)
    effective_date_end = Column(DateTime())
    status = Column(String(), nullable=False)
    valid = Column(Boolean(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime())

    def __repr__(self):
        return "<Voucher %r>" % self.name
