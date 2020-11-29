from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

def main(driver, url):
    
    driver.get(f"{url}")
    sleep(5) #para carregar os dados gerados por códigos

    div_conteudo = driver.find_element_by_xpath("//div[@id='conteudo']")
    span_conteudo = div_conteudo.find_element_by_tag_name("span")
    tables = span_conteudo.find_elements_by_tag_name("table")
    cont = 0
    for table in tables:
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            for a in row.find_elements_by_xpath('.//a'):
                cont += 1
                print(f"{cont}. {a.get_attribute('href')}")


driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
urls = ["http://www4.tjrj.jus.br/ejuris/ConsultaAcordao.aspx?DES=6321"]
for url in urls:
    main(driver,url)

"""contents = row.find_elements_by_tag_name("td")
            for content in contents:
                print(content.text)"""


