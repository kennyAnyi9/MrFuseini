import requests
from bs4 import BeautifulSoup

# Send request and parse HTML
#this will print the status code 
# html_text = requests.get('https://books.toscrape.com/')
# print(html_text)

#This would print the html
html_text = requests.get('https://books.toscrape.com/').text
#print(html_text)

#parse html to BeautifulSoup object with lxml parser
soup = BeautifulSoup(html_text, 'lxml')
# print(soup)

# heading = soup.find('div', class_='page_inner')
# # print(heading.prettify())

# heading_text = heading.a.text
# link = heading.a.get('href')
# print(f'''
#       Heading: {heading_text}
#       Link: {link}
#       ''')


books_container = soup.find('section')
# print(books_container)
book_list = books_container.find('ol', class_='row')
#the findall method would find all the tagsin question and put them in a single list
books = book_list.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')


#here we iterate over the list in books variable and print the results
# the interation variable is not really necessary but i just used it to count the number of iterations for the looping to be sure we scrapped all the data.
iteration =0
for book in books:
    title = book.h3.text
    price = book.find('div', class_='product_price').p.text
    print(f'{title}, {price}')
    iteration += 1
print(iteration)
    






    