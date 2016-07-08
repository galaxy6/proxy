#/usr/bin/env python
#_*_coding:utf-8_*_ 

from config import *
import requests
import re
import logging
    
def http_request_get(url, timeout=timeout, headers=header):
	try:
		response = requests.get(url, timeout=timeout, headers=header)
		if response.status_code == 200:
			if response.text:
				return response.text
			else:
				return response.content
		else:
			logging.info("http_request_get have a  error...")
	except Exception, e:
		logging.info("http_request_get have a except...")



#package regular expression
def regex(pattern,content):

	p = re.compile(pattern)
	result = p.findall(content)
	return result
