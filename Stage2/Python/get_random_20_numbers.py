# Problem Statement #4: Create a list of random 20 numbers between 0 and 10:
def get_random_list():
    l = []
    import random
    for n in range(20):
        l.append(random.randint(0,10))
    return l

# print get_random_list()