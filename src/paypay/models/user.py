from sqlalchemy import Column, BigInteger, String

from paypay.infra.database import Base  # type: ignore



class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    token = Column(String, index=True)
