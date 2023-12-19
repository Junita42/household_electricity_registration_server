from sqlalchemy import Column, Integer, String
from base_model import Base


class Manufacturer(Base):
    __tablename__ = 'Manufacturer'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    manufacturer_name = Column(String)
