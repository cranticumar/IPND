def check_prime(num):
    '''
    Check if number is prime or not
    '''
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i = (i + 2) if i != 2 else (i + 1)
    return True

def nth_prime(n):
    '''
    Generates nth Prime
    '''
    i = 1
    count = 1
    while count < n:
        i += 1
        if check_prime(i):
            count += 1
    return i

print nth_prime(int(raw_input("Enter the nth prime you need:")))