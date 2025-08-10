from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import setting


# Database connection setup
SQLALCHEMY_DATABASE_URL = f'postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Connection Pool: DB ke 5 open pipelines — reuse hoti hain

# Session: Ek temporary jagah to do DB work

# get_db(): Har request ko ek session milta hai jo ek connection use karta hai, aur kaam khatam hone ke baad close hota hai


# Manual Connection to PostgreSQL using psycopg

# while True:
#     try:
#         conn = psycopg.connect(host='localhost', dbname='fastapi', user='postgres', password='123')
#         cursor = conn.cursor()
#         print("Database connection successfull!")
#         break
#     except Exception as e:
#         print("Connecting to DB failed!")
#         print("Error: ", e)
#         time.sleep(2)

# # Hardcoded posts array
# my_posts = [{"title": "Post 1", "content": "Content of post 1", "id": 1},
#             {"title" : "Post 2", "content" : "Content of post 2", "id": 2}]
