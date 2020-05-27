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

    print('start extract urls')
    for link in BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('a', href=True)):
        res = requests.get('https://openclassrooms.com/%s' % (link['href']))
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        comi = soup.select('div video a')
        if comi == []:
            pass
        else:
            vvvv = str(comi[0])
            lil = vvvv[9:36]
            with open("urlinfo.txt", 'a') as txtFile:
                txtFile.writelines("{}\n".format(lil))

    print ('end extract url video')
    with open("urlinfo.txt", "r") as f:
        lines = f.readlines()
    with open("urlinfo.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != "https://player.vimeo.com/vi":
                f.write(line)
    lines_seen = set() # holds lines already seen
    outfile = open("out.txt", "w")
    for line in open("urlinfo.txt", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()               
 


			
			
        
