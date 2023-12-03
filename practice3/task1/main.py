import json
from functools import reduce

with open('countries.json', 'r') as f:
    countries = json.load(f)

# С помощью `map()` создайте новый список, изменив сделав название каждой страны прописным в списке стран.
upper_bound_countries = list(map(lambda x: x.upper(), countries))
print(upper_bound_countries)

# С помощью `filter()`, чтобы отфильтровать страны, содержащие `'land'`.
land_countries = list(filter(lambda x: 'land' in x, countries))
print(land_countries)

# С помощью `filter()`, чтобы отфильтровать страны, содержащие ровно шесть символов.
countries_6length = list(filter(lambda x: len(x) == 6, countries))
print(countries_6length)

# С помощью `filter()`, чтобы отфильтровать страны, содержащие шесть и более букв в списке стран.
countries_more_6length = list(filter(lambda x: len(x) >= 6, countries))
print(countries_more_6length)

# С помощью `filter()` для отсеивания стран, начинающихся с буквы `'E'`.
countries_not_E = list(filter(lambda x: x[0] != 'E', countries))
print(countries_not_E)

# С помощью `reduce()` объедините все страны и получите данное предложение на английском языке: Финляндия, Швеция, Дания, Норвегия и Исландия являются странами Северной Европы.
north_europe = ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
north_europe_sentence = reduce(lambda x, y: x + ', ' + y, north_europe) + 'are countries of Northern Europe.'
print(north_europe_sentence)

# Решите предыдущие задачи, объединив две или более функций высшего порядка методов
countries_mixed_params = list(filter(lambda x: len(x) >= 6, filter(lambda x: 'land' in x, countries)))
print(countries_mixed_params)

# Используя сначала каррирование, а затем замыкания, объявите функцию `categorize_countries()`, которая возвращает список стран с некоторым общим шаблоном (например, `'land', 'ia', 'island', 'stan'`), который можно менять.
def categorize_countries(suffix):
    return lambda countries: list(filter(lambda x: suffix in x, countries))

countries_stan = categorize_countries('stan')(countries)
print(countries_stan)

countries_land = categorize_countries('land')(countries)
print(countries_land)

countries_island = categorize_countries('Island')(countries)
print(countries_island)
