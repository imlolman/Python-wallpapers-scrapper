import functions as f
from bs4 import BeautifulSoup as BS
import threading
import time
import config


mainLink = config.CONFIG['mainLink']
threads = config.CONFIG['threads']
resolution = config.CONFIG['resolution']
foldername = config.CONFIG['foldername']
pages_to_download = config.CONFIG['pages_to_download']

# getting all data from base page
print("Fatching Main Data......")
soup = BS(f.getData(mainLink), 'html.parser')

# trying to get the first and last page
if(len(pages_to_download.split('-')) < 2):
  firstpage = 1
  lastpage = int(f.getFileName(soup.findAll("a", {"class":"pager__link"})[2]['href']).replace("page",""))
else:
  firstpage = int(pages_to_download.split('-')[0])
  lastpage = int(pages_to_download.split('-')[1])

# looping through all the page to download wallpapers with multithreading
threads = []
print("Initiating Downloading..\n")
for i in range(firstpage,lastpage+1):
  download_thread = threading.Thread(target=f.downloadAllFromPageLink, args=(mainLink+"/page"+str(i),resolution,foldername,lastpage*15,))
  download_thread.start()
  threads.append(download_thread)
  if(len(threads)>1):
    for t in threads:
      t.join()
      threads = []
