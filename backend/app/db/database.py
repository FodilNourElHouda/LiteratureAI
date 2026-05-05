from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(url=DATABASE_URL,
                       connect_args={"check_same_thread": False}
                       )
Session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()
