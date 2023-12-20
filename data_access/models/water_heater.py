from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship


class Water_Heater(Base):
    __tablename__ = 'Water_Heater'
    
    email = Column(String(256), ForeignKey('Appliance.email'), primary_key=True)
    seq_num = Column(Integer, ForeignKey('Appliance.seq_number'),primary_key=True)
    tank_size = Column(DECIMAL(10, 1), nullable=False)
    energy_source = Column(String(256), nullable=False)
    current_temp = Column(Integer, nullable=False)
    
    appliance = relationship("Appliance", back_populates="Water_Heater")