#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Importing the libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initialize the WebDriver 
driver = webdriver.Chrome()

# Open the web application's login page
driver.get("https://example.com/login")

# Finding the username and password input fields and entering credentials
username_input = driver.find_element(By.ID, "username")  
password_input = driver.find_element(By.ID, "password") 

username_input.send_keys("your_username")
password_input.send_keys("your_password")

# Submit the login form
login_button = driver.find_element(By.ID, "login-button") 
login_button.click()
if "dashboard" in driver.current_url:  
    print("Login successful!")
else:
    print("Login failed!")

# Close the browser
driver.quit()


# In[4]:





# In[ ]:




