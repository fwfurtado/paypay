from typing import Optional
from sqlalchemy import Boolean, Column, ForeignKey, BigInteger, String
from sqlalchemy.orm import relationship

from src.paypay.repositories.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    token = Column(String, index=True)
