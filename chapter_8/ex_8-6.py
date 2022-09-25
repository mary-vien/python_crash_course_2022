def get_city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    city_country = city + ', ' + country
    return city_country.title()

cities = get_city_country('kyiv', 'ukraine')
print(cities)

cities = get_city_country('warsaw', 'poland')
print(cities)

cities = get_city_country('oslo', 'norway')
print(cities)