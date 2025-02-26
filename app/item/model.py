from sqlalchemy import Column, Integer, String, Sequence
from app.db import Base

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
