import pandas as pd
import requests

base_url = "https://openlibrary.org/search.json"

def get_author(author):
    url = f'{base_url}?author={author}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")

chosen_author = input("Which author would you like to search for? ")
chosen_author_info = get_author(chosen_author)

print(f'{chosen_author} has ', chosen_author_info['numFound'], ' works!')




