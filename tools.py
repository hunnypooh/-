import requests
import csv
from bs4 import BeautifulSoup

def return_urls() :
  urls = []
  with open('./title_and_urls.xlsx', mode = 'r', encoding = "utf-8") as f:
    reader = csv.reader(f,delimiter = '\t')
    for txt in reader: 
      urls.append(txt[1])
    return urls[1:]
  

def extract_keywords(url) :
  url = requests.get(url)
  soup =  BeautifulSoup(url.text, "html.parser")
  title = soup.find("h3",{"class":"info_title_wrap"}).string

  keywords = []
  ul = soup.select_one('ul.keyword_list')
  lists = ul.select('li > button > span')
  for list in lists:
    keywords.append(list.get_text()[1:])
  
  return {
  'title' : title,
  'keywords' : keywords
  }

def make_title_and_keywords_list() : 
  title_and_keywords = []
  urls = return_urls()
  for url in urls :
    keywords = extract_keywords(url)
    title_and_keywords.append(keywords)
  return title_and_keywords