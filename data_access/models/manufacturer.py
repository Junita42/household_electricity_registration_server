from sqlalchemy import Column, Integer, String
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship


class Manufacturer(Base):
    __tablename__ = 'Manufacturer'
    
    manufacturer_name = Column(String(256), primary_key=True, nullable=False)

    appliance = relationship("Appliance", back_populates="Manufacturer")
