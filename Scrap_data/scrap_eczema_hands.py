from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
import os
from pywget import wget
import time


class Scrap:
    def __init__(self):
        self.url = "http://www.dermnet.com/images/Eczema-Hand/photos/"
        self.base_image_url = 'http://www.dermnet.com/dn2/allJPG3/eczema-hand-'

    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        chrome_p = os.listdir('../chrome_driver/')[0]
        chrome_path = f'chrome_driver/{chrome_p}'
        driver = webdriver.Chrome(chrome_path, options=options)
        return driver

    def get_data(self, no):
        driver = self.get_driver()
        req = self.url + str(no)
        driver.get(req)
        soup = BeautifulSoup(driver.page_source, 'html')
        print(soup)

    def get_url(self, no):
        return f'{self.base_image_url}{no}.jpg'

    def get_images(self, download_folder):
        err = []
        for i in range(9,100):
            try:
                wget.download(self.get_url(i), fr'{download_folder}/')
                print('> ', i)
                time.sleep(1)
            except Exception as e:
                time.sleep(1)
                err.append(i)
                print('x ', i)

        print('data downloaded')
        print(f'error in {err}')



Scrap().get_images('../data/ec')
