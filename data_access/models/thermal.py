from sqlalchemy import Column, Integer, String, ForeignKey
from base_model import Base
from sqlalchemy.orm import relationship

class Thermal(Base):
    __tablename__ = 'Thermal'
    
    email = Column(String(256), ForeignKey('Household.email'),primary_key=True)
    thermal_type = Column(String, primary_key=True)
    setting = Column(Integer)

    household = relationship("Household", back_populates="Thermal")
