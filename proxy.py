#/usr/bin/env python
#_*_coding:utf-8_*_ 

import re
import time
import random
import urllib2
import socket
import httplib
import logging
from lib.common import http_request_get
from lib.common import regex

def proxy_youdaili():
	res = []
	ip_list =[]
	result = []

	while not result:
		url = 'http://www.youdaili.net/Daili/http/'
		rep = http_request_get(url)
		result = regex(r'http://www\.youdaili\.net/Daili/http/\d+\.html',rep)

	for _ in xrange(2):
		urls = '%s' % result[_]
		time.sleep(2)
		response = http_request_get(urls)
		ip_list = regex(r'\d+\.\d+\.\d+\.\d+:\d+',response)
		res.extend(ip_list)
	logging.info('proxy_youdaili worked !')
	return res

def proxy_xicidaili():
	ip_list =[]
	res = []

	for page in (1,2):
		time.sleep(2)
		url = 'http://www.xicidaili.com/nn/%s' % page
		content = http_request_get(url)
		result = regex(r'(\d+\.\d+\.\d+\.\d+)</td>\s+<td>(\d+)',content)
		for _ in result:
			ip_port = '%s:%s' % ( _[0],_[1])
			ip_list.append(ip_port)
		res.extend(ip_list)
	logging.info('proxy_xicidaili worked !')
	return res


def write_file(ip_port):
	today = time.localtime()
	month = '0%s'%today.tm_mon if today.tm_mon <10 else today.tm_mon
	day = '0%s'%today.tm_mday if today.tm_mday <10 else  today.tm_mday

	path = "./iplist/ip%s%s" % (month,day)
	output = open(path,'a+')
	output.write(ip_port)
	output.write("\n")
	output.close()

def proxy_test():
	ip_list = []
	repeat_ip = []
	youdaili_ip = []
	xicidaili_ip = []
	old_ip = []
	youdaili_ip = proxy_youdaili()
	xicidaili_ip = proxy_xicidaili()
	ip_list.extend(youdaili_ip)
	ip_list.extend(xicidaili_ip)	
	for _ in ip_list:
		if _ not in repeat_ip:
			repeat_ip.append(_)
			proxy_ip = _.split(':')
			
			proxy_info ="{'host':'%s','port':%s}"%(proxy_ip[0],proxy_ip[1])
			proxy_info = eval(proxy_info)
			proxy_support = urllib2.ProxyHandler({"http" : "http://%(host)s:%(port)d" % proxy_info})
			opener = urllib2.build_opener(proxy_support)
			urllib2.install_opener(opener)
			try:
				htmlcode = urllib2.urlopen("http://www.qq.com",timeout=2).code
			 	if htmlcode == 200:
					write_file(_)
					#insert_db(proxy_ip[0],proxy_ip[1])
			except urllib2.URLError,e:
				pass
			except socket.timeout,e:
				pass
			except httplib.BadStatusLine,e:
				pass
			except urllib2.HTTPError,e:
				pass
			except Exception,e:
				pass
