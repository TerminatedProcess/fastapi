from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings as s

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:pass123@localhost:5432/fastapi'
SQLALCHEMY_DATABASE_URL = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(s.database_username, 
                                                                    s.database_password, 
                                                                    s.database_hostname, 
                                                                    s.database_port, 
                                                                    s.database_name)
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='pass123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database Connection was Successful!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
