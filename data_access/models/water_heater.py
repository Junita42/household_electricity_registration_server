from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKeyConstraint
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship


class Water_Heater(Base):
    __tablename__ = 'Water_Heater'
    
    email = Column(String(256), primary_key=True)
    seq_num = Column(Integer, primary_key=True)
    tank_size = Column(DECIMAL(10, 1), nullable=False)
    energy_source = Column(String(256), nullable=False)
    current_temp = Column(Integer, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ['email', 'seq_num'], 
            ['Appliance.email', 'Appliance.seq_num']
        ),
    )
    
    Appliance = relationship("Appliance", back_populates="Water_Heater")