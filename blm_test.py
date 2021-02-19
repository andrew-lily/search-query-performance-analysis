# v2 updating to allow ingest of CSV File for search terms

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import logging
import array
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from colorama import init
init()
from colorama import Fore, Back, Style
from datetime import datetime, timezone
import os
import csv
import numpy as np
import itertools
import threading
import sys
import getopt
import time
from random import randint
from yaspin import yaspin
from yaspin.spinners import Spinners
from PIL import Image
from io import BytesIO
from subprocess import Popen, PIPE


#Vars
#s3 = boto3.resources('s3')
args = sys.argv
logging.basicConfig(level=logging.INFO)
#now = datetime.now(timezone.utc)
now = time.time()
search_term_list = ['womanand #x27^;s ankle socks', 'sheets']
shark_spinner = yaspin(Spinners.shark, color = "green")
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--window-size=1024,3000')
options.add_argument("user-agent=“Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36”")


#Check for input csv file
if len(args) > 1:
    #Reading in search term csv
    search_term_file = args[1]
    search_term_list = []
    with open(search_term_file) as csvfile:
    	csvReader = csv.reader(csvfile)
    	for row in csvReader:
    		search_term_list.append(row[0])
#Create a new directory for scraped assests based on current time/day
directory = str(now) + "/"
parent_dir = "/Users/andrewnelson/Dev/site_search_POC/search-query-performance-analysis/output/"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print(path)

#Scraping image and utag data from each search term
for x in search_term_list:
    try:
        search_term = x
        print(Fore.GREEN +"Searching for " + search_term)
        shark_spinner.start()
        driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver', options=options)
        driver.get('https://www.bloomingdales.com/shop/search?keyword=' + search_term)
        product_count = driver.find_element_by_class_name('page-range').text
        screenshot = driver.get_screenshot_as_png()
        #image = Image.open(StringIO.StringIO(screen))
        png_src = BytesIO(screenshot)
        png_data = Image.open(png_src)
        rgb_png_data = png_data.convert('RGB')
        rgb_png_data.save(path + search_term + "_" + str(now) + ".jpg", 'JPEG', optimize=True, quality=10)
        #driver.save_screenshot(path + search_term + "_" + str(now) + ".png")
        utag_data = driver.execute_script("return utag_data")
        with open(path + 'search_data_' + str(now) +'.json', 'a+') as json_file:
            json.dump(utag_data, json_file, indent=3)
            json_file.write("\n")
            #driver.find_element_by_css_selector("ul.grid-x>li>div>a").click();
            #product_id = driver.find_element_by_css_selector("ul.grid-x>li>div").get_attribute("id")
            #product_id_click = "css=#img_" + str(product_id) +  "> .alt-image > .thumbnailImage"
            #print(product_id_click)
            #driver.find_element_by_css_selector("css=#img_3312349>.alt-image>.thumbnailImage").click()
            #time.sleep(2)
        shark_spinner.stop()
        print ("\033[A\033[A")
        print(Fore.GREEN + 'The search term \"' + search_term + '\" returned ' + product_count)
        driver.quit()
    except Exception:
        print(Fore.GREEN + "Something went wrong searching for" + search_term)
        driver.quit()
        continue
