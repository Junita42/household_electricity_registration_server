from sqlalchemy import Column, Integer, String, ForeignKey
from base_model import Base
from sqlalchemy.orm import relationship

class Heater(Base):
    __tablename__ = 'Heater'
    
    email = Column(String(256), ForeignKey('Household.email'), primary_key=True)
    air_handler_seq_num = Column(Integer, primary_key=True)
    energy_source = Column(String, nullable=False)

    household = relationship("Household", back_populates="Heater")
