import requests
import ntpath
import os 
import sys
from bs4 import BeautifulSoup as BS

downloaded_files = 0
total_files = 0
animation = "|/-\\"

def linkConverter(link,resolution):
  return link.replace("300x168",resolution)

def getData(url):
  r = requests.get(url)
  if(r.status_code == 200):
    return r.text

def download(link,foldername):
  global downloaded_files,total_files,animation
  name = getFileName(link)
  r = requests.get(link)
  foldertest = foldername
  if not (os.path.isdir(foldertest)):
    try:  
      os.mkdir(foldertest)
    except OSError:  
      print ("Creation of the directory "+foldername+" failed")
  with open(foldername+"/"+name,'wb') as f: 
    f.write(r.content)
  downloaded_files+=1
  sys.stdout.write("\r Downloading [" + "#"*int(((downloaded_files/total_files)*50)) + " "*int((((total_files-downloaded_files)/total_files)*50)) + "] " + str(downloaded_files) + "/" + str(total_files) + " Files.")
  sys.stdout.flush()
  return 1

def getFileName(link):
  return ntpath.basename(link)

def downloadAllFromPageLink(link,resolution,foldername,tf):
  global total_files
  total_files = tf
  soup = BS(getData(link), 'html.parser')
  allWalls = soup.findAll("img", {"class": "wallpapers__image"})
  for wall in allWalls:
    mainLink = linkConverter(wall['src'],resolution)
    download(mainLink,foldername)