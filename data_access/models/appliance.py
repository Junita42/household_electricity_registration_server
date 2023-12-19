from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base_model import Base

class Appliance(Base):
    __tablename__ = 'Appliance'
    
    email = Column(String(256), ForeignKey('Household.email'), primary_key=True)
    manufacturer = Column(String, nullable=False)
    model_name = Column(String, nullable=True)
    BTU = Column(Integer, nullable=False)
    seq_num = Column(Integer, primary_key=True)

    household = relationship("Household", back_populates="Appliance")
