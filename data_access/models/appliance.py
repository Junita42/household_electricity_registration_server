from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data_access.models.base_model import Base

class Appliance(Base):
    __tablename__ = 'Appliance'
    
    email = Column(String(256), ForeignKey('Household.email'), primary_key=True)
    seq_num = Column(Integer, primary_key=True)
    manufacturer = Column(String(256), ForeignKey("Manufacturer.manufacturer_name"), nullable=False)
    model_name = Column(String(256), nullable=True)
    BTU = Column(Integer, nullable=False)
    
    

    Household = relationship("Household", back_populates="Appliance")
    Air_Handler = relationship("Air_Handler", back_populates="Appliance")
    Water_Heater = relationship("Water_Heater", back_populates="Appliance")
    Manufacturer_Rel = relationship("Manufacturer", back_populates="Appliance")

