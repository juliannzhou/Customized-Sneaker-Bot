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

# Get input information from user
name = input("Please enter full name: \n")
instagram = input("Please enter InstagramID(for seller to contact): \n")
email = input("Please enter email: \n")
in_hand = input("Shoe base in hand(yes/no): \n")
condition = input("Condition of shoe base(deadstock/used): \n")

# Setting up chrome profile to avoid bot detection
options = webdriver.ChromeOptions()
options.add_argument('--profile-directory=Profile 2')
options.add_argument("user-data-dir=/Users/kwunyingzhou/Library/Application Support/Google/Chrome/")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=options)
x = 'https://www.roommate.studio/'
driver.get(x)

# Product 1: first item on top left
def check1():
    print("1 Working")
    while True:
        try:
            # switches to tab and refreshes page until item becomes clickable
            driver.switch_to.window(driver.window_handles[0])
            element1 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div/div[2]/div[1]/div/a/div[1]/div/img")))
            element1.click()
            time.sleep(2)
            driver.refresh()
        except TimeoutException:
            # enter user information and submit form
            driver.switch_to.window(driver.window_handles[0])
            name_input = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='mui-7']")))
            name_input.send_keys(name)
            instagram_input = driver.find_element_by_xpath("//*[@id='mui-8']")
            instagram_input.send_keys(instagram)
            email_input = driver.find_element_by_xpath("//*[@id='mui-9']")
            email_input.send_keys(email)
            if in_hand == "yes":
                driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/form/fieldset[1]/div/button[1]").click()
            else:
                driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/form/fieldset[1]/div/button[2]").click()

            if condition == "deadstock":
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[2]/div/button[1]").click()
            else:
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[2]/div/button[2]").click()

            driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/form/button").click()
            print("product 1 submitted!")
            break

# product 2 on top right
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
            name_input = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='mui-7']")))
            name_input.send_keys(name)
            instagram_input = driver.find_element_by_xpath("//*[@id='mui-8']")
            instagram_input.send_keys(instagram)
            email_input = driver.find_element_by_xpath("//*[@id='mui-9']")
            email_input.send_keys(email)
            if in_hand == "yes":
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[1]/div/button[1]").click()
            else:
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[1]/div/button[2]").click()

            if condition == "deadstock":
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[2]/div/button[1]").click()
            else:
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[2]/div/button[2]").click()

            driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/form/button").click()
            print("product 2 submitted!")
            break

# product 3 on bottom left

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
            name_input = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='mui-7']")))
            name_input.send_keys(name)
            instagram_input = driver.find_element_by_xpath("//*[@id='mui-8']")
            instagram_input.send_keys(instagram)
            email_input = driver.find_element_by_xpath("//*[@id='mui-9']")
            email_input.send_keys(email)
            if in_hand == "yes":
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[1]/div/button[1]").click()
            else:
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[1]/div/button[2]").click()

            if condition == "deadstock":
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[2]/div/button[1]").click()
            else:
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[2]/div/button[2]").click()

            driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/form/button").click()
            print("product 3 submitted!")
            break

# product 4 on bottom right
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
            driver.switch_to.window(driver.window_handles[3])
            name_input = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='mui-7']")))
            name_input.send_keys(name)
            instagram_input = driver.find_element_by_xpath("//*[@id='mui-8']")
            instagram_input.send_keys(instagram)
            email_input = driver.find_element_by_xpath("//*[@id='mui-9']")
            email_input.send_keys(email)
            if in_hand == "yes":
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[1]/div/button[1]").click()
            else:
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[1]/div/button[2]").click()

            if condition == "deadstock":
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[2]/div/button[1]").click()
            else:
                driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div/div[2]/form/fieldset[2]/div/button[2]").click()

            driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/form/button").click()
            print("product 4 submitted!")
            break

def refresh():
    driver.refresh()

def close():
    driver.close()

if __name__ == "__main__":
    Thread(target=check1).start()
    Thread(target=check2).start()
    Thread(target=check3).start()
    Thread(target=check4).start()








