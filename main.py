from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")
input()

mensagem = """ Olá, tudo bem? Esta mensagem esta sendo enviada por automação.
Não precisa responder! Estou testando!"""
lista_contatos = ["Glauco Silva", "Nivea Mana Love", "Priscila Prisgay", "Any"]


## Vai ser enviado uma msg para 1 pessoa e depois encaminhado para o restante.
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
##escreve na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys('Glauco Silva')
##aperta o enter - para isso tem que importar a chave (Keys)
pyperclip.copy(mensagem)
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + "v")
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(5)






