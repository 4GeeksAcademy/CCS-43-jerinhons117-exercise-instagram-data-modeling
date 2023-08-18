import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follorews(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Follorews_id = Column(ForeignKey("user.id"))
    Follorews = relationship( "user")
    user_id = Column(ForeignKey("user.id"))
    user = relationship( "user")


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('followers'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id = relationship( "post")
    post = relationship("Post")

    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Comment_tex = Column(String(250), nullable=False)
    post_code = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    

    def to_dict(self):
        return {}
    
class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_code = Column(String(250), nullable=False)
    post_id = Column(ForeignKey("media.id"))
    post = relationship( "Media", back_populates="media")
    user_id = Column(ForeignKey("user.id"))

    def to_dict(self):
        return {}

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    # person_id = Column(Integer, ForeignKey('person.id'))

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
