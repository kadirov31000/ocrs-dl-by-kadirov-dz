import os
from extracter import ocrs
from downloader import download
from IPython.display import HTML, clear_output


ocrs()
clear_output()
display(HTML("<center><h2 style=\"font-family:Trebuchet MS;color:#4f8bd6;\">Successfully get urls !</h2><br></center>"))
download()
clear_output()
display(HTML("<center><h2 style=\"font-family:Trebuchet MS;color:#4f8bd6;\">Successfully downloaded !</h2><br></center>"))
os.remove("/ocrs-dl-by-kadirov-dz/out.txt")
os.remove("/ocrs-dl-by-kadirov-dz/urlinfo.txt")
