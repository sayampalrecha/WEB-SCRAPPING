# made by SAYAM Palrecha 
#  this is the code to easily scrap out all the information or data from a website!!
#  Importing the library
 
import requests
import bs4

# getting the URL
# Just paste the URL you want in the .get('')
result  = requests.get("https://en.wikipedia.org/wiki/Narendra_Modi")

soup = bs4.BeautifulSoup(result.text,"lxml")


for item in soup.select('.toctext'):
    print(item.text)