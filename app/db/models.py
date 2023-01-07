from app.db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

# Create a User model
# Create a class for the user

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String)
    lastname = Column(String)
    address = Column(String)
    telephone = Column(Integer)
    email = Column(String, unique=True, index=True)
    creation_user = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    status = Column(Boolean, default=False)
    sales = relationship("Sales", backref="user", cascade="delete,merge")

# Create a class for sales
class Sales(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    sales = Column(Integer)
    sales_total = Column(Integer)