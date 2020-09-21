from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, re, traceback, time

def get_driver(browser):
	options = Options()
	options.headless = True
	capabilities = DesiredCapabilities().FIREFOX
	# capabilities["pageLoadStrategy"] = "eager"
	if browser == 'Firefox':
		return webdriver.Firefox(options=options, capabilities=capabilities)

def ta_find_search_bar(driver):
	return driver.find_element_by_xpath('/html/body/div[1]/header/div/div/div[2]/form/div/div[1]/input')

def search(query, search_element):
	search_element.send_keys(query)
	search_element.send_keys(Keys.RETURN)

def ta_find_result(driver):
	resultDiv = driver.find_element_by_class_name('listings-container').find_element_by_class_name('grid-layout')
	resultList = resultDiv.find_elements_by_class_name('search-product')
	# resultLinks = [{'link': elem.get_attribute('href')} for elem in resultList]
	return list(map(
		lambda elem: {
			'title': elem.find_element_by_class_name('product-title').find_element_by_tag_name('span').text,
			'link': elem.find_element_by_tag_name('a').get_attribute('href'),
			'price': elem.find_element_by_class_name('price').find_element_by_tag_name('span').text
			}, resultList))


browser = get_driver("Firefox")
browser.implicitly_wait(10) # polls DOM for 10s when trying to find element(s)
# browser.get('https://www.takealot.com/')

try:
	searchThings = "+".join(sys.argv[1:])
	# searchElement = ta_find_search_bar(browser)	|
	# search(searchThings, searchElement)			|-> when you need to search something else, i guess?
	browser.get('https://www.takealot.com/all?qsearch='+searchThings)
	print(ta_find_result(browser))
except:
	print("something (or someone) fucked up...")
	traceback.print_exc()
finally:
	browser.quit()
