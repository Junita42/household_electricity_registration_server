from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from base_model import Base
from sqlalchemy.orm import relationship


class Water_Heater(Base):
    __tablename__ = 'Water_Heater'
    
    email = Column(String(256), ForeignKey('Household.email'), primary_key=True)
    seq_num = Column(Integer, primary_key=True)
    tank_size = Column(DECIMAL(10, 1), nullable=False)
    energy_source = Column(String, nullable=False)
    current_temp = Column(Integer, nullable=False)
    
    household = relationship("Household", back_populates="Water_Heater")