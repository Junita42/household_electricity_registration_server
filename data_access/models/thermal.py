from sqlalchemy import Column, Integer, String, ForeignKey
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship

class Thermal(Base):
    __tablename__ = 'thermal'
    
    email = Column(String(256), ForeignKey('household.email'),primary_key=True)
    thermal_type = Column(String(256), primary_key=True)
    setting = Column(Integer)

    household = relationship("Household", back_populates="thermal")
