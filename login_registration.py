import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

# # Registration_login: регистрация аккаунта
# # 1. Откройте https://practice.automationtesting.in/
# driver.get("https://practice.automationtesting.in/")
#
# # 2. Нажмите на вкладку "My Account"
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
#
# # 3. В разделе "Register", введите email для регистрации
# email = driver.find_element_by_id("reg_email")
# email.send_keys("basedof180@apn7.com")
#
# # 4. В разделе "Register", введите пароль для регистрации
# password = driver.find_element_by_id("reg_password")
# password.send_keys("222rrr444hhh")
#
# # 5. Нажмите на кнопку "Register"
# register = driver.find_element_by_css_selector("[name='register']")
# register.click()



# Registration_login: логин в систему
# 1. Откройте https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")

# 2. Нажмите на вкладку "My Account"
my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
# 3. В разделе "Login", введите email для логина
username = driver.find_element_by_id("username")
username.send_keys("basedof180@apn7.com")

# 4. В разделе "Login", введите пароль для логина
password = driver.find_element_by_id("password")
password.send_keys("222rrr444hhh")

# 5. Нажмите на кнопку "Login"
login = driver.find_element_by_css_selector("[name='login']")
login.click()

# 6. Добавьте проверку, что на странице есть элемент "Logout"
logout = driver.find_element_by_link_text("Logout")


time.sleep(1)
driver.quit()