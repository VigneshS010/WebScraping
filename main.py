from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

s = Service("C:/Users/Vignesh S/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=s)
driver.get("https://www.ajio.com/men-jeans/c/830216001")
time.sleep(3)

t_end = time.time() + 10 * 1

Names = []
Prices = []
Desc = []
Reviews = []

while time.time() < t_end:
    height = driver.execute_script("return document.body.scrollHeight")
    print(height)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    new_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        r=requests.get()

        soup = BeautifulSoup(r.text, "lxml")
        # box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

        name = soup.find_all("div", class_="nameCls")
        time.sleep(0.1)
        for i in name:
            n = i.text
            Names.append(n)
        print(len(Names))

        price = soup.find_all("div", class_="price  ")
        time.sleep(0.1)
        for i in price:
            n = i.text
            Prices.append(n)
        print(len(Prices))

        desc = soup.find_all("div", class_="offer-pricess")
        time.sleep(0.1)
        for i in desc:
            n = i.text
            Desc.append(n)
        print(len(Desc))

        # rev = soup.find_all("div", class_="_3LWZlK")
        # for i in rev:
        #     n = i.text
        #     Reviews.append(n)
        # print(len(Reviews))

df = pd.DataFrame(
    {"Product name": Names, "Product price": Prices, "Product description": Desc})

df.to_csv("Premium Lap.csv")
