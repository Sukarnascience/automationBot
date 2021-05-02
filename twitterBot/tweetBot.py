'''
    Author : Sukarna Jana
    data   : 02/05/2021
    title  : making a twitter bot
'''

# to create delay 
import time
# to control our webbrowser
from selenium import webdriver
# to control webbrowser we need  web driver also
# foe this eg: we are taking FireFox web driver
# to install driver u need to go to
# https://github.com/mozilla/geckodriver/releases/tag/v0.29.1
# and download according to your needs
# sence i am using Ubuntu 64bit PC i have installed : geckodriver-v0.29.1-linux64.tar.gz
# give the path of your driver the place it's located...
driver = webdriver.Firefox(executable_path = "./geckodriver")
# now we will open twitter
# we will go directly to the login PG.
driver.get("https://twitter.com/login")
time.sleep(5)
# now we need to scarch a box by XPATH to type our username and password
# in your case XPATH may be different...

print("Hi... i am here to tweet your MSG: ;)")

userID = input("user id  :")
passwd = input("password :")
msg = input("what message you want to give :")

searchBox_login = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
searchBox_login.send_keys(userID)
searchBox_passwd = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
searchBox_passwd.send_keys(passwd)
loginBTN = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")
loginBTN.click()
time.sleep(5)
tweetBox = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div")
tweetBox.send_keys(msg)
sendtweet = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]")
sendtweet.click()

driver.close()

print("tweet has been dun ;)")
