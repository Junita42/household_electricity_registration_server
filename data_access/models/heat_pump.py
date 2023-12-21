from sqlalchemy import Column, Integer, String, ForeignKeyConstraint, DECIMAL
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship

class Heat_Pump(Base):
    __tablename__ = 'Heat_Pump'
    
    email = Column(String(256), primary_key=True)
    air_handler_seq_num = Column(Integer, primary_key=True)
    SEER = Column(DECIMAL(10, 1), nullable=False)
    HSPF = Column(DECIMAL(10, 1), nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ['email', 'air_handler_seq_num'], 
            ['Air_Handler.email', 'Air_Handler.seq_num']
        ),
    )
  
    Air_Handler = relationship("Air_Handler", back_populates="Heat_Pump")