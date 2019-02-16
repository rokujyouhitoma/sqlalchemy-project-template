import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DATABASE_URI)

Base = declarative_base()

DBSession = sessionmaker(bind=engine)
