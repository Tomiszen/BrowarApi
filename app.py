from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.beerModel import Base_beer, Beer
from models.newsModel import Base_news, News

engine = create_engine('sqlite:///beers_test.db', connect_args={'check_same_thread': False})
Base_beer.metadata.bind = engine
Base_news.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# Create the appropriate app.route functions,
# test and see if they work


# Make an app.route() decorator here
@app.route("/")
@app.route("/beers", methods=['GET', 'POST'])
def beersFunction():
    if request.method == 'GET':
        # Call the method to Get all of the beers
        return getAllBeers()
    elif request.method == 'POST':
        # Call the method to make a new beer
        print("Making a New beer")

        name = request.args.get('name', '')
        style = request.args.get('style', '')
        malt = request.args.get('malt', '')
        hop = request.args.get('hop', '')
        yeast = request.args.get('yeast', '')
        additives = request.args.get('additives', '')
        extract = request.args.get('extract', None)
        alcohol = request.args.get('alcohol', None)
        bitterness = request.args.get('bitterness', '')
        description = request.args.get('description', '')
        image = request.args.get('image', '')
        cooperation = request.args.get('cooperation', '-')

        return makeANewBeer(name, style, malt, hop, yeast, additives, extract, alcohol, bitterness, description,
                            image, cooperation)


# Make another app.route() decorator here that takes in an integer id in the URI
@app.route("/beers/<int:id>", methods=['GET', 'PUT', 'DELETE'])
# Call the method to view a specific beer
def beersFunctionId(id):
    if request.method == 'GET':
        return getBeer(id)

    # Call the method to edit a specific beer
    elif request.method == 'PUT':
        name = request.args.get('name', None)
        style = request.args.get('style', None)
        malt = request.args.get('malt', None)
        hop = request.args.get('hop', None)
        yeast = request.args.get('yeast', None)
        additives = request.args.get('additives', None)
        extract = request.args.get('extract', None)
        alcohol = request.args.get('alcohol', None)
        bitterness = request.args.get('bitterness', None)
        description = request.args.get('description', None)
        image = request.args.get('image', None)
        cooperation = request.args.get('cooperation', None)
        return updateBeer(id, name, style, malt, hop, yeast, additives, extract, alcohol, bitterness, description,
                          image,
                          cooperation)

    # Call the method to remove a beer
    elif request.method == 'DELETE':
        return deleteBeer(id)


def getAllBeers():
    beers = session.query(Beer).all()
    return jsonify(Beers=[i.serialize for i in beers])


def getBeer(id):
    beer = session.query(Beer).filter_by(id=id).one()
    return jsonify(beer=beer.serialize)


def makeANewBeer(name, style, malt, hop, yeast, additives, extract, alcohol, bitterness, description,
                 image, cooperation):
    beer = Beer(name=name, style=style, malt=malt, hop=hop, yeast=yeast, additives=additives, extract=extract,
                alcohol=alcohol, bitterness=bitterness, description=description, image=image, cooperation=cooperation)
    session.add(beer)
    session.commit()
    return jsonify(Beer=beer.serialize)


def updateBeer(id, name=None, style=None, malt=None, hop=None, yeast=None, additives=None, extract=None, alcohol=None,
               bitterness=None, description=None, image=None, cooperation=None):
    beer = session.query(Beer).filter_by(id=id).one()
    if name:
        beer.name = name
    if style:
        beer.style = style
    if malt:
        beer.malt = malt
    if hop:
        beer.hop = hop
    if yeast:
        beer.yeast = yeast
    if additives:
        beer.additives = additives
    if extract:
        beer.extract = extract
    if alcohol:
        beer.alcohol = alcohol
    if bitterness:
        beer.bitterness = bitterness
    if description:
        beer.description = description
    if image:
        beer.image = image
    if cooperation:
        beer.cooperation = cooperation
    session.add(beer)
    session.commit()
    return "Updated a Beer with id %s" % id


def deleteBeer(id):
    beer = session.query(Beer).filter_by(id=id).one()
    session.delete(beer)
    session.commit()
    return "Removed Beer with id %s" % id


@app.route("/news", methods=['GET', 'POST'])
def newsFunction():
    if request.method == 'GET':
        # Call the method to Get last 5 of the news
        return getLastFiveNews()
    elif request.method == 'POST':
        # Call the method to make a new news
        print("Making a New News")

        header = request.args.get('header', '')
        description = request.args.get('description', '')
        created_date = request.args.get('created_date', '')
        event_date = request.args.get('event_date', '')
        image = request.args.get('image', '')
        link = request.args.get('link', '')
        category = request.args.get('category', '')

        return makeANewNews(header, description, created_date, event_date, image, link, category)


# Make another app.route() decorator here that takes in an integer id in the URI
@app.route("/news/<int:id>", methods=['GET', 'PUT', 'DELETE'])
# Call the method to view a specific news
def newsFunctionId(id):
    if request.method == 'GET':
        return getNews(id)

    # Call the method to edit a specific news
    elif request.method == 'PUT':
        header = request.args.get('header', None)
        description = request.args.get('description', None)
        created_date = request.args.get('created_date', None)
        event_date = request.args.get('event_date', None)
        image = request.args.get('image', None)
        link = request.args.get('link', None)
        category = request.args.get('category', None)
        return updateNews(id, header, description, created_date, event_date, image, link, category)

    # Call the method to remove a news
    elif request.method == 'DELETE':
        return deleteNews(id)


def getLastFiveNews():
    news = session.query(News).order_by(News.id.desc()).limit(5)
    return jsonify(News=[i.serialize for i in news])


def getNews(id):
    news = session.query(News).filter_by(id=id).one()
    return jsonify(News=news.serialize)


def makeANewNews(header, description, created_date, event_date, image, link, category):
    news = News(header=header, description=description, created_date=created_date, event_date=event_date,
                image=image, link=link, category=category)
    session.add(news)
    session.commit()
    return jsonify(News=news.serialize)


def updateNews(id, header=None, description=None, created_date=None, event_date=None, image=None, link=None,
               category=None):
    news = session.query(News).filter_by(id=id).one()
    if header:
        news.name = header
    if description:
        news.description = description
    if created_date:
        news.created_date = created_date
    if event_date:
        news.event_date = event_date
    if image:
        news.image = image
    if link:
        news.link = link
    if category:
        news.category = category
    session.add(news)
    session.commit()
    return "Updated a News with id %s" % id


def deleteNews(id):
    news = session.query(News).filter_by(id=id).one()
    session.delete(news)
    session.commit()
    return "Removed News with id %s" % id


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=5000)
