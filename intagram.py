from selenium import webdriver
import time 
from userlogin import userName, password

PATH = "C:\\Users\Murad\\Desktop\\chromedriver.exe"

browser = webdriver.Chrome()

browser.get("https://www.instagram.com/accounts/login/")


browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(userName)
browser.find_elements_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)

browser.find_elements_by_css_selector('button[type=submit]').click()