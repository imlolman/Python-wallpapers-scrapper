import requests
import ntpath
import os 
from bs4 import BeautifulSoup as BS

def linkConverter(link,resolution):
  return link.replace("300x168",resolution)

def getData(url):
  r = requests.get(url)
  if(r.status_code == 200):
    return r.text

def download(link,foldername):
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
  # print("Downloaded: "+ name)
  return 1

def getFileName(link):
  return ntpath.basename(link)

def downloadAllFromPageLink(link,resolution,foldername):
  soup = BS(getData(link), 'html.parser')
  allWalls = soup.findAll("img", {"class": "wallpapers__image"})
  for wall in allWalls:
    mainLink = linkConverter(wall['src'],resolution)
    # print("Started Downloading: "+mainLink)
    download(mainLink,foldername)