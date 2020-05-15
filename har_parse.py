import json
from urllib.parse import urlparse
'''
format: 
method + url +querystring(optional)
httpVersion
host
useragent
headers
bodySize
cookies
\n
postData(optional;)
'''

file = open("test.har",encoding="utf8")
json_object = json.load(file)

entries = json_object['log']['entries'] # this is an array we are working with now 
# work with entry[0] for now, which is our dict

request = entries[0]['request']

response = entries[0]['response']

METHOD = request['method']
URL = urlparse(request['url']).path
QUERY_STRING_OPT = urlparse(request['url']).query
HTTP_VERSION = request['httpVersion']
HEADER_BLOCK = ''
for header in request['headers']:
	HEADER_BLOCK+=header['name']+': '+header['value']+'\n'
