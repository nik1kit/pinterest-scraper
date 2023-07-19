from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time
import pickle
from download_picture import get_picture_link

# def get_picles(driver):
#     pickle.dump(driver.get_cookies(), open('cookies.pkl', 'wb'))

def get_url_pins():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    url = 'https://ru.pinterest.com/JusteatmeAnnie/anime-girls/'

    driver.get(url)
    time.sleep(5)

    main_link_pins_of_pictures = []

    # Логинимся
    time.sleep(5)
    driver.find_element(By.XPATH, '//button[@class="RCK Hsu USg adn CCY NTm KhY iyn oRi lnZ wsz YbY"]').click()
    time.sleep(2)
    log_in_input_field = driver.find_element(By.XPATH, '//input[@placeholder="Адрес электронной почты"]')
    time.sleep(1)
    log_in_input_field.clear()
    time.sleep(1)
    print('Enter the login...')
    log_in_input_field.send_keys('artemyser127@gmail.com') # Ваша почта
    password_input_field = driver.find_element(By.XPATH, '//input[@placeholder="Пароль"]')
    time.sleep(1)
    password_input_field.clear()
    time.sleep(1)
    print('Enter the password...')
    password_input_field.send_keys('Nopassword1230') # Ваш пароль
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[@class="red SignupButton active"]').click()
    time.sleep(6)

    # Начинаем скролить страницу и подгружать пины
    SCROLL_PAUSE_TIME = 2
    SCROLLS = 0
    # Получаем высоту прокрутки
    last_height = driver.execute_script("return document.body.scrollHeight")
    print('Starting work...')

    while SCROLLS < 100:
        # Получаем код страницы
        Page_source = driver.page_source
        soup = BeautifulSoup(Page_source, 'lxml')
        pins_of_pictures = soup.find_all('a', class_='Wk9 xQ4 CCY S9z DUt iyn kVc agv LIa')
        link_pins_of_pictures = []

        # Получаем ссылки на пины и записываем в файл
        for item in pins_of_pictures:
            pins_url = 'https://ru.pinterest.com' + item.get('href')
            link_pins_of_pictures.append(pins_url)
        # with open('links to pins.txt', 'a', encoding='utf-8') as file:
        #     for pins in link_pins_of_pictures:
        #         if pins not in main_link_pins_of_pictures:
        #             file.write(pins + '\n')
        # get_picture_link(pins)
        for pins in link_pins_of_pictures:
            if pins not in main_link_pins_of_pictures:
                get_picture_link(pins)
        for item in link_pins_of_pictures:
            main_link_pins_of_pictures.append(item)

        time.sleep(SCROLL_PAUSE_TIME)
        # Прокрутить страницу до самого низа
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Обновлем счётчик
        SCROLLS += 1
        print('Начинаю цикл заново')
        continue
        # # Ожидаем конца прокрутки и подгрузки пинов
        # time.sleep(SCROLL_PAUSE_TIME)
        #
        #
        # # Вычисляем новую высоту прокрутки и сравниваем со старой
        # new_height = driver.execute_script("return document.body.scrollHeight")
        # if new_height == last_height:
        #     break
        # last_height = new_height




def main():
    get_url_pins()


if __name__ == '__main__':
    main()
    print('Images downloaded')
    time.sleep(5)

