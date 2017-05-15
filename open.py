#!/usr/bin/python
"""
Created on Fri April 24 17:50:57 2015

@author: jamshid.k
"""
import time

import selenium
import lxml.html as LH

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os, time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
def login_page(wd,user,login):
    
    try:
        us_name = wd.find_element_by_id("login")
        pswd = wd.find_element_by_id("password")
        us_name.send_keys(user)
        pswd.send_keys(login)
        pswd.send_keys(Keys.RETURN)
        
    except Exception, e:
        pass


def start():
    menu = {}
    menu['1']="Beta" 
    menu['2']="Asn"
    menu['3']="hiphone"
    menu['4']="Gsf"
    menu['5']="Ses"
    menu['6']="Himatrix"
    menu['7']='Rservice'
    menu['8']='Aroma'
    menu['9']='Task Scrum'
    menu['10'] = 'Yas'
    options=menu.keys()
    options.sort()
    for entry in options: 
        print entry, menu[entry]

    selection=raw_input("Please Select a Project:") 
    if selection =='1': 
        version = raw_input("live/Test:")
        if version== 'l':
            host = 'orchiderp.net'
            port =9430
            user='orchid'
            login='556677001'
            passwd='Bet#2015' 
        else:
            host = 'orchiderp.net'
            port =9431
            user='orchid'
            login='556677001'
    elif selection == '2': 
        version = raw_input("live/Test:")
        if version== 'l':
            host='orchiderp.net'
            port=9352
            user='admin'
            login='asn123'
            passwd='9447770001'
        else:
            host='orchiderp.net'
            port=9351
            user='admin'
            login='asn123'
    elif selection == '3':
        host='128.199.247.125' 
        user='orchid'
        login='123'
        version = raw_input("live/Test:")
        if version== 'l': 
            port=8069
        else:
            port=9069
            
    elif selection == '4':
        version = raw_input("live/Test:")
        if version== 'l': 
            host='104.131.178.84'
            port=8069
            user='orchid'
            login='556677001'
            passwd='Gsf#2015'
        else:
            host='104.131.178.84'
            port=9069
            user='orchid'
            login='556677001'
            passwd='Gsf#2015'
            
    elif selection == '5':
        version = raw_input("live/Test:")
        if version== 'l': 
            host='104.236.215.84'
            port=8069
            user='orchid'
            login='556677001'
            passwd='Ses#2015'
        else:
            host='104.236.215.84'
            port=9069
            user='orchid'
            login='556677001'
            passwd='Ses#2015'
    elif selection == '6':
        host='himatrixerp.com' 
        user='admin'
        login='craig2005'
        version = raw_input("live/Test:")
        if version== 'l': 
            port=8069
        else:
            port=9069
    elif selection == '7':
        host = 'orchiderp.net'
        port =9451
        user='admin'
        login='res123'
    elif selection == '8':
        host='128.199.199.28' 
        user='Orchid'
        login='556677001'
        version = raw_input("live/Test:")
        if version== 'l': 
            port=8020
        else:
            port=9020
    elif selection == '9':
        host = 'orchiderp.com'
        port =8090
        user='jamshid@orchiderp.com'
        login='123'
    elif selection == '10':
        host='128.199.148.185' 
        user='admin'
        login='fslhggi'
        version = raw_input("live/Test:")
        if version== 'l': 
            port=8069
        else:
            port=9069
            
    else: 
        print "Unknown Option Selected!" 
    url = "http://" + host + ":" + str(port) + "/web"
    wd = webdriver.Firefox() # uses Firefox
    wd.get(url)    
    time.sleep(5)
    login_page(wd,user=user,login=login)
if(__name__=="__main__"):
    start() # for home page
