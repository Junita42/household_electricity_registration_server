from sqlalchemy import Column, Integer, String, ForeignKeyConstraint
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship

class Heater(Base):
    __tablename__ = 'heater'
    
    email = Column(String(256), primary_key=True)
    air_handler_seq_num = Column(Integer, primary_key=True)
    energy_source = Column(String(256), nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ['email', 'air_handler_seq_num'], 
            ['air_handler.email', 'air_handler.seq_num']
        ),
    )
    air_handler = relationship("Air_Handler", back_populates="heater")
