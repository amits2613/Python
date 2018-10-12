#!/usr/bin/python3

import requests, sys

from requests.exceptions import ConnectionError

try:
	
	response = requests.get("https://www.yahoo.com")
	test = response.status_code

	if (test == 200):
		print("Success")

	else:
		print ("Fail\n",test, response.reason)

except ConnectionError as e:
        print ('BAD URL', e)
        


