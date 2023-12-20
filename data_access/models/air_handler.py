from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from data_access.models.base_model import Base

class Air_Handler(Base):
    __tablename__ = 'Air_Handler'
    
    email = Column(String(256), ForeignKey('Appliance.email'), primary_key=True)
    seq_num = Column(Integer, ForeignKey('Appliance.seq_num'), primary_key=True)
    RPM = Column(Integer, nullable=False)

    appliance = relationship("Appliance", back_populates="Air_Handler")
    AC = relationship("AC", back_populates="air_handler")
    Heater = relationship("Heater", back_populates="air_handler")
    Heat_Pump = relationship("Heat_Pump", back_populates="air_handler")
    
