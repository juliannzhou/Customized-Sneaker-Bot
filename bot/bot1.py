from threading import Thread
import webbrowser, time, schedule
from selenium import webdriver
import time
import urllib
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--profile-directory=Profile 2')
options.add_argument("user-data-dir=/Users/kwunyingzhou/Library/Application Support/Google/Chrome/")
driver = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=options)
x = 'https://www.roommate.studio/'
driver.get(x)

def check1():
    print("1 Working")
    while True:
        try:
            driver.switch_to.window(driver.window_handles[0])
            element1 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div/div[2]/div[1]/div/a/div[1]/div/img")))
            element1.click()
            time.sleep(2)
            driver.refresh()
        except TimeoutException:
            driver.switch_to.window(driver.window_handles[0])
            print("Britney Done!")
            break

def check2():
    print("2 Working")
    driver.execute_script("window.open('https://www.roommate.studio/');")
    while True:
        try:
            driver.switch_to.window(driver.window_handles[1])
            element2 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div/div[2]/div[2]/div/a/div[1]/div/img")))
            element2.click()
            time.sleep(2)
            driver.refresh()
        except TimeoutException:
            driver.switch_to.window(driver.window_handles[1])
            print("Jordan Done!")
            break

def check3():
    print("3 Working")
    driver.execute_script("window.open('https://www.roommate.studio/');")
    while True:
        try:
            driver.switch_to.window(driver.window_handles[2])
            element3 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div/div[2]/div[3]/div/a/div[1]/div/img")))
            element3.click()
            time.sleep(2)
            driver.refresh()
        except TimeoutException:
            driver.switch_to.window(driver.window_handles[2])
            print("Tree Hugger Done!")
            break


def check4():
    print("4 Working")
    driver.execute_script("window.open('https://www.roommate.studio/');")
    while True:
        try:
            driver.switch_to.window(driver.window_handles[3])
            element4 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div/div[2]/div[4]/div/a/div[1]/div/img")))
            element4.click()
            time.sleep(2)
            driver.refresh()
        except TimeoutException:
            driver.switch_to.window(driver.window_handles[2])
            print("Kobe Done!")
            break

def refresh():
    driver.refresh()

def close():
    driver.close()

if __name__ == "__main__":
    url = driver.current_url

    print(url)
    Thread(target=check1).start()
    Thread(target=check2).start()
    Thread(target=check3).start()
    Thread(target=check4).start()







