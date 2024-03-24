from sqlalchemy import Column, String, Integer, ForeignKey

from database import Base


class User(Base):
    __tablename__ = 'users'


    id = Column(Integer, primary_key=True)
    login = Column(String, index=True)
    password = Column(String, index=True)
