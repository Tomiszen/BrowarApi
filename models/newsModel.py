from sqlalchemy import Column, Integer, String, SmallInteger
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base_news = declarative_base()


class News(Base_news):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    header = Column(String(100), nullable=False)
    description = Column(String(500))
    created_date = Column(String(26))
    event_date = Column(String(26))
    image = Column(String(255))
    link = Column(String(255))
    category = Column(SmallInteger)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "header": self.header,
            "description": self.description,
            "created_date": self.created_date,
            "event_date": self.event_date,
            "image": self.image,
            "link": self.link,
            "category": self.category
        }


engine = create_engine('sqlite:///beers_test.db')
Base_news.metadata.create_all(engine)
