def gen_prime_factors(number):
    '''
    Generates a list of prime factors for the provided number
    '''
    largest = []
    n = 2

    while n*n <= number:
        if number % n == 0:
            number = number/n
            largest.append(n)
        else:
            n += 1

    largest.append(number)

    if number > largest[-1]:
        return number
    return largest[-1]

primes = gen_prime_factors(int(raw_input("Enter a number: ")))
print primes