# selenium-login-hello-world
use selenium chromedriver to login to a webpage
 
``` python
# coding=utf-8
from selenium import webdriver
import os

# Prerequisite - download the selenium chromedriver and put it in this project
chromedriver_path = os.path.join(os.path.dirname(__file__), 'chromedriver')

username = 'myusername'
validPassword = 'myvalidPassword'
invalidPassword = 'myinvalidPassword'
login_url = 'https://<MYURL>'


def test_login(url, username, password):
    browser = webdriver.Chrome(chromedriver_path)
    browser.get()

    browser.find_element_by_id('username').send_keys(username)
    browser.find_element_by_id('password').send_keys(password)
    browser.find_element_by_id('submit').click()

    # if the target fields have not been blessed with readable id's, 
    # xpath is another (though brittle) identifier option. 
    # to get an x-path:
    # use chrome, right-click on the inputbox 
    # -> inspect *this opens the inspector window with your element highlighted 
    # -> right-click the highlighted portion -> copy -> copy as xpath -> paste in your code
    # using the find_element_by_xpath method
    # i.e. browser.find_element_by_xpath('//[1]').send_keys(username)

    success = browser.find_element_by_id('login')
    if success.text == u'login success':
        return "pass"
    else:
        return "fail"


print("Valid creds.  expected result: pass.  actual result: " + test_login(login_url, username, validPassword))
print("Invalid creds.  expected result: fail.  actual result: " + test_login(login_url, username, invalidPassword))
```
