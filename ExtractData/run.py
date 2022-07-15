# example.py
with open('jsData.txt', 'r') as file:
    data = file.read()

from selenium import webdriver

# Start Chrome Driver (only works on chrome version 104.10.1 or below
chromedriver = 'chromedriver'

options = webdriver.ChromeOptions()
 
options.add_argument("user-data-dir=C:/Users/Ruman/AppData/Local/Google/Chrome/User Data")
#insert your name in the 'Ruman' part to automatically sign in

driver = webdriver.Chrome(options=options)

URL = 'https://www.strava.com/athlete/training'

driver.get(URL)

# Execute JS
driver.execute_script(data)

#Copy and paste the extracted data into this conversion tool:
#https://www.convertcsv.com/json-to-csv.htm
