"""
	TODO:
		# If -ta or -takealot is specified, only use takealot.com
		# Implement amazon scraping
		# Implement flags for amazon
		# Implement category filtering?
		# limit per site result
		# sorting
"""

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

def find_result(site_key, driver):
	if site_key is 'ta':
		return ta_find_result(driver)
	elif site_key is 'fb':
		return fb_find_result(driver)

def ta_find_result(driver):
	resultDiv = driver.find_element_by_class_name('listings-container').find_element_by_class_name('grid-layout')
	resultList = resultDiv.find_elements_by_class_name('search-product')
	# resultLinks = [{'link': elem.get_attribute('href')} for elem in resultList]
	return list(map(
		lambda elem: {
			'title': elem.find_element_by_class_name('product-title').find_element_by_tag_name('span').text, # empty after couple elements?
			'link': elem.find_element_by_tag_name('a').get_attribute('href'),
			'price': elem.find_element_by_class_name('price').find_element_by_tag_name('span').text # empty after couple elements?
			}, resultList[:10]))

def fb_find_result(driver):
	resultDivXpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[1]/div[2]'
	resultDiv = driver.find_element_by_xpath(resultDivXpath)
	resultList = resultDiv.find_elements_by_class_name('sonix8o1')
	return [
		{
			'title': elem.find_element_by_xpath(resultDivXpath+'/div[1]/div/span/div/div/a/div/div[2]/div[2]/span/div/span/span').text,
			'link': elem.find_element_by_tag_name('a').get_attribute('href'),
			'price': elem.find_element_by_class_name('d2edcug0').text
		} for elem in resultList[:10] if elem.find_element_by_class_name('d2edcug0').text is not 'Sold'
	]

def get_urls_from_flag(args):
	possible_sites = [
		('ta', 'https://www.takealot.com/all?qsearch='),
		('fb', 'https://www.facebook.com/marketplace/search/?query=')
	]
	if '-ta' in args or '-takealot' in args:
		return [possible_sites[0]]
	elif '-fb' in args or '-facebook' in args:
		return [possible_sites[1]]
	return possible_sites


browser = get_driver("Firefox")
browser.implicitly_wait(20) # polls DOM for 10s when trying to find element(s)
# browser.get('https://www.takealot.com/')


if __name__ == '__main__':
	try:
		urls = get_urls_from_flag(sys.argv[1:])
		query = [arg for arg in sys.argv[1:] if not re.match(r'[-*?]',arg)]
		searchThings = "+".join(query)
		# searchElement = ta_find_search_bar(browser)	|
		# search(searchThings, searchElement)			|-> when you need to search something else, i guess?
		results = {}
		for url in urls:
			browser.get(url[1]+searchThings)
			results[url[0]] = find_result(url[0], browser)
		print(results)
		# browser.get('https://www.takealot.com/all?qsearch='+searchThings)
		# print(ta_find_result(browser))
	except:
		print("something (or someone) fucked up...")
		traceback.print_exc()
	finally:
		browser.quit()
