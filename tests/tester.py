import sys

import httplib2

print("Running Endpoint Tester....\n")
address = ''
if address == '':
    address = 'http://localhost:5000'

###Making a POST Request
##print ("Making a POST request to /beers...")
##try:
##	url = address + "/beers?name=Rauchdoppelbock&description=Kooperacja+z+Browarem+Trzech+Kumpli&style=Wędzony+Podwójny+Koźlak&malt=slod+jeczmienny&hop=Iunga"
##	h = httplib2.Http()
##	resp, result = h.request(url, 'POST')
##	obj = json.loads(result)
##	beerID = obj['Beer']['id']
##	if resp['status'] != '200':
##		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
##
##except Exception as err:
##	print ("Test 1 FAILED: Could not make POST Request to web server")
##	print (err.args)
##	sys.exit()
##else:
##	print ("Test 1 PASS: Succesfully Made POST Request to /puppies")


# Making a GET Request
print("Making a GET Request for /beers...")
try:
    url = address + "/beers"
    h = httplib2.Http()
    resp, result = h.request(url, 'GET')
    print(result.decode('utf-8'))
    if resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
    print("Test 2 FAILED: Could not make GET Request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 2 PASS: Succesfully Made GET Request to /puppies")

# Making GET Requests to /puppies/id
print("Making GET requests to /beers/id ")

try:
    id = beerID
    url = address + "/beers/%s" % id
    h = httplib2.Http()
    resp, result = h.request(url, 'GET')
    if resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])


except Exception as err:
    print("Test 3 FAILED: Could not make GET Requests to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 3 PASS: Succesfully Made GET Request to /puppies/id")

# Making a PUT Request
print("Making PUT requests to /puppies/id ")

try:
    id = puppyID

    url = address + "/puppies/%s?name=wilma&description=A+sleepy+bundle+of+joy" % id
    h = httplib2.Http()
    resp, result = h.request(url, 'PUT')
    if resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
    print("Test 4 FAILED: Could not make PUT Request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 4 PASS: Succesfully Made PUT Request to /puppies/id")

# Making a DELETE Request

print("Making DELETE requests to /puppies/id ... ")

try:
    id = puppyID
    url = address + "/puppies/%s" % id
    h = httplib2.Http()
    resp, result = h.request(url, 'DELETE')
    if resp['status'] != '200':
        raise Exception('Received an unsuccessful status code of %s' % resp['status'])


except Exception as err:
    print("Test 5 FAILED: Could not make DELETE Requests to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 5 PASS: Succesfully Made DELETE Request to /puppies/id")
    print("ALL TESTS PASSED!!")
