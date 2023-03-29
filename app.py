import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.opera.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Definindo o navegador que será usado para pegar os dados do site escolhido
options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = "E:\Projetos VSCode\Python\GUI App\chromedriver\chromedriver.exe"

nav = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
nav.get('https://bakeandcakegourmet.com.br/receitas')


