import requests
from bs4 import BeautifulSoup
from csv import writer

search = requests.get('https://www.themoviedb.org/search/movie?query=Akira')

soup = BeautifulSoup(search.text, 'html.parser')

searchResults = soup.find(class_='flex').find(class_='title result')['href']

moviePage = requests.get('https://www.themoviedb.org'+searchResults)

soup = BeautifulSoup(moviePage.text, 'html.parser')

genres = []
getGenre = soup.find(class_='genres').findAll('li')
for genre in getGenre:
	genres.append(genre.getText())

print(genres)
