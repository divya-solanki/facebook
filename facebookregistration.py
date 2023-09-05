import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "C:\\chromedriver.exe"
service = Service(chrome_driver_path)
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=chrome_options)

# option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=option)
# driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path='C:/Users/divya/Downloads/chromedriver-win64/chromedriver.exe')
driver.implicitly_wait(5)
driver.get('https://freetestdata.com/wp-content/uploads/2021/09/Free_Test_Data_100KB_DOC.doc')
driver.maximize_window()
#
#
# def generate_random_email():
#     random_name = ''.join(random.choice(string.ascii_lowercase) for x in range(12))
#     email = random_name + '@' + 'gmail.com'
#     return email
#
#
# def generate_random_password():
#     return ''.join(random.choice(string.ascii_letters) for x in range(12))
#
#
# driver.find_element(By.XPATH, "//button[contains(text(), 'Allow all cookies')]").click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[contains(text(), "Create new account")]').click()
# driver.find_element(By.NAME, 'firstname').send_keys('Toby')
# driver.find_element(By.NAME, 'lastname').send_keys('Maguire')
#
# email = generate_random_email()
# pwd = generate_random_password()
#
# driver.find_element(By.NAME, 'reg_email__').send_keys(email)
# driver.find_element(By.NAME, 'reg_email_confirmation__').send_keys(email)
# driver.find_element(By.NAME, 'reg_passwd__').send_keys(pwd)
#
# day = Select(driver.find_element(By.ID, 'day'))
# day.select_by_visible_text('13')
# month = Select(driver.find_element(By.ID, 'month'))
# month.select_by_visible_text('Sep')
# year = Select(driver.find_element(By.ID, 'year'))
# year.select_by_visible_text('2000')
#
# driver.find_element(By.XPATH, '//input[@value= "1"]').click()
# driver.find_element(By.NAME, 'websubmit').click()
# time.sleep(20)
