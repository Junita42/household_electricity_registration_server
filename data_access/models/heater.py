from sqlalchemy import Column, Integer, String, ForeignKeyConstraint
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship

class Heater(Base):
    __tablename__ = 'Heater'
    
    email = Column(String(256), primary_key=True)
    air_handler_seq_num = Column(Integer, primary_key=True)
    energy_source = Column(String(256), nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ['email', 'air_handler_seq_num'], 
            ['Air_Handler.email', 'Air_Handler.seq_num']
        ),
    )
    Air_Handler = relationship("Air_Handler", back_populates="Heater")
