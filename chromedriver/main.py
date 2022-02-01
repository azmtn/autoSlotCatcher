from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from sys import platform
import time
import os

url = ""
login = ""
password = ""


options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36")

abspath = os.path.abspath("chromedriver_linux" if platform == "linux" else "chromedriver_mac")
chrome_service = Service(abspath)
driver = webdriver.Chrome(service=chrome_service, options=options)

try:
    driver.get(url="https://signin.intra.42.fr/users/sign_in")
    time.sleep(2)

    login_input = driver.find_element(By.ID, "user_login")
    login_input.clear()
    login_input.send_keys(login)

    password_input = driver.find_element(By.ID, "user_password")
    password_input.clear()
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    time.sleep(10)

    # driver.refresh() # обновление страницы
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
