#!/usr/bin/env python
#-- encoding:utf-8 --

import time
import logging
from proxy import *

def logger():
	logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='./log/task.log')	
def task():
    print "task is running..."
    logging.debug('task is runnging ....')

def timer():
	logger()
	task()
	while True:
		current_time = time.localtime()
		curhour = current_time.tm_hour
		curmin = current_time.tm_min
		if curhour < 10:
			deltahour = 10 - curhour
		else:
			deltahour = 24 - curhour + 10
		sleep_time = deltahour*3600 -curmin*60
        
		diff_time = 30*60
		proxy_test()
		time.sleep(sleep_time)

if __name__ == '__main__':
    timer()
