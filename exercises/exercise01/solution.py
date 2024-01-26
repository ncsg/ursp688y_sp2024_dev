types = {}
cities = {}
for id, request in service_requests.items():
    for key, value in request.items():
        if key == 'Description':
            if value not in types:
                types[value] = 0
            types[value] = types[value] + 1
        elif key == 'City':
            if value not in cities:
                cities[value] = 0
            cities[value] = cities[value] + 1