import requests
import json

def fetch_corporates_data(query):
    url = 'https://ranking.glassdollar.com/graphql'
    response = requests.post(url, json={'query': query})

    if response.status_code == 200:
        result = response.json()
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None

    data = []
    for corporate in result['data']['topRankedCorporates']:
        themes = set()
        for partner in corporate['startup_partners']:
            themes.update(partner['theme_gd'].split(', '))
        corporate['startup_themes'] = list(themes)
        data.append(corporate)

    return data
