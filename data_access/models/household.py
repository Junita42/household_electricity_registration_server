from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship

class Household(Base):
    __tablename__ = 'Household'
    
    email = Column(String(256), primary_key=True)
    type = Column(String(256),nullable=False)
    postal = Column(String(256), ForeignKey('Valid_Postal.postal_code'), nullable=False)
    sqft = Column(Integer, nullable=False)
    offgrid_flag = Column(Boolean, nullable=False)


    Appliance = relationship("Appliance", back_populates="Household")
    Power_Generator = relationship("Power_Generator", back_populates="Household")
    Public_Utilities = relationship("Public_Utility", back_populates="Household")
    Thermal = relationship("Thermal", back_populates="Household")
    Valid_Postal = relationship("Valid_Postal", back_populates="Household")
  