from selenium.webdriver import Firefox
import sys, time

site = "https://google.com/search?q=thing"

browser = Firefox()

browser.get(site)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
browser.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
time.sleep(10)
browser.close()
