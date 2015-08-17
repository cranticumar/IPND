
# Problem Statement: find last occurance position of target_string in search_string
def find_last(search_string, target_string):
    search_location = 0
    while search_string.find(target_string, search_location) >= 0:
        search_location = search_string.find(target_string, search_location) + 1
    return search_location-1