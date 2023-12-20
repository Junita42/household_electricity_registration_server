from sqlalchemy import Column, String, DECIMAL
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship

class Valid_Postal(Base):
    __tablename__ = 'Valid_Postal'
    
    postal_code = Column(String(256), primary_key=True)
    city = Column(String(256), nullable=False)
    state = Column(String(256), nullable=False)
    latitude = Column(DECIMAL(9,6))
    longitude = Column(DECIMAL(9,6))

    Household = relationship("Household", back_populates="Valid_Postal")