import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.geeksforgeeks.org/search-algorithms-in-ai/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

h3_elements = soup.find_all('h3')
dfs = 'Depth First Search:'
bfs = 'Breadth First Search:'


def depth(text):
    for i in h3_elements:
        if(i.text == dfs):
            print(i.next_sibling.text)

def breadth(text):
    for i in h3_elements:
        if(i.text == bfs):
            print(i.next_sibling.text)


depth(dfs)
print()
breadth(bfs)
