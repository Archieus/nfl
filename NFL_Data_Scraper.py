import urllib.request, urllib.error
import ssl
from bs4 import BeautifulSoup, Comment
from urllib.request import urlopen

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.pro-football-reference.com'
year = input("Enter Stat Year: ")

html = urllib.request.urlopen(url + '/years/'+ str(year) +'/#all_team_stats').read()

soup = BeautifulSoup(html, 'html.parser')

# lambda expression formula: text=lambda t: isinstance(t, Commment)) looking for Comments.
table = soup.select_one("#all_team_stats").find_next(text=lambda t: isinstance(t, Comment))
table = BeautifulSoup(table, 'html.parser')

#print(table)
# loop results of the table into an array
for tr in table.select('tr'):
    tds = [td.get_text(strip=True) for td in tr.select('td')]
    print(*tds)
