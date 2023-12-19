from sqlalchemy import Column, String, Numeric
from base_model import Base


class Valid_Postal(Base):
    __tablename__ = 'Valid_Postal'
    
    postal_code = Column(String, primary_key=True)
    city = Column(String)
    state = Column(String)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
