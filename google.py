from selenium import webdriver

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def start():
    print("Welcome to the project Search :) ")
    print("0 - Exit the console")
    print("1 - Search")
    user_input = input("Enter Your Choice: ")
    if user_input == "1":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get('https://www.google.com/')
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div").click()
        search = input("Enter what you wanna search: ")
        textbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        textbox.send_keys(search)
        print('Result has opened in your browser.')
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
        time.sleep(1000)
    elif user_input == "0":
        print("Good Bye, Have a great day!")
    else:
        print("Please enter valid user-input.")

start()