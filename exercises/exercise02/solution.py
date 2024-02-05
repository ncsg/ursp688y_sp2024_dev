def count_unique_values(service_requests, label):
    uniques = {}
    for id, request in service_requests.items():
        for key, value in request.items():
            if key == label:
                if value not in uniques:
                    uniques[value] = 0
                uniques[value] = uniques[value] + 1
    return uniques

def count_unique_descriptions(service_requests):
    return count_unique_values(service_requests, 'Description')

def count_unique_cities(service_requests):
    return count_unique_values(service_requests, 'City')

count_unique_descriptions(service_requests)

count_unique_cities(service_requests)