def gen_prime_factors(number):
    '''
    Generates a list of prime factors for the provided number
    http://www.ilovemaths.com/1lcmandhcf.asp
    '''
    largest = []
    lcm = []
    n = 2

    while n*n <= number:
        print n
        if number % n == 0:
            number = number/n
            largest.append(n)
        else:
            n = 3 if n == 2 else n+2

    largest.append(number)
    print largest
    if number > largest[-1]:
        return number
    return largest[-1]

primes = gen_prime_factors(int(raw_input("Enter a number: ")))
print primes