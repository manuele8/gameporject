import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

# path to the firefox binary inside the Tor package
binary = r'C:\Users\manue\OneDrive\Desktop\Tor Browser\Browser/firefox'
firefox_binary = FirefoxBinary(binary)
PATH = 'C:\Program Files (x86)\geckodriver.exe'

browser = None


def get_browser(binary=None):
    global browser
    # only one instance of a browser opens, remove global for multiple instances
    if not browser:
        browser = webdriver.Firefox(firefox_binary=binary, executable_path=PATH)
    return browser


if __name__ == "__main__":
    browser = get_browser(binary=firefox_binary)
    urls = (
        ('tor browser check', 'https://check.torproject.org/'),
        ('ip checker', 'http://icanhazip.com')
    )
    for url_name, url in urls:
        print("getting", url_name, "at", url)
        browser.get(url)
