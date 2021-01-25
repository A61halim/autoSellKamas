from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from notify import notification

import time
PATH = 'C:\\Users\\alakf\\Desktop\\kamasSite\\chromedriver.exe'

driver = webdriver.Chrome(PATH)
#/html/body/div[1]/div/div[1]/section/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[3]/center/a
mail = "alakfifi900@gmail.com"
passw = "testtest"

driver.get("https://vente.tryandjudge.com/dofuskamas.php")


sell = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[3]/center/a')
if sell.text == 'Cliquez ici pour Vendre':
    sell.click()
    notification('Jri jri rah t7aal',title="bi3 Kama")
    email = driver.find_element_by_xpath('//*[@id="email"]')
    email.send_keys(mail)
    mdp = driver.find_element_by_xpath('//*[@id="mdp"]')
    mdp.send_keys(passw)
    mdp.send_keys(Keys.ENTER)

else:
    pass