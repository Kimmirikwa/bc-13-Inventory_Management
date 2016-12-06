from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("test.db",convert_unicode = True )
db_session = scoped_session(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    #importing all the modules that might define modules so as they
    #will be registered properly on the matadata