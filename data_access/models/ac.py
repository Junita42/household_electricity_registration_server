from sqlalchemy import Column, String, Integer, DECIMAL, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from data_access.models.base_model import Base

class AC(Base):
    __tablename__ = 'AC'
    
    email = Column(String(256), primary_key=True)
    air_handler_seq_num = Column(Integer, primary_key=True)
    EER = Column(DECIMAL(10, 1), nullable=False)

    # Composite foreign key constraint
    __table_args__ = (
        ForeignKeyConstraint(
            ['email', 'air_handler_seq_num'], 
            ['Air_Handler.email', 'Air_Handler.seq_num']
        ),
    )
    Air_Handler = relationship("Air_Handler", back_populates="AC")
