from sqlalchemy import Column, String, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from data_access.models.base_model import Base

class Air_Handler(Base):
    __tablename__ = 'Air_Handler'
    
    email = Column(String(256), primary_key=True)
    seq_num = Column(Integer, primary_key=True)
    RPM = Column(Integer, nullable=False)


    # Composite foreign key constraint
    __table_args__ = (
        ForeignKeyConstraint(
            ['email', 'seq_num'], 
            ['Appliance.email', 'Appliance.seq_num']
        ),
    )

    Appliance = relationship("Appliance", back_populates="Air_Handler")
    AC = relationship("AC", back_populates="Air_Handler")
    Heater = relationship("Heater", back_populates="Air_Handler")
    Heat_Pump = relationship("Heat_Pump", back_populates="Air_Handler")

