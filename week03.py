def duplicate_city(cities):
    result_city = []
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2:
            result_city.append(city)
    return result_city

cities = ['Incheon', 'Seoul', 'Incheon', 'Incheon', 'Gwangju']

cities.append('Incheon')
cities.append('Seoul')
cities.append('Suwon')
print(cities)
print(set(duplicate_city(cities)))