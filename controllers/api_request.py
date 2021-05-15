import sys

import requests


# POST
def POSTbeer(address, name, style, malt, hop, yeast, additives, bitterness, extract, alcohol, description, image,
             cooperation):
    values = {
        'name': name,
        'style': style,
        'malt': malt,
        'hop': hop,
        'yeast': yeast,
        'additives': additives,
        'extract': extract,
        'alcohol': alcohol,
        'bitterness': bitterness,
        'description': description,
        'image': image,
        'cooperation': cooperation
    }

    try:
        r = requests.post(address + '/beers', params=values)
        if r.status_code != 200:
            raise Exception('Received an unsuccessful status code of %s' % r.status_code)

    except Exception as err:
        print("POST FAILED")
        print(err.args)
        sys.exit()

    else:
        print("POST PASS")


# PUT
def PUTbeer(address, beerID, name=None, style=None, malt=None, hop=None, yeast=None, additives=None, bitterness=None,
            extract=None,
            alcohol=None, description=None, image=None, cooperation=None):
    values = {
        'id': beerID,
        'name': name,
        'style': style,
        'malt': malt,
        'hop': hop,
        'yeast': yeast,
        'additives': additives,
        'extract': extract,
        'alcohol': alcohol,
        'bitterness': bitterness,
        'description': description,
        'image': image,
        'cooperation': cooperation
    }

    try:
        r = requests.put(address + "/beers/" + beerID, params=values)
        print(r.url)
        if r.status_code != 200:
            raise Exception('Received an unsuccessful status code of %s' % r.status_code)

    except Exception as err:
        print("PUT FAILED")
        print(err.args)
        sys.exit()

    else:
        print("PUT PASS")


# GET /beers
def GETbeers(address):
    try:
        r = requests.get(address + "/beers")
        print(r.json())
        obj = r.json()
        print(obj['Beers'][1]['name'])
        if r.status_code != 200:
            raise Exception('Received an unsuccessful status code of %s' % r.status_code)

    except Exception as err:
        print("GET FAILED")
        print(err.args)
        sys.exit()

    else:
        print("GET PASS")


# GET /beers/id
def GETbeer(address, beerID):
    try:
        r = requests.get(address + "/beers/" + beerID)
        # print(r.json())
        obj = r.json()
        print(obj['beer']['name'])
        if r.status_code != 200:
            raise Exception('Received an unsuccessful status code of %s' % r.status_code)

    except Exception as err:
        print("GET FAILED")
        print(err.args)
        sys.exit()

    else:
        print("GET PASS")


# DELETE /beers/id
def DELETEbeer(address, beerID):
    try:
        r = requests.delete(address + "/beers/" + beerID)
        print(r.url)
        if r.status_code != 200:
            raise Exception('Received an unsuccessful status code of %s' % r.status_code)

    except Exception as err:
        print("DELETE FAILED")
        print(err.args)
        sys.exit()

    else:
        print("DELETE PASS")


# POST
def POSTnews(address, header, description, created_date, event_date, image, link, category):
    values = {
        'header': header,
        'description': description,
        'created_date': created_date,
        'event_date': event_date,
        'link': link,
        'image': image,
        'category': category
    }

    try:
        r = requests.post(address + '/news', params=values)
        if r.status_code != 200:
            raise Exception('Received an unsuccessful status code of %s' % r.status_code)

    except Exception as err:
        print("POST FAILED")
        print(err.args)
        sys.exit()

    else:
        print("POST PASS")


# PUT
def PUTnews(address, newsID, header=None, description=None, created_date=None, event_date=None, image=None, link=None,
            category=None):
    values = {
        'header': header,
        'description': description,
        'created_date': created_date,
        'event_date': event_date,
        'link': link,
        'image': image,
        'category': category
    }

    try:
        r = requests.put(address + "/news/" + newsID, params=values)
        print(r.url)
        if r.status_code != 200:
            raise Exception('Received an unsuccessful status code of %s' % r.status_code)

    except Exception as err:
        print("PUT FAILED")
        print(err.args)
        sys.exit()

    else:
        print("PUT PASS")


# GET /news
def GETnews(address):
    try:
        r = requests.get(address + "/news")
        print(r.json())
        obj = r.json()
        print(obj['News'][0]["header"])
        print(obj['News'][4]["header"])
        if r.status_code != 200:
            raise Exception('Received an unsuccessful status code of %s' % r.status_code)

    except Exception as err:
        print("GET FAILED")
        print(err.args)
        sys.exit()

    else:
        print("GET PASS")


# GET /news/id
def GETnewsOne(address, newsID):
    try:
        r = requests.get(address + "/news/" + newsID)
        # print(r.json())
        obj = r.json()
        print(obj['News']['header'])
        print(obj['News']['category'])
        if r.status_code != 200:
            raise Exception('Received an unsuccessful status code of %s' % r.status_code)

    except Exception as err:
        print("GET FAILED")
        print(err.args)
        sys.exit()

    else:
        print("GET PASS")


# DELETE /news/id
def DELETEnews(address, newsID):
    try:
        r = requests.delete(address + "/news/" + newsID)
        print(r.url)
        if r.status_code != 200:
            raise Exception('Received an unsuccessful status code of %s' % r.status_code)

    except Exception as err:
        print("DELETE FAILED")
        print(err.args)
        sys.exit()

    else:
        print("DELETE PASS")
