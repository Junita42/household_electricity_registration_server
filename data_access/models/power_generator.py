from sqlalchemy import Column, Integer, String, ForeignKey
from base_model import Base
from sqlalchemy.orm import relationship

class Power_Generator(Base):
    __tablename__ = 'Power_Generator'
    
    email = Column(String(256), ForeignKey('Household.email'), primary_key=True)
    seq_num = Column(Integer, primary_key=True)
    avg_kwatts_hr_per_month = Column(Integer, nullable=False)
    battery_storage = Column(Integer, nullable=True)
    type = Column(String, nullable=False)

    Household = relationship("Household", back_populates="Power_Generator")