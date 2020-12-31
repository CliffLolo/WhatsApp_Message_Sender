#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

#Load the chrome driver
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=user-data")

#Set executable_path to the location where your chromedriver is located
driver = webdriver.Chrome(options=chrome_options, executable_path=r"C:\Users\hp\Desktop\New folder (2)\chromedriver_win32/chromedriver.exe")
wait = WebDriverWait(driver, 60)
count = 0

#Open WhatsApp URL in chrome browser
driver.get("https://web.whatsapp.com/")

#Read the data from excel
data = pd.read_excel('contacts.xlsx',engine='openpyxl')
message = data['Message'][0]

#Iterate excel rows
for name in data['Name'].tolist():
    # Locate search box through x_path
    search_box = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    title = wait.until(lambda driver:driver.find_element_by_xpath(search_box))

    # Clear search box if any contact number is in it
    title.clear()

    # Send contact number in search box
    title.send_keys(str(data['Contact'][count]))
    count = count + 1

    # Wait for 4 seconds to search contact number
    time.sleep(4)

    try:
        element = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/span')
    except NoSuchElementException:
        message = message.replace('{name}',"{}")
        new_message = message.format(name)
        
        title.send_keys(Keys.ENTER)
        actions = ActionChains(driver)
        actions.send_keys(new_message)
        actions.send_keys(Keys.ENTER)
        actions.perform()

# end the instance of chromedriver or any driver used
driver.quit()


# In[ ]:




