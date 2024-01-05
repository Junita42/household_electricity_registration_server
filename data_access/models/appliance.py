from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data_access.models.base_model import Base

class Appliance(Base):
    __tablename__ = 'appliance'
    
    email = Column(String(256), ForeignKey('household.email'), primary_key=True)
    seq_num = Column(Integer, primary_key=True)
    manufacturer = Column(String(256), ForeignKey("manufacturer.manufacturer_name"), nullable=False)
    electricity_model = Column(String(256), nullable=True)
    BTU = Column(Integer, nullable=False)
    
    

    household = relationship("Household", back_populates="appliance")
    air_handler = relationship("Air_Handler", back_populates="appliance")
    water_heater = relationship("Water_Heater", back_populates="appliance")
    manufacturer_rel = relationship("Manufacturer", back_populates="appliance")

