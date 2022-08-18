"""
スクレイピング
会社案内を抜粋
"""

import urllib.request
from bs4 import BeautifulSoup

req  = urllib.request.urlopen('http://quality-start.in/company/')
soup = BeautifulSoup(req, "html.parser")
print ( soup.find('span', class_="u-display-block site-description under-logo").text )
