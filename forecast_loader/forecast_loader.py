import re

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

link = 'https://www.windguru.cz/1825'


class Scraper(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS('/home/james/Downloads/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
        self.driver.set_window_size(1120, 550)

    def scrape(self):
        print('Loading...')
        self.driver.get(link)

        forecast = {}

        # while True:
        s = BeautifulSoup(self.driver.page_source, "html.parser")
        timesteps = s.find("table", {"class": "tabulka"}).find('id'== 'tabid_3_0_dates').find_all("td", {"class": "day1"})
        for ts in timesteps:
            print(ts.contents)
            cells = row.find_all("td")
            id = row['id']
            forecast[id] = []
            i = 0
            for cell in cells:
                if ('DIRPW' in id):  # or ('DIRPW' in id):
                    print(id + " " + str(i))
                    value = cell.find('span').find('svg').find('g')["transform"]
                else:
                    value = cell.get_text()
                forecast[id].append(value)
                i = i + 1

        print(forecast)

        self.driver.quit()
        return forecast


if __name__ == '__main__':
    scraper = Scraper()
    scraper.scrape()

