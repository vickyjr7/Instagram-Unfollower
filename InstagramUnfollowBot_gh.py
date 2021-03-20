# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 01:00:31 2021

@author: VICKY JUNGHARE
"""
#importing required python packages
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains 
import time
import random

username= "Dummy" #Instagram Username
password= "Dummy@123" #Instagram Password

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe") #Chrome driver path may change according to your system
driver.get("https://www.instagram.com/")
enter_username = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'username')))
enter_username.send_keys(username)
   
enter_password = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'password')))
enter_password.send_keys(password)
enter_password.send_keys(Keys.RETURN)
time.sleep(random.randint(1,4))

try:
  	not_now = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'mt3GC')))
  	a= not_now.find_elements_by_tag_name("button")[1]
  	actions = ActionChains(driver)
  	actions.click(a)
  	actions.perform()
except:
   	pass

#Getting list Current follow requests
driver.get("https://www.instagram.com/accounts/access_tool/current_follow_requests")

users=[]    

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'lxml')
persons=soup.find_all('div',attrs= "-utLf") 


for b in persons[0:]:
    result = b.text.strip()
    users.append(result)
    
l=len(users)
for x in range(l): 
    driver.get("https://www.instagram.com/"+ users[x])
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button').click()
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
    time.sleep(random.randint(2,4))
