import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 600);")
selenium_rubi = driver.find_element_by_tag_name('[data-product_id="160"]').click()
time.sleep(2)
reviems = driver.find_element_by_css_selector('.tabs.wc-tabs .reviews_tab').click()
star_5 = driver.find_element_by_css_selector('.comment-form-rating .star-5').click()
your_review = driver.find_element_by_id('comment')
your_review.send_keys("Nice book!")
name = driver.find_element_by_id('author')
name.send_keys('Egor')
Email = driver.find_element_by_id('email')
Email.send_keys('EgorkaEgorka@mail.ru')
time.sleep(2)
submit = driver.find_element_by_css_selector('.form-submit .submit').click()
driver.quit()