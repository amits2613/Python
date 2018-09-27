#!/usr/bin/python3

from selenium import webdriver

br = webdriver.Firefox()
br.get('https://www.facebook.com/')
email = br.find_element_by_id('email')
email.send_keys('ixxxxxxxx@gmail.com')
pas = br.find_element_by_id('pass')
pas.send_keys('xxxxxxxxxx')
pas.submit()
