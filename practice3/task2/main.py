import json
from collections import Counter

with open('countries-data.json', 'r') as f:
    countries = json.load(f)

def print_countries(countries):
    print('\n'.join([f"{country['name']}: cap= {country['capital']}, pop= {country['population']}" for country in countries]))
    print('\n')

# Отсортировать страны: по названию
country_sorted_by_name = sorted(countries, key=lambda x: x['name'])
print_countries(country_sorted_by_name)

# Отсортировать страны: по столице
country_sorted_by_capital = sorted(countries, key=lambda x: x['capital'])
print_countries(country_sorted_by_capital)

# Отсортировать страны: по численности населения
country_sorted_by_population = sorted(countries, key=lambda x: x['population'])
print_countries(country_sorted_by_population)

# Выявить произвольное число (начать с 10) наиболее распространенных языков и где их используют.
languages = Counter(language for country in countries for language in country['languages'])
most_languages = languages.most_common(10)
print('\n'.join([f"language: {language}, count = {count}" for language, count in most_languages]))

# Выявить произвольное число (начать с 10) наиболее населенных стран.
most_populated = sorted(countries, key=lambda x: x['population'], reverse=True)[:10]
print_countries(most_populated)