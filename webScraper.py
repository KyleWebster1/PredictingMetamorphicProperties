# Scrape the first webpage

# Links to site
# Colt
website1 = "https://dst.lbl.gov/ACSSoftware/colt/api/cern/jet/stat/Descriptive.html"

# Import
from bs4 import BeautifulSoup
import requests
import urllib.request
import re

# Get web info for first site
response = requests.get(website1)

# Function for parsing information from tr tag for first database
def parseTRtag(tag):
    # List of attributes in order of; name, return type, input types, desc text
    # Get td tags from tr
    tds = tag.find_all('td')
    # Get text from first td tag
    returnType = tds[0].getText()
    returnType = returnType.split("\xa0")[1]

    # Separate second table entry into fields
    desc = tds[1].getText()
    desc = re.sub("\n|\t", "", desc)
    separateNameandDesc = desc.split(")", 1)
    # Get function name
    separateName = separateNameandDesc[0].split("(")
    name = separateName[0]

    # Get input types
    inputTypes = separateName[1]
    inputTypes = inputTypes.split(",")
    for i in range(0,len(inputTypes)):
        temp = inputTypes[i].strip()
        temp = re.sub("\xa0", " ", temp)
        inputTypes[i] = temp.split(" ")[0]
    inputTypes = ",".join(inputTypes)

    # Get description text
    text = separateNameandDesc[1]
    text = text.strip()

    # Return values
    return([name, returnType, inputTypes, text])


# Parse response
# Create soup object
soup = BeautifulSoup(response.text, "html.parser")
# Get the 3rd table, has all information inside
table = soup.find_all('table')[2]
# Find all the tr tags
tr = table.find_all("tr")

# List of attributes for each entry
attributes = []

# Loop through all tr tags
for tri in tr:
    # Get color of current tr tag
    bgcolor = tri['bgcolor']
    # If white parse
    if bgcolor == 'white':
        attributes.append(parseTRtag(tri))

# for i in range(0,5):
#     print(attributes[i])

# Print to a file
outputFile = open("coltAttributes.txt", "w")
for attribute in attributes:
    outputFile.write("|".join(attribute))
    outputFile.write("\n")
outputFile.close()

# Scrape second site
# Visit each set of links
toVisit = [
    "https://mahout.apache.org/docs/0.13.0/api/docs/mahout-integration/overview-summary.html",
    "https://mahout.apache.org/docs/0.13.0/api/docs/mahout-math/overview-summary.html",
    "https://mahout.apache.org/docs/0.13.0/api/docs/mahout-mr/overview-summary.html"
]

for link in toVisit:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")

    divs = soup.find_all("div")
    table = None
    for div in divs:
        # Get the table with the links in it
        try:
            if div['class'] == ['contentContainer']:
                table = div.find("table")
        except:
            pass
    # Get the table bodies
    bodies = table.find('tbody')
    # Get table data
    tds = bodies.find_all('td')
    print(tds[0])
    break