import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

#Home: добавление комментария
#1. Откройте https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")

#2. Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")

#3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
selenium_ruby = driver.find_element_by_css_selector("[title='Selenium Ruby']")
selenium_ruby.click()

#4. Нажмите на вкладку "REVIEWS"
reviews = driver.find_element_by_class_name("reviews_tab")
reviews.click()

#5. Поставьте 5 звёзд
star_5 = driver.find_element_by_class_name("star-5")
star_5.click()

#6. Заполните поле "Review" сообщением: "Nice book!"
review = driver.find_element_by_id("comment")
review.send_keys("Nice book!")

# 7. Заполните поле "Name"
name = driver.find_element_by_id("author")
name.send_keys("Ilia")

# 8. Заполните "Email"
email = driver.find_element_by_id("email")
email.send_keys("test@test.ru")

# 9. Нажмите на кнопку "SUBMIT"
submit = driver.find_element_by_id("submit")
submit.click()

time.sleep(1)
driver.quit()