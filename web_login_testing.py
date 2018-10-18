#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
import time
import os

driver self = webdriver.Firefox()
self.get('https://www.facebook.com/')
email = self.find_element_by_id('email')
email.send_keys('ixxxxxxxx@gmail.com')
pas = self.find_element_by_id('pass')
pas.send_keys('xxxxxxxxxx')
pas.submit()
