import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my_account = driver.find_element_by_id('menu-item-50').click()
#Email = driver.find_element_by_id('reg_email')
#Email.send_keys('Egorovegor71@mail.ru')
#Password = driver.find_element_by_id('reg_password')
#Password.send_keys('123456qswA!!!')
#time.sleep(2)
#Register = driver.find_element_by_tag_name('[name="register"]').click()
#driver.quit()
name = driver.find_element_by_id('username')
name.send_keys('Egorovegor71@mail.ru')
password = driver.find_element_by_id('password')
password.send_keys('123456qswA!!!')
login = driver.find_element_by_tag_name('[name="login"]').click()
Logout = driver.find_element_by_css_selector('.woocommerce-MyAccount-navigation .woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout')
if Logout is not None:
    print('Элемент есть')
else:
    print('Элемента нет')
driver.quit()

