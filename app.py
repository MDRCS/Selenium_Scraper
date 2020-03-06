from selenium import webdriver
from pages.quotes_page import QuotesPage,InvalidAuthorTagError

try:

    chrome = webdriver.Chrome(executable_path="/Applications/chromedriver")
    chrome.get('http://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)

    author = input('Enter a valid author name please ..')
    tag = input('Enter a valid tag name please ..')

    print(page.search_quotes(author,tag))

except InvalidAuthorTagError as e:
    print(e)
except Exception as e:
    print(e)
    print('An unknown error occured please try again')


# tags = page.get_available_tags() #Snippet code to print all tags
# print("select one of these tags [{}]".format(" | ".join(tags)))


