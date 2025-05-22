import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATASOURCE = os.getenv("DATASOURCE")
HOST_DB = os.getenv("HOST_DB")
POSTGRES_DB = os.getenv("POSTGRES_DB")
PORT_DB = os.getenv("PORT_DB")
USERNAME_DB = os.getenv("USERNAME_DB")
PASSWORD_DB= os.getenv("PASSWORD_DB")

DATABASE_URL = DATASOURCE + USERNAME_DB + ":" + PASSWORD_DB + "@" + HOST_DB + ":" + PORT_DB + "/" + POSTGRES_DB
# Crear el motor
engine = create_engine(DATABASE_URL)

# Crear la fábrica de sesiones
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

# Base para declarar modelos ORM
Base = declarative_base()