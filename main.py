
import requests
from bs4 import BeautifulSoup

response = requests.get('https://pypi.org/simple/')
soup = BeautifulSoup(response.text, 'html.parser')

with open("demo.py", "a") as myfile:
    for a in soup.find_all('a'):
        print(a.contents[0])
        myfile.write("import " + a.contents[0] + "\n")
