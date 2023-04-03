from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
import json

options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"

nav = webdriver.Chrome(options=options)
nav.get('https://bakeandcakegourmet.com.br/receitas')

receitas_dict = {}
id_receita = 1

# Iterando por todas as páginas de receitas
while True:
    
    # Entrar na div externa primeiro, para fazer com que a interna possa ser visualizada 
    div_externa = nav.find_elements(By.CSS_SELECTOR, "div.receita-div-listagem")
    
    # Iterando por todas as receitas por página
    for receita in div_externa:
        receita.click()

        div_interna = receita.find_element(By.CSS_SELECTOR, "div.receita-div-ver-button")
        links = div_interna.find_elements(By.TAG_NAME, "a")
        time.sleep(0.2)
        links[2].click()
        
        # Fazendo uma espera até que os elementos da página estejam disponíveis para serem acessados, e pegando nome da receita
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        nome_receita = WebDriverWait(nav, 3, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "h2.user-pacotes-div-title"))).text      
        
        # Pegando a descrição da receita
        descricao_receita = nav.find_element(By.CSS_SELECTOR, "p.sinopse").text
        
        # Pegando o tempo de preparo da receita
        div_preparo = nav.find_element(By.CSS_SELECTOR, "div.preparo")
        tempo_preparo = div_preparo.find_element(By.TAG_NAME, "p").text
        
        # Pegando os utensílios necessários para fazer a receita
        div_utensilios = nav.find_element(By.CSS_SELECTOR, "div.receita-single")
        utensilios = div_utensilios.find_elements(By.XPATH, "./div[3]")[0].text

        # Pegando os equipamentos necessários para fazer a receita
        equipamentos = div_utensilios.find_elements(By.XPATH, "./div[4]")[0].text
        
        # Pegando os medidores necessários para fazer a receita
        medidores = div_utensilios.find_elements(By.XPATH, "./div[5]/p")[0].text

        # Pegando os ingredientes necessários para realizar a receita
        div_ingredientes = nav.find_element(By.ID, "content-list-ingredientes")
        informacoes_ingredientes = div_ingredientes.find_elements(By.XPATH, ".//*")
      
        lista_informacoes_receita = {}
        lista_ingredientes_titulo = ""
        lista_ingredientes_conteudo = ""
        
        # O loop a seguir itera por todos os ingredientes da receita, separando-os pelos tópicos especificados do site.
        i = 0
        while i < len(informacoes_ingredientes) - 1:
                if informacoes_ingredientes[i].tag_name == "p":
                    lista_ingredientes_titulo = informacoes_ingredientes[i].text
                    lista_ingredientes_conteudo = ""
                    i += 1
                    
                    while informacoes_ingredientes[i].tag_name != "p":
                        if informacoes_ingredientes[i].tag_name == "div":
                            lista_ingredientes_conteudo += informacoes_ingredientes[i].text + "\n"
                        i += 1
                        
                        if i == len(informacoes_ingredientes) - 1:
                            break
                    
                    # Todas as informações da receita são adicionadas à um dicionário
                    lista_informacoes_receita.update([('nome', nome_receita)])
                    lista_informacoes_receita.update([('descricao', descricao_receita)])
                    lista_informacoes_receita.update([('tempo_preparo', tempo_preparo)])
                    lista_informacoes_receita.update([('utensilios', utensilios)])
                    lista_informacoes_receita.update([('equipamentos', equipamentos)])
                    lista_informacoes_receita.update([('medidores', medidores)])
                    lista_informacoes_receita.update([(lista_ingredientes_titulo, lista_ingredientes_conteudo)])
                    
        # Depois, cada receita é adicionada à um novo dicionário com um id relacionado a cada receita.
        receitas_dict.update([(id_receita, lista_informacoes_receita)])
        id_receita += 1
        
        nav.back()


    # Ir para a próxima pagina, até encontrar a última
    try:
        proxima_pagina = nav.find_element(By.PARTIAL_LINK_TEXT, "Próxima ")
    except NoSuchElementException:
        print("Acabaram as páginas.")
        break
    proxima_pagina.click()

# O dicionário das receitas é usado para criar o arquivo JSON.
with open('receitas.JSON', 'w', encoding='UTF-8') as receitas:
    receitas.write(json.dumps(receitas_dict, indent=2))


nav.quit()


