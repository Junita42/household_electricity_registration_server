from sqlalchemy import Column, Integer, String, ForeignKey
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship

class Power_Generator(Base):
    __tablename__ = 'power_generator'
    
    email = Column(String(256), ForeignKey('household.email'), primary_key=True)
    seq_num = Column(Integer, primary_key=True)
    kilowatt_hours = Column(Integer, nullable=False)
    battery_storage = Column(Integer, nullable=True)
    energy_source = Column(String(256), nullable=False)

    household = relationship("Household", back_populates="power_generator")