import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from googletrans import Translator
import googletrans
import pandas as pd

urlConcepts = 'https://www.geeksforgeeks.org/search-algorithms-in-ai/'

response = requests.get(urlConcepts)
soup = BeautifulSoup(response.content, 'html.parser')

h3_elements = soup.find_all('h3')
imgs = soup.find_all('img', alt=['DFS ques', 'DFS soln', 'BFS ques', 'BFS solution', 'greedy algo ques', 'greedy solution'])

dfs = 'Depth First Search:'
bfs = 'Breadth First Search:'

def translate(text_list):
    x = Translator()
    translatedText = x.translate(text_list, dest = 'pt')
    return translatedText
    
def depth(text):
    for i in h3_elements:
        if(i.text == dfs):
            return i.next_sibling.text

def breadth(text):
    for i in h3_elements:
        if(i.text == bfs):
            return i.next_sibling.text

def heuristic():
    for i in h3_elements:
        if(i.text == 'Greedy Search:'):
            return i.previous_sibling.text
        
def greedy():
    target = soup.find('h3', text='Greedy Search:')
    if target:
        nextp = target.find_next_siblings('p', limit=3)
        combinedtag = ""
        for tag in nextp:
            combinedtag += tag.get_text() + ""
    return combinedtag.strip()
            

        

dfs_text = depth(dfs)
bfs_text = breadth(bfs)
heuristic_text = heuristic()
greedy_text = greedy()

translated_dfs = translate(dfs_text)
translated_bfs = translate(bfs_text)
translated_heuristic = translate(heuristic_text)
translated_greedy = translate(greedy_text)

image_links = [img['src'] for img in imgs if 'src' in img.attrs]
df_images = pd.DataFrame(image_links)

data = {
    'Título': [dfs, bfs, 'Search Heuristics:', 'Greedy Search:'],
    'Conteúdo EN': [dfs_text, bfs_text, heuristic_text, greedy_text],
    'Conteúdo Traduzido': [translated_dfs.text, translated_bfs.text, translated_heuristic.text, translated_greedy.text]
}
df_concepts = pd.DataFrame(data)


with pd.ExcelWriter('data.xlsx') as writer:
    df_concepts.to_excel(writer, sheet_name='Concepts', index=False)
    df_images.to_excel(writer, sheet_name='Images', index=False)

# Salvar o DataFrame em um arquivo Excel
#df.to_excel('data.xlsx', index=False, sheet_name='Concepts')
