
import re
import os

def my_search(Path, text, find):
    Path = input("enter file path: ")
    with open(Path, 'r') as text:
        os.path(text.read())
    find = input('which word are you looking for?: ')

    for words, in text:
        re.search(text, words)
        if words in find:
            number_of_words = text.count(find)
            return f"{find.format(words)}, {number_of_words} search results."
                
        
    
print(my_search('Path', 'text', 'find'))

