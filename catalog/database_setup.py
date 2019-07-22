"""Database setup for the Item Catalog project.

This script should be run first before running the main application.py,
though application.py will run this script if no database file it found.
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Get the base class mapper from SQLalchemy
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    picture = Column(String(256))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    items = relationship('Item', cascade="save-update, merge, delete")

    @property
    def serialise(self):
        # Returns category data in an easily serialiseable format.
        return {
            'id' : self.id,
            'name' : self.name,
            'Item' : [i.serialise for i in self.items]
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String)        
    image_url = Column(String(250))

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialise(self):
        """Returns item data in an easily serialiseable format."""
        return {
            'id' : self.id,
            'cat_id' : self.category_id,
            'name' : self.name,
            'description' : self.description            
        }


def create_db(database_url):
    """Create an empty database with the tables defined above."""
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    print "Database file created..."
