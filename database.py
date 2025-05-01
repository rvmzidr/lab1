from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Remplacer USERNAME et PASSWD par ton utilisateur et mot de passe PostgreSQL
URL_DATABASE = 'postgresql://postgres:123456@localhost:5432/quizApp'


engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
