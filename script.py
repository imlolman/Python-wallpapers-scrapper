import functions as f
from bs4 import BeautifulSoup as BS
import threading
import time
import config


mainLink = config.CONFIG['mainLink']
estimate_downoading_time_for_one_image_in_seconds = config.CONFIG['estimate_downoading_time_for_one_image_in_seconds']
threads = config.CONFIG['threads']
resolution = config.CONFIG['resolution']
foldername = config.CONFIG['foldername']


# getting all data from base page
soup = BS(f.getData(mainLink), 'html.parser')

# trying to get the last page
firstpage = 1
lastpage = int(f.getFileName(soup.findAll("a", {"class":"pager__link"})[2]['href']).replace("page",""))
lastpage = 3

# looping through all the page to download wallpapers with multithreading
for i in range(firstpage,lastpage+1):
  print("Starting downloading for page "+str(i))
  download_thread = threading.Thread(target=f.downloadAllFromPageLink, args=(mainLink+"/page"+str(i),resolution,foldername,))
  download_thread.start()
  time.sleep((estimate_downoading_time_for_one_image_in_seconds*15)/threads)
