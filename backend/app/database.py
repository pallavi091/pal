# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# # DATABASE_URL = "sqlite:///./hrms.db"
# DATABASE_URL = "postgresql+psycopg2://postgres:Pallavi@localhost:5432/hrms"

# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal = sessionmaker(bind=engine)

# Base = declarative_base()



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:Pallavi@localhost:5432/hrms"

engine = create_engine(DATABASE_URL)  # ✅ NO connect_args

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

