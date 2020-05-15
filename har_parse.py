import json
from urllib.parse import urlparse
'''
TODO
There are some redundant constant declarations such as HEADER_BLOCK and RESPONSE_HEADER_BLOCK
we need to decide if we want to keep those or just use one dynamic var for both
'''

file = open("har_full.har",encoding="utf8")
json_object = json.load(file)

entries = json_object['log']['entries']  #each entry contains a request/response pair

#request = entries[29]['request'] 
#response = entries[29]['response']

'''
TODO: encapsulate the below into methods
'''
# request object
def parse_entry(request,response):
	METHOD = request['method']
	URL = urlparse(request['url']).path
	QUERY_STRING_OPT = urlparse(request['url']).query
	HTTP_VERSION = request['httpVersion']
	HEADER_BLOCK = ''
	for header in request['headers']:
		HEADER_BLOCK+=header['name'].capitalize()+': '+header['value']+'\n'
	COOKIE_BLOCK = ''
	if len(request['cookies'])>0:
		for cookie in request['cookies'][:-1]:
			COOKIE_BLOCK+= 'Cookie: '+cookie['name']+'='+cookie['value']+'; '
		COOKIE_BLOCK+= request['cookies'][-1]['name']+'='+request['cookies'][-1]['value']+'\n'

	if METHOD == 'POST':
		POST_DATA = request['postData']['text']
	else:
		COOKIE_BLOCK+='\n'

	# response object
	RESPONSE_HTTP_VERSION = response['httpVersion']
	STATUS_CODE = str(response['status'])+' '+response['statusText']
	RESPONSE_HEADER_BLOCK = ''
	for header in response['headers']:
		RESPONSE_HEADER_BLOCK+=header['name'].capitalize()+': '+header['value']+'\n'
	RESPONSE_HEADER_BLOCK+='\n'
	RESPONSE_BODY = response['content']['text'] if ('text' in response['content'].keys()) else '' #302 and other status codes dont include a body for response 
	'''
	comment this out or remove, for tesing purposes only
	'''
	# print request
	print("%s %s%s %s\n%s%s" %(METHOD,URL,QUERY_STRING_OPT,HTTP_VERSION,HEADER_BLOCK,COOKIE_BLOCK))

	#print response 
	print("%s %s\n%s%s" %(RESPONSE_HTTP_VERSION, STATUS_CODE,RESPONSE_HEADER_BLOCK,RESPONSE_BODY))
for i in range(len(entries)):
	request = entries[i]['request'] 
	response = entries[i]['response']
	parse_entry(request,response)
file.close()