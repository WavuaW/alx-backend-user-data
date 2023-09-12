#!/usr/bin/env python3
'''User Model
'''
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    '''A user class that implements user functionalities
    '''
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    email = Column('email', String(250), nullable=False)
    hashed_password = Column('hashed_password', String(250), nullable=False)
    session_id = Column('session_id', String(250), nullable=False)
    reset_token = Column('reset_token', String(250), nullable=False)

    def __init___(self, id, email, hashed_password, session_id, reset_token):
        '''Initializing the colums
        '''
        self.id = id
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token
