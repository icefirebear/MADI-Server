from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.core.config import settings

DATABASE = settings.SQLALCHEMY_DATABASE_URI

ENGINE = create_engine(DATABASE, encoding="utf-8", echo=False)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
