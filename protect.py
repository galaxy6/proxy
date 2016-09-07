#!/usr/bin/evn python2.7
#_*_coding:utf-8_*_

import os
import re
import sys
import time
import signal
import subprocess
from collections import deque

class Protect(object):
	'''
	程序出现错误或退出后，保护进程检测到错误进程进行杀死后并重启新的进程
	'''
	
	def __init__(self):
		self.run()
		
	def defend(self):
		keys = deque()
		result = os.popen('ps aux')
		res = result.read()
		for line in res.splitlines():
			if 'python task.py' in line:
				lines = line.split()
				if 'S' in lines[7]:
					keys.append(1)
				else:
					pid = int(lines[1])
					os.kill(pid,signal.SIGKILL)
					keys.append(0)
			else:
				keys.append(0)
		value = reduce(lambda x,y:x+y,keys)
		current = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
		if value == 0:
			subprocess.Popen('python task.py',shell=True)
			print "%s Program has been reset..."%current
		else:
			print "%s %s is running..."%(current,sys.argv[0])
		
	def run(self):
		while True:
			current_time = time.localtime()
			curhour = current_time.tm_hour
			curmin = current_time.tm_min
			if curhour < 11:
				deltahour = 11 - curhour
			else:
				deltahour = 24 - curhour + 11
			sleep_time = deltahour*3600 -curmin*60
			self.defend()
			time.sleep(sleep_time)

if __name__ == '__main__':
	Protect()
