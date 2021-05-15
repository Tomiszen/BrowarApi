from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base_beer = declarative_base()


class Beer(Base_beer):
    __tablename__ = 'beer'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    style = Column(String(50), nullable=False)
    malt = Column(String(255))
    hop = Column(String(255))
    yeast = Column(String(100))
    additives = Column(String(255))
    bitterness = Column(String(5))
    extract = Column(Integer)
    alcohol = Column(Integer)
    description = Column(String(500))
    image = Column(String(255))
    cooperation = Column(String(255))

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "style": self.style,
            "ingredients": {
                "malt": self.malt,
                "hop": self.hop,
                "yeast": self.yeast,
                "additives": self.additives
            },
            "parameters": {
                "extract": self.extract,
                "alcohol": self.alcohol,
                "bitterness": self.bitterness
            },
            "description": self.description,
            "image": self.image,
            "cooperation": self.cooperation
        }


engine = create_engine('sqlite:///beers_test.db')
Base_beer.metadata.create_all(engine)
