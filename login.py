from dependencies import *

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com")

username = driver.find_element_by_id("session_key")
username.send_keys(config.username)
password = driver.find_element_by_id("session_password")
password.send_keys(config.password)
driver.find_element_by_class_name("sign-in-form__submit-button").click()
