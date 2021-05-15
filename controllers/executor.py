from controllers import api_request
from libs import read_excel

address = 'http://localhost:5000'

source_file = ("C:/Users/Tomisz/Desktop/Test.xlsx")

source_data = read_excel.read_input(source_file)

# for beer in source_data:
#     name = beer[0]
#     style = beer[1]
#     bitterness = beer[2]
#     extract = beer[3]
#     alcohol = beer[4]
#     malt = beer[5]
#     hop = beer[6]
#     yeast = beer[7]
#     additives = beer[8]
#     description = beer[9]
#     cooperation = beer[10]
#     image = beer[11]
#
#     api_request.POSTbeer(address, name, style, malt, hop, yeast, additives, bitterness, extract, alcohol, description,
#                          image, cooperation)

api_request.GETbeers(address)
# api_request.PUTbeer(address=address, beerID='2', alcohol='1.7', extract=16)
# api_request.GETbeer(address, '1')
# api_request.DELETEbeer(address, '1')
# api_request.GETbeer(address, '2')
