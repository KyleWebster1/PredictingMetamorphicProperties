# Scrape the first webpage
# "https://dst.lbl.gov/ACSSoftware/colt/api/cern/jet/stat/Descriptive.html"

# Links to sites
website1 = "https://dst.lbl.gov/ACSSoftware/colt/api/cern/jet/stat/Descriptive.html"

# Import
import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib.request
import time

# Get web info for first site
response = requests.get(website1)

# Parse response
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())
# for tr in soup.find_all('tr'):
#     if tr["bgcolor"] == "white":
#         print(tr)