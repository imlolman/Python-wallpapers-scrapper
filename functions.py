import requests
import ntpath
from bs4 import BeautifulSoup as BS
import threading

def linkConverter(link):
  return link.replace("300x168","1920x1080")

def getData(url):
  r = requests.get(url)
  if(r.status_code == 200):
    return r.text

def download(link):
  name = getFileName(link)
  r = requests.get(link)
  with open("downloaded/"+name,'wb') as f: 
    f.write(r.content)
  print("Downloaded: "+ name)
  return 1

def getFileName(link):
  return ntpath.basename(link)

def downloadAllFromPageLink(link):
  soup = BS(getData(link), 'html.parser')
  allWalls = soup.findAll("img", {"class": "wallpapers__image"})
  for wall in allWalls:
    mainLink = linkConverter(wall['src'])
    print("Started Downloading: "+mainLink)
    download(mainLink)