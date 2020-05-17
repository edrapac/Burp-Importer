import json
from urlparse import urlparse

# from urllib.parse import urlparse #Python3





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
