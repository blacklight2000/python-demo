""" Selenium Test Case """


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('http://python.org')
elem = browser.find_element_by_css_selector("#id-search-field")
elem.send_keys("pyconnards")
elem.send_keys(Keys.RETURN)
assert "No results found." in browser.page_source
