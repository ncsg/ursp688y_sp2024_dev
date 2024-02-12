# Pseudocode
# For Part 1 - General code that solves the questions.

# Step 1. Create a new one-dimensional tracker list that will take each service
# request type from the service_requests dictionary
# Step 2. Iterate through each individual service request from the dictionary,
# and add the type of request to the new list.
# Step 3. Use the Counter function to both tally and find the most common
# service request type.

# For Question 2
# Same process but change the variable being counted from request type to city.

# Attempt 1, A separate function for both the type and location of requests.
# This method does not take any inputs, and can only be used for the specific
# question. My second attempt below has more variability and flexibility.

from collections import Counter

all_request_types = []
all_locations = []

def count_request_type(id):
  all_request_types.append(service_requests[id]['Request Type'])
  
def count_request_location(id):  
  all_locations.append(service_requests[id]['City'])

for key in service_requests:
  count_request_type(key)

request_type_counter = Counter(all_request_types)
print(request_type_counter.most_common(1))

for location in service_requests:
  count_request_location(location)

loc_counter = Counter(all_locations)
print(loc_counter.most_common(1))

# Part 2, Creating one function that allows the user to find the most common
# instance of any category of information that is desired. This function would
# work for any dictionary that has data arranged in a similar manner to the
# service_requests dictionary. 

def info_seeker(dictionary, desired_info):
  info_list = []
  for info in dictionary:
    info_list.append(service_requests[info][desired_info])
  info_counter = Counter(info_list)
  print(info_counter.most_common(1))

info_seeker(service_requests, "Taken By")
