# Dict comprehensions.
cities = ["mumbai", "new york", "paris"]
countries = ["india", "usa", "france"]

z = zip(cities, countries)

dic = {city:country for city, country in z if city.startswith("m")}