import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.opera.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
import json
import io


options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = "E:\Projetos VSCode\Python\GUI App\chromedriver\chromedriver.exe"

# Escolhendo qual navegador irei usar
nav = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
nav.get('https://bakeandcakegourmet.com.br/receitas')

# Iterando por todas as páginas de receitas
while True:
    
    # Entrar na div externa primeiro, para fazer com que a interna possa ser visualizada 
    div_externa = nav.find_elements(By.CSS_SELECTOR, "div.receita-div-listagem")
    
    # Iterando por todas as receitas por página
    for receita in div_externa:
        receita.click()

        div_interna = receita.find_element(By.CSS_SELECTOR, "div.receita-div-ver-button")
        links = div_interna.find_elements(By.TAG_NAME, "a")
        time.sleep(0.5)
        links[2].click()
        
        # Pegando as informações de cada receita
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        # Fazendo uma espera até que os elementos da página estejam disponíveis para serem acessados, e pegando nome da receita
        nome_receita = WebDriverWait(nav, 3, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "h2.user-pacotes-div-title"))).text      
        
        # Pegando a descrição da receita
        descricao_receita = nav.find_element(By.CSS_SELECTOR, "p.sinopse").text
        
        # Pegando o tempo de preparo da receita
        div_preparo = nav.find_element(By.CSS_SELECTOR, "div.preparo")
        tempo_preparo = div_preparo.find_element(By.TAG_NAME, "p").text
        
        # Pegando os utensílios necessários para fazer a receita
        div_utensilios = nav.find_element(By.CSS_SELECTOR, "div.receita-single")
        utensilios = div_utensilios.find_elements(By.XPATH, "./div[3]")[0].text
        print(f'Utensilios: {utensilios}')

        # Pegando os equipamentos necessários para fazer a receita
        equipamentos = div_utensilios.find_elements(By.XPATH, "./div[4]")[0].text
        print(f'Equipamentos: {equipamentos}')
        
        # Pegando os medidores necessários para fazer a receita
        medidores = div_utensilios.find_elements(By.XPATH, "./div[5]/p")[0].text
        print(f'Medidores: {medidores}')
        
        # Pegando os ingredientes necessários para realizar a receita
        div_ingredientes = nav.find_element(By.ID, "content-list-ingredientes")
        tipos_ingredientes = div_ingredientes.find_elements(By.CSS_SELECTOR, "p.receita-single-ingrediente-title")
        
        #i = 0
        #for tipo_ingr in tipos_ingredientes:
        #    titulo_tipo_ingr = tipo_ingr.text
        #    ingredientes = 
        
        nav.back()


    # Ir para a próxima pagina
    try:
        proxima_pagina = nav.find_element(By.CSS_SELECTOR, "a.page-link")
    except NoSuchElementException:
        print("Acabou as páginas.")
        break
    proxima_pagina.click()
    

nav.quit()


