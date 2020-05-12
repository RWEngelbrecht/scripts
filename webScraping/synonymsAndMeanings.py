# Written so I don't have to open browser myself or leave terminal to
# look for word definitions/synonyms, so works on mac (maybe ubuntu)
# and Firefox only. Needs selenium installed, using geckodriver.
#
# Works by running > python3 synonymsAndMeanings.py synonym 'word'
# 				or > python3 synonymsAndMeanings.py define 'word'
# or set up aliases

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys

def lookUpWord(driver, command, word):
	if command == "synonym":
		driver.get("https://www.thesaurus.com/browse/"+word)
	elif command == "define":
		driver.get("https://www.dictionary.com/browse/"+word)
	else:
		print("Something went horribly wrong...\nYou probably didn't give me a word")
		driver.quit()

# use -q to execute phantomSearch, scrape synonyms/definition, print to stdout
def phantomSearch(driver, command, word, flags):
	if "-q" in flags:
		print("command == "+command)
		if command == "synonym":
			driver.get("https://www.thesaurus.com/browse/"+word)
			synonymList = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/main/section/section/div[2]/ul")
			synonymItems = synonymList.find_elements_by_tag_name("li")
			for synonymItem in synonymItems:
				print(synonymItem.text)
			driver.quit()
		elif command == "define":
			definitions = []
			driver.get("https://www.dictionary.com/browse/"+word)
			definitionBlock = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/main/section/section/div[1]/section[2]")
			definitionItems = definitionBlock.find_elements_by_tag_name("div")
			for i in range (0, len(definitionItems)):#definitionItem in definitionItems:
				if len(definitionItems[i].find_element_by_tag_name("span").text) > 0:
					definitions.append(
						str(i + 1) + '. ' +
						definitionItems[i].find_element_by_tag_name("span").text
						)
			driver.quit()
			for definition in definitions:
				print(definition)

capabilities = DesiredCapabilities().FIREFOX
capabilities["pageLoadStrategy"] = "eager"

if len(sys.argv) == 3 and (sys.argv[1] == "synonym" or sys.argv[1] == "define"):
	driver = webdriver.Firefox(capabilities=capabilities)
	lookUpWord(driver, sys.argv[1], sys.argv[2])
elif len(sys.argv) > 3 and (sys.argv[1] == "synonym" or sys.argv[1] == "define"):
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(capabilities=capabilities, options=options)
	phantomSearch(driver, sys.argv[1], sys.argv[2], sys.argv[3:])
else:
	print("You used it wrong, dumbass!")
