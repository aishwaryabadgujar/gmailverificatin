from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

gmail_id = "awxyz143@gmail.com"
gmail_password = "jamesbond@1"
driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")

url = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

#gmail website url
driver.get(url)

#For login id input
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(gmail_id)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()

#for password input
driver.implicitly_wait(15)
driver.find_element_by_name('password').send_keys(gmail_password)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()

#For compose function
driver.find_element_by_xpath('//*[@id=":3c"]/div/div').click()