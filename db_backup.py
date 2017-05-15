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



def backup(wd,passwd):
    try:
        backup_elem = wd.find_element_by_link_text("Backup").click()
        time.sleep(10)
        pswd = wd.find_element_by_name("backup_pwd")
        time.sleep(10)
        pswd.send_keys(passwd)
        time.sleep(10)
        pswd.send_keys(Keys.RETURN)
        while True:
            time.sleep(10)
    except Exception, e:
        raise e

def get_accounting(wd):
    try:
        account_link_element = wd.find_element_by_link_text("Accounting").click()
        time.sleep(10)
        wd.find_element_by_link_text("Customers").click()
        time.sleep(10)
        wd.find_element_by_class_name("oe_kanban_button_new oe_highlight").click()
    except Exception, e:
        raise e


def login_rservice(wd):
	
	try:
		us_name = wd.find_element_by_id("login")
		pswd = wd.find_element_by_id("password")
		us_name.send_keys('admin')
		pswd.send_keys('res123')
		wd.find_element_by_tag_name('button').send_keys(Keys.RETURN)
        
	except Exception, e:
		pass

        
def start_testing():
    menu = {}
    menu['1']="Beta" 
    menu['2']="Asn"
    menu['3']="hiphone"
    menu['4']="Gsf"
    menu['5']="Ses"
    menu['6']="Aroma"
    menu['7']="Yas"
    menu['8']="Himatrix"
    options=menu.keys()
    options.sort()
    for entry in options: 
        print entry, menu[entry]

    selection=raw_input("Please Select a Project:") 
    if selection =='1': 
        host = 'orchiderp.net'
        port =9430
        passwd='Bet#2015' 
    elif selection == '2': 
        host='orchiderp.net'
        port=9352
        passwd='9447770001'
    elif selection == '3':
        host='hptretail.com' 
        port=80
        passwd='Hip#2015'
    elif selection == '4': 
        host='104.131.178.84'
        port=8069
        passwd='Gsf#2015'
    elif selection == '5':
        host='104.236.215.84'
        port=8069
        passwd='Ses#2015'
    elif selection == '6':
        host='128.199.199.28'
        passwd='delight'
        port=8020
    elif selection == '7':
        host='128.199.148.185'
        port=8069
        passwd='hggih;fv'
    else: 
        print "Unknown Option Selected!" 
    
    url = "http://"+host+":"+str(port)+"/web/database/manager"
    wd = webdriver.Chrome() # uses Firefox
    wd.get(url) 
   
    time.sleep(10)
    backup(wd,passwd)
   


if(__name__=="__main__"):
    start_testing() # for home page
