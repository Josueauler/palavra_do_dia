from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random

driver= webdriver.Chrome()
driver.get("https://www.bible.com/pt/bible/129/GEN.1.NVI")

livros= [
    "Gênesis", "Êxodo", "Levítico", "Números", "Deuteronômio",
    "Josué", "Juízes", "Rute",
    "1 Samuel", "2 Samuel",
    "1 Reis", "2 Reis",
    "1 Crônicas", "2 Crônicas",
    "Esdras", "Neemias", "Ester",
    "Jó", "Salmos", "Provérbios", "Eclesiastes", "Cânticos",
    "Isaías", "Jeremias", "Lamentações", "Ezequiel", "Daniel",
    "Oséias", "Joel", "Amós", "Obadias", "Jonas", "Miquéias",
    "Naum", "Habacuque", "Sofonias", "Ageu", "Zacarias", "Malaquias",
    "Mateus", "Marcos", "Lucas", "João",
    "Atos",
    "Romanos",
    "1 Coríntios", "2 Coríntios",
    "Gálatas", "Efésios", "Filipenses", "Colossenses",
    "1 Tessalonicenses", "2 Tessalonicenses",
    "1 Timóteo", "2 Timóteo",
    "Tito", "Filemom",
    "Hebreus",
    "Tiago",
    "1 Pedro", "2 Pedro",
    "1 João", "2 João", "3 João",
    "Judas",
    "Apocalipse"]

escolhido= random.choice(livros) #escolhe um dos livros

driver.minimize_window()
sleep(1)
buscar= driver.find_element(By.NAME, "Search")
botao= driver.find_element(By.XPATH, "//button[@class='relative items-center font-bold ease-in-out duration-100 focus:outline-2 focus:outline-info-light dark:focus:outline-info-dark hover:shadow-light-2 disabled:text-gray-50 dark:disabled:bg-gray-40 dark:disabled:text-white disabled:hover:shadow-none disabled:opacity-50 disabled:bg-gray-10 disabled:cursor-not-allowed max-w-fit dark:bg-yv-red-dark text-white text-xs px-3 inline-flex bg-yv-red rounded-full cursor-pointer h-4 w-4 justify-center mli-1 mlb-1 pli-0.5 z-base']")
buscar.send_keys(escolhido)
botao.click()
sleep(1)
versiculos= driver.find_elements(By.XPATH, "//p[@class]")
link= driver.find_elements(By.XPATH, "//a[@class]")

versiram= random.choice(versiculos[0:5])

versiculo= versiram
print('A palavra do dia é:\n{}'.format(versiculo.text))

completo= int(input('DIGITE 1 PARA LER O VERSÍCULO COMPLETO OU 2 PARA FINALIZAR:\n'))
if completo == 1:
    link[10].click()
    sleep(1)
    blink= driver.find_elements(By.XPATH, "//a[@href]")
    blink[1].click()
    driver.maximize_window()

while True:
    pass
