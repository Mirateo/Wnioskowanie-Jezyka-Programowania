"""
======================= START OF LICENSE NOTICE =======================
  Copyright (C) 2024 Mateusz Murawski. All Rights Reserved
======================== END OF LICENSE NOTICE ========================
"""
import requests
from bs4 import BeautifulSoup

"""
scrapTiobeIndex function.

This function scrapes the TIOBE index website to retrieve the popularity ratings of programming languages.
"""
def scrapTiobeIndex():
    url = "https://www.tiobe.com/tiobe-index/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        language_rows = soup.select('.table-top20 tr')
        popularity = {}
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


if __name__ == "__main__":
    scrapTiobeIndex()