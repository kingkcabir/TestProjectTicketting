
import requests
from bs4 import BeautifulSoup
import re
from nltk.stem import PorterStemmer

# Step 1: Web Scraping
def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        return None

# Step 2: Data Indexing
def index_words(soup):
    index = {}
    words = re.findall(r'\w+', soup.get_text())
    for word in words:
        word = word.lower()
        if word in index:
            index[word] += 1
        else:
            index[word] = 1
    return index

# Step 3: Text Processing
def remove_stop_words(index):
    stop_words = {'a', 'an', 'the', 'and', 'or', 'in', 'on', 'at'}
    for stop_word in stop_words:
        if stop_word in index:
            del index[stop_word]
    return index

def apply_stemming(index):
    stemmer = PorterStemmer()
    stemmed_index = {}
    for word, count in index.items():
        stemmed_word = stemmer.stem(word)
        if stemmed_word in stemmed_index:
            stemmed_index[stemmed_word] += count
        else:
            stemmed_index[stemmed_word] = count
    return stemmed_index

# Step 4: Search Function
def search(query, index):
    query_words = re.findall(r'\w+', query.lower())
    results = {}
    for word in query_words:
        if word in index:
            results[word] = index[word]
    return results

# Example usage
if __name__ == "__main__":
    url = "https://google.com"
    soup = fetch_page(url)
    if soup:
        indexed_words = index_words(soup)
        cleaned_index = remove_stop_words(indexed_words)
        stemmed_index = apply_stemming(cleaned_index)
        query = "python tutorial"
        search_results = search(query, stemmed_index)
        print(f"Search results for '{query}': {search_results}")