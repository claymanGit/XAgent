from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
#from XAgentServer.application.core.envs import XAgentServerEnv
#SQLALCHEMY_DATABASE_URL = os.getenv('MYSQL_DB_URL', XAgentServerEnv.DB.db_url)
SQLALCHEMY_DATABASE_URL = os.getenv('MYSQL_DB_URL', "mysql+pymysql://root:xagent@172.17.0.1:3306/xagent")
SQLALCHEMY_DATABASE_URL = os.getenv('MYSQL_DB_URL', "mysql+pymysql://root:xagent@localhost:3306/xagent")


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=2, pool_timeout=3600, pool_recycle=7200
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#print(SessionLocal)
Base = declarative_base()

# if database is not exist, create it
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    pass