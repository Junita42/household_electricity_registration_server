from sqlalchemy import Column, Integer, String, ForeignKey
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship

class Power_Generator(Base):
    __tablename__ = 'Power_Generator'
    
    seq_num = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(256), ForeignKey('Household.email'), primary_key=True)
    kilowatt_hours = Column(Integer, nullable=False)
    battery_storage = Column(Integer, nullable=True)
    energy_source = Column(String(256), nullable=False)

    Household = relationship("Household", back_populates="Power_Generator")