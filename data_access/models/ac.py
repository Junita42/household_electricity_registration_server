from sqlalchemy import Column, String, Integer, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from base_model import Base

class AC(Base):
    __tablename__ = 'AC'
    
    email = Column(String(256), ForeignKey('Household.email'), primary_key=True)
    air_handler_seq_num = Column(Integer, primary_key=True)
    EER = Column(DECIMAL(10, 1), nullable=False)

    household = relationship("Household", back_populates="AC")