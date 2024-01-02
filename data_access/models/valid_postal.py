from sqlalchemy import Column, String, DECIMAL, CHAR, create_engine
from data_access.models.base_model import Base
from sqlalchemy.orm import relationship, sessionmaker

class Valid_Postal(Base):
    __tablename__ = 'valid_postal'
    
    postal_code = Column(CHAR(5), primary_key=True)
    city = Column(String(256), nullable=False)
    state = Column(String(256), nullable=False)
    latitude = Column(DECIMAL(10,7), nullable=False)
    longitude = Column(DECIMAL(10,7), nullable=False)

    household = relationship("Household", back_populates="valid_postal")


