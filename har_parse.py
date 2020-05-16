import json
from urlparse import urlparse

# from urllib.parse import urlparse Python3





# request object
class Request:
	
	def __init__(self, request_entry,method='',url='',query_string='',http_ver='',header_blk='',cookie_blk='',post_dat='',full_url=''):
		self.request_entry = request_entry

	#parser
	def parse_entry(self): #setter for all attributes
		self.method = self.request_entry['method']
		self.url = urlparse(self.request_entry['url']).path
		self.full_url = self.request_entry['url']
		self.query_string = urlparse(self.request_entry['url']).query
		self.http_ver = self.request_entry['httpVersion']
		self.header_blk = ''
		for header in self.request_entry['headers']:
			self.header_blk+=header['name'].capitalize()+': '+header['value']+'\n'
		self.cookie_blk = ''
		if len(self.request_entry['cookies'])>0:
			for cookie in self.request_entry['cookies'][:-1]:
				self.cookie_blk+= 'Cookie: '+cookie['name']+'='+cookie['value']+'; '
			self.cookie_blk+= self.request_entry['cookies'][-1]['name']+'='+self.request_entry['cookies'][-1]['value']+'\n'
		if self.method == 'POST':
			self.post_dat = self.request_entry['postData']['text']
		else:
			self.cookie_blk+='\n'
	

		# uncomment for debugging
		#print("%s %s%s %s\n%s%s" %(METHOD,URL,QUERY_STRING_OPT,HTTP_VERSION,HEADER_BLOCK,COOKIE_BLOCK))
		

# response object
class Response:
	
	def __init__(self,response_entry,response_http_ver='',response_stat='',response_head='',response_body=''):
		self.response_entry = response_entry

	def parse_entry(self):
		self.response_http_ver = self.response_entry['httpVersion']
		self.response_stat = str(self.response_entry['status'])+' '+self.response_entry['statusText']
		self.response_head = ''
		for header in self.response_entry['headers']:
			self.response_head+=header['name'].capitalize()+': '+header['value']+'\n'
		self.response_head+='\n'
		self.response_body = self.response_entry['content']['text'] if ('text' in self.response_entry['content'].keys()) else '' #302 and other status codes dont include a response body in .har files 
		
		# uncomment for debugging
		#print("%s %s\n%s%s" %(RESPONSE_HTTP_VERSION, STATUS_CODE,RESPONSE_HEADER_BLOCK,RESPONSE_BODY))
'''
# FOR OPENING AND PARSING THE .HAR FILE DIRECTLY FROM THIS CLASS FILE, USE THE BELOW CODE 
file = open("developer.twitter.com.har",encoding="utf8")
json_object = json.load(file)
entries = json_object['log']['entries']  #each entry contains a request/response pair
for i in range(len(entries)):
	newRequest = Request(entries[i]['request'])
	newRequest.parse_entry()
	print(newRequest.full_url)
	#newResponse = Response(entries[i]['response'])
	#newResponse.parse_entry()
	#print(newResponse.response_http_ver,newResponse.response_stat,newResponse.response_head)
'''