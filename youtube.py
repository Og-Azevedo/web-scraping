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

link = "https://www.google.com/"

def launchBrowser(link):
    driver = webdriver.Chrome(service=service)
    driver.get(link)
    return driver

def coletar_pesquisa(num_pag, driver, termo):
    #faz a pesquisa na página pricipal
    search = driver.find_element(By.CLASS_NAME, 'gLFyf')
    search.send_keys(termo)

    time.sleep(1)

    search.submit()

    time.sleep(1)

    #coleta os links da página
    count = 0
    while (count <= num_pag):
        time.sleep(2)

        ranking_seo = driver.find_elements(By.CLASS_NAME, "yuRUbf")

        for item in ranking_seo:
            try:
                titulo = item.find_element(By.TAG_NAME, "h3").text
                link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
                print(titulo)
                print(link)
            except:
                continue

        print(30 * "---")
        driver.find_element(By.XPATH, '//*[@id="pnnext"]/span[2]').click()
        count += 1




driver = launchBrowser(link)
coletar_pesquisa(3,driver,"iphone")




###---Finalizar o browser
time.sleep(5)
# driver.quit()






