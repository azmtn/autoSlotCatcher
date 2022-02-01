from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

url = "https://signin.intra.42.fr/users/sign_in"
chrome_service = Service("/home/border/Desktop/autoSlotCatcher/chromedriver/chromedriver_linux")
driver = webdriver.Chrome(service=chrome_service)

try:
    driver.get(url=url)
    time.sleep(10)
    # driver.refresh() # обновление страницы
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()