
from bs4 import BeautifulSoup
import requests

url = "https://www.cbssports.com/nfl/stats/"

def fetch_and_parse(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def extract_player_data(row):
    columns = row.find_all('td')
    return {
        'name': columns[0].text.strip(),
        'position': columns[1].text.strip(),
        'team': columns[2].text.strip(),
        'touchdowns': columns[3].text.strip()
    }

def get_football_stats():
    soup = fetch_and_parse(url)
    table = soup.find('table', class_='TableBase-table')
    
    players = [
        extract_player_data(row)
        for row in table.find_all('tr')[1:21]
        if row.find_all('td')
    ]
    
    for player in players:
        print(f"Player: {player['name']}, Position: {player['position']}, Team: {player['team']}, Touchdowns: {player['touchdowns']}")

if __name__ == "__main__":
    get_football_stats()




