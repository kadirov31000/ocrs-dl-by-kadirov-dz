
import urllib.request
import requests
import progressbar
import os
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
class download:
    path = "/content/ocrs-dl-by-kadirov-dz/output"

    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
    def reporthook(blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 1e2 / totalsize
            s = "\r%5.1f%% %*d / %d" % (
                percent, len(str(totalsize)), readsofar, totalsize)
            sys.stderr.write(s)
            if readsofar >= totalsize: # near the end
                sys.stderr.write("\n")
        else: # total size is unknown
            sys.stderr.write("read %d\n" % (readsofar,))
    file1 = open('out.txt', 'r') 
    Lines = file1.readlines()
    for line in Lines: 
        
            nurl = line
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
        
            ndriver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
        
            baseURL = 'http://savevideo.me/'
            ndriver.get(baseURL)
            input_box = WebDriverWait(ndriver, 30).until(
                EC.presence_of_element_located((By.ID, 'url')))
        
            input_box.send_keys(nurl)
            clickdownload = WebDriverWait(ndriver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="search_results"]/div[1]/p[1]/a')))
            link = clickdownload.get_attribute('href')
            titledownload = WebDriverWait(ndriver, 30).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/table/tbody/tr/td[2]/div[3]/div[2]/div[2]/div[1]')))
            nanan = titledownload.get_attribute('title')
            lolo = nanan[11:]+ ".mp4"
            
            fullfilename = os.path.join(path, lolo)
            print(lolo)
            test = urllib.request.urlretrieve(link, fullfilename, reporthook)
        
            time.sleep(10)
            ndriver.quit()
    print('download finish')
