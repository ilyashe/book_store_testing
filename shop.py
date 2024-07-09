import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

# # Shop: отображение страницы товара
# # 1. Откройте https://practice.automationtesting.in/
# driver.get("https://practice.automationtesting.in/")
#
# # 2. Залогиньтесь
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# username = driver.find_element_by_id("username")
# username.send_keys("basedof180@apn7.com")
# password = driver.find_element_by_id("password")
# password.send_keys("222rrr444hhh")
# login = driver.find_element_by_css_selector("[name='login']")
# login.click()

# # 3. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
#
# # 4. Откройте книгу "HTML 5 Forms"
# html_5_forms = driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']")
# html_5_forms.click()
#
# # 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
# title = driver.find_element_by_class_name("product_title")
# title_text = title.text
# assert title_text == "HTML5 Forms"



# # Shop: количество товаров в категории
# # 1. Откройте https://practice.automationtesting.in/
# driver.get("https://practice.automationtesting.in/")
#
# # 2. Залогиньтесь
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# username = driver.find_element_by_id("username")
# username.send_keys("basedof180@apn7.com")
# password = driver.find_element_by_id("password")
# password.send_keys("222rrr444hhh")
# login = driver.find_element_by_css_selector("[name='login']")
# login.click()
#
# # 3. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
#
# # 4. Откройте категорию "HTML"
# html = driver.find_element_by_link_text("HTML")
# html.click()
#
# # 5. Добавьте тест, что отображается три товара
# items_count = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
# if len(items_count) == 3:
#     print("Отображается три товара")
# else:
#     print("Ошибка. Количество товаров: " + str(len(items_count)))



# # Shop: сортировка товаров
# # 1. Откройте https://practice.automationtesting.in/
# driver.get("https://practice.automationtesting.in/")
#
# # 2. Залогиньтесь
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# username = driver.find_element_by_id("username")
# username.send_keys("basedof180@apn7.com")
# password = driver.find_element_by_id("password")
# password.send_keys("222rrr444hhh")
# login = driver.find_element_by_css_selector("[name='login']")
# login.click()
#
# # 3. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
#
# # 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
#
# default = driver.find_element_by_css_selector("[value='menu_order']")
# default_selected = default.get_attribute("selected")
# if default_selected is not None:
#     print('Выбран вариант сортировки по умолчанию')
# else:
#     print('Ошибка! Выбран иной вариант сортировки')
#
# # 5. Отсортируйте товары по цене от большей к меньшей
# sort_by = driver.find_element_by_class_name("orderby")
# select = Select(sort_by)
# select.select_by_value("price-desc")
#
# # 6. Снова объявите переменную с локатором основного селектора сортировки
# # 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# high_to_low = driver.find_element_by_css_selector("[value='price-desc']")
# high_to_low_selected = high_to_low.get_attribute("selected")
# if high_to_low_selected is not None:
#     print('Выбран вариант сортировки по цене от большей к меньшей')
# else:
#     print('Ошибка! Выбран иной вариант сортировки')



# # Shop: отображение, скидка товара
# # 1. Откройте https://practice.automationtesting.in/
# driver.get("https://practice.automationtesting.in/")
#
# # 2. Залогиньтесь
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# username = driver.find_element_by_id("username")
# username.send_keys("basedof180@apn7.com")
# password = driver.find_element_by_id("password")
# password.send_keys("222rrr444hhh")
# login = driver.find_element_by_css_selector("[name='login']")
# login.click()
#
# # 3. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
#
# # 4. Откройте книгу "Android Quick Start Guide"
# android_quick = driver.find_element_by_css_selector("[title='Android Quick Start Guide']")
# android_quick.click()
#
# # 5. Добавьте тест, что содержимое старой цены = "₹600.00"
# book_old_price = driver.find_element_by_css_selector(".price > del > span")
# book_old_price_text = book_old_price.text
# assert book_old_price_text == "₹600.00"
#
# # 6. Добавьте тест, что содержимое новой цены = "₹450.00"
# book_new_price = driver.find_element_by_css_selector(".price > ins > span")
# book_new_price_text = book_new_price.text
# assert book_new_price_text == "₹450.00"
#
# # 7. Добавьте явное ожидание и нажмите на обложку книги
# book_cover = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
#
# # 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
# close = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# close.click()



# # Shop: проверка цены в корзине
# # 1. Откройте https://practice.automationtesting.in/
# driver.get("https://practice.automationtesting.in/")
#
# # 2. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
#
# # 3. Добавьте в корзину книгу "HTML5 WebApp Development"
# add_to_basket = driver.find_element_by_css_selector(".post-182 .button")
# add_to_basket.click()
#
# # 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# time.sleep(1)
# items_amount = driver.find_element_by_css_selector(".cartcontents")
# items_amount_text = items_amount.text
# assert items_amount_text == "1 Item"
# money_amount = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# money_amount_text = money_amount.text
# assert money_amount_text == "₹180.00"
#
# # 5. Перейдите в корзину
# cart = driver.find_element_by_css_selector(".wpmenucart-contents")
# cart.click()
#
# # 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# subtotal = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "180.00"))
#
# # 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
# total = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹183.60"))



# # Shop: работа в корзине
# # 1. Откройте https://practice.automationtesting.in/
# driver.get("https://practice.automationtesting.in/")
#
# # 2. Нажмите на вкладку "Shop"
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
#
# # 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# driver.execute_script("window.scrollBy(0, 300);")
# html_add_to_basket = driver.find_element_by_css_selector(".post-182 .button")
# html_add_to_basket.click()
# time.sleep(1)
# add_to_basket = driver.find_element_by_css_selector(".post-180 .button")
# add_to_basket.click()
#
# # 4. Перейдите в корзину
# cart = driver.find_element_by_css_selector(".wpmenucart-contents")
# cart.click()
#
# # 5. Удалите первую книгу
# time.sleep(1)
# remove_item = driver.find_element_by_css_selector("[data-product_id='182']")
# remove_item.click()
#
# # 6. Нажмите на Undo (отмена удаления)
# time.sleep(1)
# undo = driver.find_element_by_link_text("Undo?")
# undo.click()
#
# # 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# time.sleep(1)
# quantity = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
# quantity.clear()
# quantity.send_keys("3")
#
# # 8. Нажмите на кнопку "UPDATE BASKET"
# update_basket = WebDriverWait(driver, 10).until(
#      EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='update_cart']")))
# update_basket.click()
#
# # 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
# quantity_value = quantity.get_attribute("value")
# assert quantity_value == "3"
#
# # 10. Нажмите на кнопку "APPLY COUPON"
# time.sleep(1)
# apply_coupon = driver.find_element_by_css_selector("[name='apply_coupon']")
# apply_coupon.click()
#
# # 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# total = WebDriverWait(driver, 10).until(
#      EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error"), "Please enter a coupon code."))



# Shop: покупка товара
# 1. Откройте https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")

# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
shop = driver.find_element_by_id("menu-item-40")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")

# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
html_add_to_basket = driver.find_element_by_css_selector(".post-182 .button")
html_add_to_basket.click()

# 4. Перейдите в корзину
time.sleep(1)
cart = driver.find_element_by_css_selector(".wpmenucart-contents")
cart.click()

# 5. Нажмите "PROCEED TO CHECKOUT"
proceed_to_checkout = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
proceed_to_checkout.click()

# 6. Заполните все обязательные поля
firstname = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.ID, "billing_first_name")))
firstname.send_keys("Ivan")

lastname = driver.find_element_by_id("billing_last_name")
lastname.send_keys("Ivanov")

email = driver.find_element_by_id("billing_email")
email.send_keys("basedof180@apn7.com")

phone = driver.find_element_by_id("billing_phone")
phone.send_keys("+79999992233")

country = driver.find_element_by_css_selector(".country_select.select2-container")
country.click()
country_search = driver.find_element_by_id("s2id_autogen1_search")
country_search.send_keys("Serbia")
country_option = driver.find_element_by_css_selector(".select2-match")
country_option.click()

address = driver.find_element_by_id("billing_address_1")
address.send_keys("Kneza Milosha")

city= driver.find_element_by_id("billing_city")
city.send_keys("Nish")

state= driver.find_element_by_id("billing_state")
state.send_keys("Kraina")

postcode= driver.find_element_by_id("billing_postcode")
postcode.send_keys("111666")

# 7. Выберите способ оплаты "Check Payments"
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
check_payments = driver.find_element_by_id("payment_method_cheque")
check_payments.click()

# 8. Нажмите PLACE ORDER
time.sleep(2)
driver.execute_script("window.scrollBy(0, 100);")
place_order = driver.find_element_by_id("place_order")
place_order.click()

# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
thank_you = WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
payment_method = WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method"), "Check Payments"))


time.sleep(3)
driver.quit()