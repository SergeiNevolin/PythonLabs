import json
import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from deep_translator import GoogleTranslator

def retrieve_airports_data():
    airports_info = {}
    
    def generate_letter_url(letter):
        return f"https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_{letter}"

    def extract_airport_details(row):
        cells = row.find_all("td")
        if len(cells) > 1:
            code = cells[0].text.strip()
            name = cells[2].text.strip()
            return code, name
        return None, None

    for letter_code in range(65, 91):
        letter_url = generate_letter_url(chr(letter_code))
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(letter_url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        table = soup.find("table", {"class": "wikitable sortable"})
        rows = table.find_all("tr")[1:]

        for row in rows:
            code, name = extract_airport_details(row)
            if code and name:
                airports_info[code] = name

    return airports_info

def translate_airport_name_to_english(airport_name):
    translated_name = GoogleTranslator(source='auto', target='en').translate(airport_name)
    return translated_name.lower()

def find_airport_code_by_name(airports_info, target_airport_name):
    target_airport_name_en = translate_airport_name_to_english(target_airport_name)
    
    for code, name in airports_info.items():
        if fuzz.ratio(name.lower(), target_airport_name_en) >= 80:
            return code
    
    return "Airport not found"

if __name__ == "__main__":
    airports_info = retrieve_airports_data()

    with open("airports.json", "w") as output_file:
        json.dump(airports_info, output_file, indent=4)

    target_airport_name = 'Аэропорт Внуково'
    airport_code = find_airport_code_by_name(airports_info, target_airport_name)
    print(f"Код: {airport_code} (Аэропорт: {target_airport_name})")

    target_airport_name = 'Perth Airport'
    airport_code = find_airport_code_by_name(airports_info, target_airport_name)
    print(f"Код: {airport_code} (Аэропорт: {target_airport_name})")
