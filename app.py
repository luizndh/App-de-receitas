import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.opera.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = "E:\Projetos VSCode\Python\GUI App\chromedriver\chromedriver.exe"

nav = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
nav.get('https://bakeandcakegourmet.com.br/receitas')

# Iterando por todas as páginas de receitas
while True:
    
    # Entrar na div externa primeiro, para fazer com que a interna possa ser visualizada 
    div_externa = nav.find_elements(By.CSS_SELECTOR, "div.receita-div-listagem")
    
    # Iterando por todas as receitas por página
    for elemento in div_externa:
        elemento.click()

        div_interna = elemento.find_element(By.CSS_SELECTOR, "div.receita-div-ver-button")
        links = div_interna.find_elements(By.TAG_NAME, "a")
        time.sleep(0.5)
        links[2].click()
        # pega as informações da receita...
        nav.back()


    # Ir para a próxima pagina
    try:
        proxima_pagina = nav.find_element(By.CSS_SELECTOR, "a.page-link")
    except NoSuchElementException:
        print("Acabou as páginas.")
        break
    proxima_pagina.click()


