# coding=utf-8
from selenium import webdriver
import os
chromedriver_path = os.path.join(os.path.dirname(__file__), 'chromedriver')

username = 'myusername'
validPassword = 'myvalidPassword'
invalidPassword = 'myinvalidPassword'
login_url = 'https://login.com'


def test_login(url, username, password):
    browser = webdriver.Chrome(chromedriver_path)
    browser.get()

    #todo - find the actual dom elements. use chrome, right-click on the inputbox -> inspect *this opens the inspector window with your element highlighted -> right-click the highlighted portion -> copy -> copy as xpath -> paste in your code
    browser.find_element_by_xpath('//*[@id="user"]/div[1]/a').send_keys(username)
    browser.find_element_by_xpath('//*[@id="password"]/div[1]/a').send_keys(password)
    browser.find_element_by_xpath('//*[@id="submit"]/div[1]/a').click()

    success = browser.find_element_by_id('login')
    if success.text == u'login success':
        return "pass"
    else:
        return "fail"


print("Valid creds.  expected result: pass.  actual result: " + test_login(login_url, username, validPassword))
print("Invalid creds.  expected result: fail.  actual result: " + test_login(login_url, username, invalidPassword))

