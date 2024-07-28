from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os

load_dotenv()

site_link = os.getenv("SITE_LINK")
service = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=service)

#Entrar no site
navegador.get(site_link)

#Para copiar o xpath do elemento, clique com o botão direito do mouse no elemento e clique em "Copiar" -> "Copiar XPath"
navegador.find_element('xpath', '//*[@id="botaoParticipar"]/div').click()

navegador.find_element('xpath', '//*[@id="firstname"]').send_keys('Lira')
navegador.find_element('xpath', '//*[@id="email"]').send_keys('Lira@videoSeleniumAutomacao.com')
navegador.find_element('xpath', '//*[@id="phone"]').send_keys('11 99999-9999')
navegador.find_element('xpath', '//*[@id="_form_8305_submit"]').click()

input("Pressione Enter para fechar o navegador...")
