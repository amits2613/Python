#!/usr/bin/python3

import requests, sys

from requests.exceptions import ConnectionError

try:
	
	response = requests.get("https://www.yahoo.com")
	c360 = response.status_code

	if (c360 == 200):
		print("Success")

	else:
		print ("Fail", resonse.reason)

except ConnectionError as e:
        print ('BAD URL', e)
        


