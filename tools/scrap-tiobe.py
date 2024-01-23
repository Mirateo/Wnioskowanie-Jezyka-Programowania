import requests
from bs4 import BeautifulSoup

def scrape_tiobe_index():
    url = "https://www.tiobe.com/tiobe-index/"
    response = requests.get(url)
    popularity = {}
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        language_rows = soup.select('.table-top20 tr')
        for row in language_rows[1:]:  # Skip the header row
            columns = row.select('td')
            if len(columns) >= 3:  # Ensure there are enough columns
                language_name = columns[4].text.strip()
                language_rating = (float)(columns[5].text.strip()[:-1])/1.397
                popularity[language_name] = language_rating
            else:
                print("Unexpected table structure. Check the HTML structure.")
    else:
        print(f"Failed to retrieve the TIOBE index. Status Code: {response.status_code}")
        
    print(popularity)

if __name__ == "__main__":
    scrape_tiobe_index()