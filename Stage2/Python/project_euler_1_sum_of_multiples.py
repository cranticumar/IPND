# Problem Statement #5: https://projecteuler.net/problem=1
def get_sum_multiples(range_of_numbers, list_of_multiples, all=False):
    sum = 0
    length = len(list_of_multiples)
    for n in range(range_of_numbers):
        for m in list_of_multiples:
            if n % m == 0 and isinstance(n/m, int):
                if not all:
                    sum += n
                    break
                elif list_of_multiples.index(m) == length - 1:
                    sum = sum + n
            elif all:
                break
    return sum

'''Tests'''
# print get_sum_multiples(1000, [3,5])
