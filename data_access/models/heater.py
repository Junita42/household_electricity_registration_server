from sqlalchemy import Column, Integer, String, ForeignKey
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship

class Heater(Base):
    __tablename__ = 'Heater'
    
    email = Column(String(256), ForeignKey('Air_Handler.email'), primary_key=True)
    air_handler_seq_num = Column(Integer, ForeignKey('Air_Handler.seq_number'), primary_key=True)
    energy_source = Column(String(256), nullable=False)

    air_handler = relationship("Air_Handler", back_populates="Heater")
