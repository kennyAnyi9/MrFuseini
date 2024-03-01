import requests
from bs4 import BeautifulSoup





# Send request and parse HTML
#this will print the status code 
# html_text = requests.get('https://books.toscrape.com/')
# print(html_text)

html_text = requests.get('https://books.toscrape.com/').text
#print(html_text)

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
books = book_list.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

iteration =0
for book in books:
    title = book.h3.text
    price = book.find('div', class_='product_price').p.text
    print(f'{title}, {price}')
    iteration += 1
print(iteration)
    







# iteration =0
# main_container = soup.find('div', class_="hugo4-pc-pagex-root")
# product_container=main_container.find('div', class_="product-water-fall")
# product_sub_container=product_container.find('div', class_="hugo4-pc-grid hugo4-pc-grid-5 hugo4-pc-grid-list hugo4-pc-grid-waterfall")

# #trying to scrape all waterfall divs
# all_waterfall_divs = product_sub_container.find_all('div', class_="waterfall-column")
# print(all_waterfall_divs)
    