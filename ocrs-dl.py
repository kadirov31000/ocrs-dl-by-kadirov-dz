import os
from extracter import ocrs
from downloader import download
from IPython.display import HTML, clear_output


ocrs()

download()

os.remove("out.txt")
os.remove("urlinfo.txt")
