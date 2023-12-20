from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship

class Heat_Pump(Base):
    __tablename__ = 'Heat_Pump'
    
    email = Column(String(256), ForeignKey('Air_Handler.email'), primary_key=True)
    air_handler_seq_num = Column(Integer, ForeignKey('Air_Handler.seq_num'), primary_key=True)
    SEER = Column(DECIMAL(10, 1), nullable=False)
    HSPF = Column(DECIMAL(10, 1), nullable=False)

  
    air_handler = relationship("Air_Handler", back_populates="Heat_Pump")
