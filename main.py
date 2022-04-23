#baixar o crhomedriver https://chromedriver.chromium.org/downloads
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from os.path import exists
import time


service = Service(executable_path=ChromeDriverManager().install())

def launchBrowser():


    driver = webdriver.Chrome(service=service)
    driver.get("https://pt.wikipedia.org/wiki/As_Aventuras_da_Turma_da_M%C3%B4nica")
    # driver.get(r"file:///C:/Users/yogoc/Downloads/site/Hashtag%20Treinamentos%20_%20Aprenda%20TUDO%20de%20Excel,%20VBA%20e%20Power%20BI.html")
    return driver



# time.sleep(1)
# driver.find_element(By.ID, 'fullname').send_keys("og Azevedo")
# driver.find_element(By.ID, 'email').send_keys("og@gmail.com")
# driver.find_element(By.ID, '_form_173_submit').click()


driver = launchBrowser()
# driver.find_element(By.ID, 'fullname').send_keys("og Azevedo")
time.sleep(1)
# driver.find_element(By.CLASS_NAME, "header-grid__logo__link--icon").click()
# titulo = driver.find_element(By.TAG_NAME, 'i').text
# print(titulo)
#
# link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Rio de").text
# print(link_text)
#
#
# driver.find_element(By.CLASS_NAME, "mw-ui-icon-wikimedia-search").click()
# time.sleep(1)
# driver.find_element(By.NAME, "search").send_keys(link_text)

menu_lateral = driver.find_elements(By.TAG_NAME, "a")

for item in menu_lateral:
    if "esplanada" in item.text.lower():
        print(item.text)
        item.click()
        break
# for tx in titulo[:3]:
#     print(titulo.text)

# driver.quit()

