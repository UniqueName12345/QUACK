import requests
import selenium

"""
WADDLE - Web Automation & Data Delivery, DuckDuckGo Lookup Engine
"""

class Waddle:
    def __init__(self):
        pass

    def turn_query_into_url(self, query):
        return "https://duckduckgo.com/html/?q=" + query
    
    def scrape_results(self, url):
        driver = selenium.webdriver.Firefox()
        driver.get(url)
        results = driver.find_element_by_id("serp__results").text
        driver.quit()
        return results