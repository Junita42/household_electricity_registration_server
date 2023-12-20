from sqlalchemy import Column, String, Numeric
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship

class Valid_Postal(Base):
    __tablename__ = 'Valid_Postal'
    
    postal_code = Column(String(256), primary_key=True)
    city = Column(String(256), nullable=False)
    state = Column(String(256), nullable=False)
    latitude = Column(Numeric)
    longitude = Column(Numeric)

    household = relationship("Household", back_populates="Valid_Postal")