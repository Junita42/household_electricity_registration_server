from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, CHAR
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship

class Household(Base):
    __tablename__ = 'household'
    
    email = Column(String(256), primary_key=True)
    household_type = Column(String(256),nullable=False)
    postal = Column(CHAR(5), ForeignKey('valid_postal.postal_code'), nullable=False)
    sqft = Column(Integer, nullable=False)
    public_utilities = Column(String(256), nullable=True)


    appliance = relationship("Appliance", back_populates="household")
    power_generator = relationship("Power_Generator", back_populates="household")
    thermal = relationship("Thermal", back_populates="household")
    valid_postal = relationship("Valid_Postal", back_populates="household")
  