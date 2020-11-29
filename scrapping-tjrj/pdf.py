from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main(driver):
    driver.get("http://www4.tjrj.jus.br/ejud/ConsultaProcesso.aspx?N=2020.059.02843")
    sleep(5) #para carregar os dados gerados por códigos

    div_conteudo1 = driver.find_element_by_xpath("//div[@id='content-barra']")
    div_conteudo = driver.find_element_by_xpath("//a[3]").click() #cr-button
    

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
main(driver)

