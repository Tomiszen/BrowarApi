from controllers import api_request

address = 'http://localhost:5000'

# api_request.POSTnews(address, "Test01", "Opis01", datetime.datetime.now(), datetime.datetime.now(), '', '', 2)
# api_request.POSTnews(address, "Test02", "Opis02", datetime.datetime.now(), datetime.datetime.now(), '', '', 2)
# api_request.POSTnews(address, "Test03", "Opis03", datetime.datetime.now(), datetime.datetime.now(), '', '', 2)
# api_request.POSTnews(address, "Test04", "Opis04", datetime.datetime.now(), datetime.datetime.now(), '', '', 2)
# api_request.POSTnews(address, "Test05", "Opis05", datetime.datetime.now(), datetime.datetime.now(), '', '', 2)
# api_request.POSTnews(address, "Test06", "Opis06", datetime.datetime.now(), datetime.datetime.now(), '', '', 2)
# api_request.POSTnews(address, "Test07", "Opis07", datetime.datetime.now(), datetime.datetime.now(), '', '', 2)
# api_request.POSTnews(address, "Test08", "Opis08", datetime.datetime.now(), datetime.datetime.now(), '', '', 2)
# api_request.POSTnews(address, "Test09", "Opis09", datetime.datetime.now(), datetime.datetime.now(), '', '', 2)
# api_request.POSTnews(address, "Test10", "Opis10", datetime.datetime.now(), datetime.datetime.now(), '', '', 2)

# api_request.GETnews(address)
# api_request.DELETEnews(address, '9')
# api_request.PUTnews(address, newsID='8', category=1)
api_request.GETnewsOne(address, newsID='8')

# api_request.GETbeers(address)
# api_request.PUTbeer(address=address, beerID='2', alcohol='1.7', extract=16)
# api_request.GETbeer(address, '1')
# api_request.DELETEbeer(address, '1')
# api_request.GETbeer(address, '2')
