import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')

def get_picture_link(pins_link):
    driver = webdriver.Chrome(options=option)
    driver.get(pins_link)
    time.sleep(5)
    Page_source = driver.page_source
    soup = BeautifulSoup(Page_source, 'lxml')
    picture_url = soup.find('img', class_='hCL kVc L4E MIw').get('src')
    download_picture(picture_url)

number = 1
def download_picture(picture_url):
    global number
    picture = requests.get(picture_url).content
    with open(f'pinterest_anime_girls\{number}.jpg', 'wb') as file:
        file.write(picture)
    print(f'Downloaded {number} images')
    number += 1

def main():
    file = list(link.strip() for link in open('links to pins.txt'))
    for link in file:
        get_picture_link(link)
        print(f'Downloaded {number} images')