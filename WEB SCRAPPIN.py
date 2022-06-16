#  this iss the code to easily scrap out all the information or data from a website!!
#  Importing the library
import requests
import bs4

# getting the URL
result  = requests.get("https://en.wikipedia.org/wiki/Narendra_Modi")
# this gives you all the text in the webpage in the form of a long string
print(result.text)

#  to make the code more readable we use the bs4 library
soup = bs4.BeautifulSoup(result.text,"lxml")
print(soup)