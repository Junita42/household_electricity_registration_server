from sqlalchemy import Column, String, Integer, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from data_access.models.base_model import Base

class AC(Base):
    __tablename__ = 'AC'
    
    email = Column(String(256), ForeignKey('Air_Handler.email'), primary_key=True)
    air_handler_seq_num = Column(Integer, ForeignKey('Air_Handler.seq_num'), primary_key=True)
    EER = Column(DECIMAL(10, 1), nullable=False)

    air_handler = relationship("Air_Handler", back_populates="AC")
