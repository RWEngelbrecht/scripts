import requests, sys, re
from bs4 import BeautifulSoup
from csv import writer

if len(sys.argv) < 2:
	sys.exit('Enter a movie you\'d like to look up...')
elif len(sys.argv) > 2:
	title = " ".join(sys.argv[1:]).title()
	searchTitle = "+".join(sys.argv[1:])
elif len(sys.argv) == 2:
	title = sys.argv[1].title()
	searchTitle = re.sub("\s+", "+", sys.argv[1])


search = requests.get('https://www.themoviedb.org/search/movie?query='+searchTitle)

soup = BeautifulSoup(search.text, 'html.parser')

searchResults = soup.find(class_='flex').find(class_='title result')['href']

moviePage = requests.get('https://www.themoviedb.org'+searchResults)

gloup = BeautifulSoup(moviePage.text, 'html.parser')

genres = []
getGenre = gloup.find(class_='genres').findAll('li')

releaseDate = gloup.find(class_='release_date').getText()

director = gloup.find('ol').find('li').find('a').getText()

facts = gloup.find(class_='facts').findAll('p')
for fact in facts:
	factChildren = fact.findChildren('strong')
	for child in factChildren:
		if child.getText() == "Runtime":
			releaseDate = fact.getText()[8:]

for genre in getGenre:
	genres.append(genre.getText())

print(
"""Title:		"""+title+"""
Released:	"""+releaseDate+"""
Director:	"""+director+"""
Genres:		"""+", ".join(genres)
)
