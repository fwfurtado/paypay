from src.paypay.infra.settings import GLOBAL_CONFIG

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = GLOBAL_CONFIG.database_settings.dsn

engine = create_engine(
    DATABASE_URL,
    echo=True,
    echo_pool='debug'
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()