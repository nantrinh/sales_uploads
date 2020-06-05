import ipdb 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# https://stackoverflow.com/questions/17652937/how-to-build-a-flask-application-around-an-already-existing-database

# format: postgresql://user:password@hostname/database_name
db_string = "postgresql://admin:password@localhost:5432/sales"

engine = create_engine(db_string, echo=True)
Base = declarative_base()
Base.metadata.reflect(engine)

class Sale(Base):
    __table__ = Base.metadata.tables['sales']

# The Session class will create new Session objects which are bound to the database
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

sales = [
    Sale(customer_name='BTS2', price='abc', quantity=0, merchant_name=68, merchant_address='MA2')
] 

session.add_all(sales)
session.commit()