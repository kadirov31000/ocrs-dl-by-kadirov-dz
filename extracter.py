import requests

import os
import requests, os, bs4, threading
from bs4 import BeautifulSoup, SoupStrainer

import sys
class ocrs:
    print('''
    ██╗  ██╗ █████╗ ██████╗ ██╗██████╗  ██████╗ ██╗   ██╗      ██████╗ ███████╗
    ██║ ██╔╝██╔══██╗██╔══██╗██║██╔══██╗██╔═══██╗██║   ██║      ██╔══██╗╚══███╔╝
    █████╔╝ ███████║██║  ██║██║██████╔╝██║   ██║██║   ██║█████╗██║  ██║  ███╔╝ 
    ██╔═██╗ ██╔══██║██║  ██║██║██╔══██╗██║   ██║╚██╗ ██╔╝╚════╝██║  ██║ ███╔╝  
    ██║  ██╗██║  ██║██████╔╝██║██║  ██║╚██████╔╝ ╚████╔╝       ██████╔╝███████╗
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═══╝        ╚═════╝ ╚══════╝
                                                                           
    ''')
    url = input('put url here ==> ')


    response = requests.get(url)


    for link in BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('a', href=True)):
        res = requests.get('https://openclassrooms.com/%s' % (link['href']))
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        comi = soup.select('div video a')
        if comi == []:
            pass
        else:
            comii = soup.find("video").get("src")
            with open("urlinfo.txt", 'a') as txtFile:
                txtFile.writelines("{}\n".format(comii))

    print ('end extract url video')
    lines_seen = set() # holds lines already seen
    outfile = open("out.txt", "w")
    for line in open("urlinfo.txt", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()               
 


			
			
        
