# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re, os
# import pandas as pd

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Document</title>
</head>
<body>
	<div id="section-1">
		<h3 data-hello="hi">Hello</h3>
		<img src="https://images.unsplash.com/photo-1578932219015-3b27be0dbdf8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=675&q=80" />
		<p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fuga, quas praesentium saepe aspernatur rerum qui. Maxime error ad et officia quidem cum, fuga reiciendis sint illum, ipsum nesciunt dolore hic.</p>
	</div>
	<div id="section-2">
		<ul class="items">
			<li class="item"><a href="#">Item1</a></li>
			<li class="item"><a href="#">Item2</a></li>
			<li class="item"><a href="#">Item3</a></li>
			<li class="item"><a href="#">Item4</a></li>
		</ul>
	</div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')


### DIRECTLY ACCESS ELEMENTS
# print(soup.head)
# print(soup.body)
# print(soup.head.title)

### USING find()
elem = soup.find('div')  ## Returns first element found

### USING find_all()/findAll()
elem = soup.findAll('div')  ## Returns list of elements found

### FINDING BY ID/CLASS
elem = soup.find(id='section-2')
elem = soup.find(class_='items')   ## Class is reserved keyword, append underscore

### FINDING BY ATTRIBUTES
elem = soup.find(attrs={"data-hello":"hi"})

### USING select()
elem = soup.select('#section-1')  ## Returns list of elements selected, # for id, . for class
elem = soup.select('#section-1')[0]

### USING get_text()
elem = soup.find(class_='item').get_text()  ## Returns text enclosed in element
	## Example of looping
	# for item in soup.select('.items'):
	# 	print(item.get_text())

### Navigation
elem = soup.body.contents[0].find_next_sibling()
elem = soup.find(id='section-2').find_previous_sibling() ## Returns section-1 div
elem = soup.find(class_='item').find_parent()
elem = soup.find('h3').find_next_sibling('p')

print(elem)
