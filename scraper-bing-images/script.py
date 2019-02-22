# bing images scraper
# runs in python 3
# tested on macbook air and macbook pro
# running macos high sierra
# by aaron montoya-moraga
# august 2018

# python dependencies
# these dont need any installation
# os is used for doing directory operations
import os
# sys is used for retrieving arguments from the terminal
import sys
# time is used for making the script pause and wait
import time
# string is used for string operations
import string
# TODO argparse is used for retrieving arguments from the terminal
import argparse
# pip install urllib3
import urllib.request
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# pip install Pillow
import PIL.Image

# execute this file script.py with python 3
# to check the version of python you can open terminal and write
# python --version
# or
# python3 --version
# and it will tell you if you are using python 3

# in this machine my alias is python3, so the command is
# python3 script.py "subject to scrape" maxImages
# where
# script.py is this file, can be retrieved with sys.argv[0]
# "subject to scrape" is a string,  retrievable with sys.argv[1]
# maxImages is a number, retrievable with sys.argv[2]

# retrieve the script
script = sys.argv[0]

# retrieve the subject to be scraped
#  default to "broccoli"
try:
    scrapeSubject = sys.argv[1]
except:
    scrapeSubject = "broccoli"

# retrieve the times of scraping google images
#  default to 4
# try:
#     scrapeTimes = sys.argv[2]
# except:
#     scrapeTimes = 4

try:
    # maxImages = sys.argv[3]
    maxImages = int(sys.argv[2])
except:
    maxImages = 100

# declaration of scraping function
def scrape(subject):

    # number of failed images download in a row before giving up
    maxFails = 20

    # number of current fails
    currentFails = 0

    # initialize downloaded list
    downloaded = list()

    # print starting scraping
    print("scraping " + subject)

    # create a new folder for saving scraped imagess
    # replace spaces with underscores
    auxSubject = "images_" + subject.replace(" ", "_")
    # check that the folder does not exist
    if not os.path.exists(auxSubject):
        # create the folder
        os.makedirs(auxSubject)

    # open a new google chrome window
    driver = webdriver.Chrome()

    #declare actionChains for right-click
    actionChains = ActionChains(driver)

    # set the window size
    driver.set_window_size(1200, 800)

    # queryBegin for images search
    queryBegin = "https://www.bing.com/images/search?&q="

    # append subject to complete the query URL
    queryURL = queryBegin + subject

    # change directory
    os.chdir(auxSubject)

    # do the query
    print("query bing images")

    # do the query
    driver.get(queryURL)

    # wait for loading
    time.sleep(3.0)

    # find all the results
    results = driver.find_elements_by_class_name("mimg")

    # click the first one
    results[0].click()

    # wait so that it loads
    time.sleep(2.0)

    # point to to iframe
    driver.switch_to.frame("OverlayIFrame")

    # wait
    time.sleep(1.0)

    # retrieve the image
    image = driver.find_element_by_xpath("//div[@class='imgContainer nofocus']//img")

    # retrieve the src
    src = image.get_attribute('src')
    local = auxSubject + "_" +  str(len(downloaded))

    # Fix to get around HTTP Error 403: Forbidden errors, aka the sites with the original src img give 403 errors to direct downloads.

    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    urllib.request.urlretrieve(src, local)

    downloaded.append(src)

    counter = 0

    # press right arrow and go to the next image
    actionChains.send_keys(Keys.RIGHT).perform()

    time.sleep(1.0)

    # get rid of popup
    # find popup
    popup = driver.find_element_by_xpath("//div[@class='action  exp nofocus']//span")
    # if there is a popup, click on it
    try:
        popup.click()
    except:
        print("didn't find any popup")

    time.sleep(1.0)

    # get rid of quit
#    quit = driver.find_element_by_xpath("//div[@class='Default']//div[@class='action  col nofocus']")
#    try:
#        quit.click()
#    except:
#        print("didn't find quit")

    # find the following ones until it breaks
    while counter < maxImages and (currentFails < maxFails):

        try:

            print("get the image")

            # retrieve the image
            images = driver.find_elements_by_xpath("//div[@class='imgContainer nofocus']//img")
            image = images[0]

            print("get the source")

            # retrieve the src
            src = image.get_attribute('src')
            local = auxSubject + "_" +  str(len(downloaded))

            print(src)

            # append it to the downloaded list
            downloaded.append(src)

            # download
            urllib.request.urlretrieve(src, local)

            print("downloaded " + str(len(downloaded)))

            time.sleep(1.0)

            # reset counter of fails
            currentFails = 0

        except:
            print("couldnt download the image")
            currentFails = currentFails + 1

        #get the next image
        #actionChains.send_keys(Keys.RIGHT).perform()
        next = driver.find_element_by_xpath("//div[@id='navr']//span")
        next.click()

        time.sleep(1.0)

        # advance counter
        counter = counter + 1

        time.sleep(0.1)

    time.sleep(100)

def convertToJPG():
    try:
        os.makedirs("_jpg")
    except:
        print("folder already created")

    for filename in os.listdir(os.getcwd()):
        # open original image
        if (filename[0] == "i"):
            try:
                PIL.Image.open(filename).convert("RGB").save("_jpg/" + filename + ".jpg", quality=100)
                print("converted " + filename + " to jpg")
            except:
                print("could not convert " + filename)

# call the function for scraping
scrape(scrapeSubject)

print("Done scraping, converting all images now to jpg")
# convert all the images to JPG format
convertToJPG()

# final message, goodbye, the end
print("finished scraping and converting to jpg. Yay 🎉")
