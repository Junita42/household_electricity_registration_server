from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base_model import Base

class Air_Handler(Base):
    __tablename__ = 'Air_Handler'
    
    email = Column(String(256), ForeignKey('Household.email'), primary_key=True)
    seq_num = Column(Integer, primary_key=True)
    RPM = Column(Integer, nullable=False)
    

    household = relationship("Household", back_populates="Air_Handler")
