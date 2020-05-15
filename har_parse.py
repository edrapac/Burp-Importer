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
class Request:
	"""docstring for ClassName"""
	def __init__(self, request_entry,method='',url='',query_string='',http_ver='',header_blk='',cookie_blk='',post_dat=''):
		self.request_entry = request_entry
	def parse_entry(self):
		METHOD = self.request_entry['method']
		URL = urlparse(self.request_entry['url']).path
		QUERY_STRING_OPT = urlparse(self.request_entry['url']).query
		HTTP_VERSION = self.request_entry['httpVersion']
		HEADER_BLOCK = ''
		for header in self.request_entry['headers']:
			HEADER_BLOCK+=header['name'].capitalize()+': '+header['value']+'\n'
		COOKIE_BLOCK = ''
		if len(self.request_entry['cookies'])>0:
			for cookie in self.request_entry['cookies'][:-1]:
				COOKIE_BLOCK+= 'Cookie: '+cookie['name']+'='+cookie['value']+'; '
			COOKIE_BLOCK+= self.request_entry['cookies'][-1]['name']+'='+self.request_entry['cookies'][-1]['value']+'\n'

		if METHOD == 'POST':
			POST_DATA = self.request_entry['postData']['text']
		else:
			COOKIE_BLOCK+='\n'
		
		#for debugging
		print("%s %s%s %s\n%s%s" %(METHOD,URL,QUERY_STRING_OPT,HTTP_VERSION,HEADER_BLOCK,COOKIE_BLOCK))
		

# response object
class Response:
	
	def __init__(self,response_entry,response_http_ver='',response_stat='',response_head='',response_body=''):
		self.response_entry = response_entry

	def parse_entry(self):
		RESPONSE_HTTP_VERSION = self.response_entry['httpVersion']
		STATUS_CODE = str(self.response_entry['status'])+' '+self.response_entry['statusText']
		RESPONSE_HEADER_BLOCK = ''
		for header in self.response_entry['headers']:
			RESPONSE_HEADER_BLOCK+=header['name'].capitalize()+': '+header['value']+'\n'
		RESPONSE_HEADER_BLOCK+='\n'
		RESPONSE_BODY = self.response_entry['content']['text'] if ('text' in self.response_entry['content'].keys()) else '' #302 and other status codes dont include a body for response 
		
		#for debugging
		print("%s %s\n%s%s" %(RESPONSE_HTTP_VERSION, STATUS_CODE,RESPONSE_HEADER_BLOCK,RESPONSE_BODY))
		
for i in range(len(entries)):
	newRequest = Request(entries[i]['request'])
	newRequest.parse_entry()
	newResponse = Response(entries[i]['response'])
	newResponse.parse_entry()

file.close()