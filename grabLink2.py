import os, time, logging, base64, datetime, openpyxl, pandas

from colorama import Fore
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

def iniciarBrowser(user):
    
    pasta = rf"C:\Users\{user}\Desktop"
    PATH = rf"C:\Users\{user}\Desktop\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory":
                     rf"{pasta}/",
                 "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(PATH, options=options)

    return browser

def main():

    link = input("Cole o link da pasta: ")

    browser = iniciarBrowser("FIGUEIG")
    browser.get(link)
    browser.maximize_window()

    time.sleep(2)

    imagens = []

    quantidadeDeImagens = browser.find_element(By.XPATH, 
    '//*[@id=":1"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div')
    quantidadeDeImagens = quantidadeDeImagens.get_attribute("childElementCount")

    time.sleep(1)
    print("\n")

    for imagem in range(1, int(quantidadeDeImagens)):

        seletor = browser.find_element(By.XPATH, 
        f'//*[@id=":1"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[{imagem}]')
        imagemLink = seletor.get_attribute("innerHTML")
        imagemLink = imagemLink.split('"')
        imagemLink = imagemLink[1].split('"')

        print(f"https://drive.google.com/uc?id={imagemLink[0]}")
    
    print("\n")

main()