import requests 
import bs4

req = requests.get("https://en.wikipedia.org/wiki/Google")
soup = bs4.BeautifulSoup(req.text,'lxml')

soup.select('.image')[1]
