import requests
from bs4 import BeautifulSoup  as BS

url = "http://localhost:9000/docs"

# Collect the web page content
page = requests.get(url)

# Publish the web page in  beautiful soup
soup = BS(page.text, 'html.parser')

# Print the scripts included in the web page
for script in soup.find_all('script'):
    print(f"- {script}")
