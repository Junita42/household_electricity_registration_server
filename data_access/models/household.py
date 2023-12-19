from sqlalchemy import Column, Integer, String, Boolean
from base_model import Base
from sqlalchemy.orm import relationship

class Household(Base):
    __tablename__ = 'Household'
    
    email = Column(String(256), primary_key=True)
    type = Column(String,nullable=False)
    postal = Column(String, nullable=False)
    sqft = Column(Integer, nullable=False)
    offgrid_flag = Column(Boolean, nullable=False)

    AC = relationship("AC", back_populates="Household")
    Air_Handler = relationship("Air_Handler", back_populates="Household")
    Appliance = relationship("Appliance", back_populates="Household")
    Heat_Pump = relationship("Heat_Pump", back_populates="Household")
    Heater = relationship("Heater", back_populates="Household")
    Power_Generator = relationship("Power_Generator", back_populates="Household")
    Public_Utilities = relationship("Public_Utility", back_populates="Household")
    Thermal = relationship("Thermal", back_populates="Household")
    Water_Heater = relationship("Water_Heater", back_populates="Household")
  