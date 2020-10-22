####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: lecture notes
# description: Section 15 - Web Scraping
# other: N/A
####################################

# RULES
# 1. always try to get permission before scraping, otherwise I might be blocked
# 2. check the laws of whatever country we are operating in (for legal issues)

# LIMITATIONS
# each website is unique -> so for each website there must exist a Python script
# an update to a website might brake my script

import requests
import bs4

# Grabbing a title
result = requests.get("http://example.com")

type(result)
result.text

# bs with lxml tranforms the previous raw html into the following
soup = bs4.BeautifulSoup(result.text,'lxml')
soup

# returns the tag we specified as a list (i.e., there might be more than one)
soup.select('title')
soup.select('title')[0].getText()
soup.select('p')
site_paragraphs = soup.select('p')
type(site_paragraphs[0])  # not a string, instead is a specialized bs object,
                          # which is why we can do something like call .getText()

# Grabbing a class (from CSS) using soup.select()
# 'div'         : all elements with 'div' tag
# '#some_id'    : elements containing id='some_id'
# '.some_class' : elements containing class='some_class'
# 'div span'    : any element named span within a div element
# 'div > span'  : any element named span directly within a div element, with
#                 nothing in between

res = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")
soup = bs4.BeautifulSoup(res.text,'lxml')

soup.select('.toctext')[0].text
soup.select('.toctext')[0].getText()

for item in soup.select('.toctext'):
    print(item.text)

# Grabbing an image
#soup.select('img')  # can return more than what is needeed (it will depend on
#                      the website)
soup.select('.thumbimage')
jonas_salk = soup.select('.thumbimage')[0]
jonas_salk['src']  # we can treat it as a dictionary

image_link = requests.get('http://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Roosevelt_OConnor.jpg/220px-Roosevelt_OConnor.jpg')
#image_link.content  # raw content of the image which is a binary file

#make sure to use the same format that the image has
f = open('my_image_image.jpg','wb')  # wb means write binary
f.write(image_link.content)
f.close()

# Multiple elements across multiple pages
# GOAL: get title of every book with a 2 star rating

#Check that this also work with page 1
#http://books.toscrape.com/catalogue/page-2.html

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

req = requests.get(base_url.format(1))

soup = bs4.BeautifulSoup(req.text,'lxml')

products = soup.select(".product_pod")  # always check the length, in this case should be 20

example = products[0]

# one way (not useful everytime)
'star-rating Two' in str(example)

# another way (checking for the presence of a class)
example.select('.star-rating.Three')  # if there is a space in a class we should add a dot
example.select('.star-rating.Two')  # nothing
example.select('a')[1]['title']

two_star_titles = []

for n in range(1,51):

    scrape_url = base_url.format(n)
    req = requests.get(base_url.format(1))
    soup = bs4.BeautifulSoup(req.text,'lxml')
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])

two_star_titles
