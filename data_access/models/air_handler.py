from sqlalchemy import Column, String, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from data_access.models.base_model import Base

class Air_Handler(Base):
    __tablename__ = 'air_handler'
    
    email = Column(String(256), primary_key=True)
    seq_num = Column(Integer, primary_key=True)
    RPM = Column(Integer, nullable=False)


    # Composite foreign key constraint
    __table_args__ = (
        ForeignKeyConstraint(
            ['email', 'seq_num'], 
            ['appliance.email', 'appliance.seq_num']
        ),
    )

    appliance = relationship("Appliance", back_populates="air_handler")
    ac = relationship("AC", back_populates="air_handler")
    heater = relationship("Heater", back_populates="air_handler")
    heat_pump = relationship("Heat_Pump", back_populates="air_handler")

