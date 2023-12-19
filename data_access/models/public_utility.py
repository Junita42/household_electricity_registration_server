from sqlalchemy import Column, String, ForeignKey
from base_model import Base
from sqlalchemy.orm import relationship


class Public_Utility(Base):
    __tablename__ = 'Public_Utilities'
    
    email = Column(String(256), ForeignKey('Household.email'), primary_key=True)
    utilities_type = Column(String(250), nullable=False)

    household = relationship("Household", back_populates="Public_Utilities")