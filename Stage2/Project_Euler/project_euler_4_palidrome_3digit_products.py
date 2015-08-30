import datetime

def check_palindrome(var):
    var = str(var)
    length = len(var)
    i = 0
    while i < length:
        if var[i] != var[-1-i]:
            return False
        i += 1
    return True

def gen_palindromes(n):
    '''
    generates palindromes list, where each number is product of 2 n digited numbers
    '''
    least = int(str(1) + str(0) * (n-1))
    great = int(str(1) + str(0) * n)
    palindromes = []

    start = datetime.datetime.now()
    for m in xrange(least, great):
        for k in xrange(m, great):
            if check_palindrome(k * m):
                palindromes.append(k * m)

    print "compuation time is {0}".format(datetime.datetime.now() - start)
    return max(palindromes)

print gen_palindromes(int(raw_input("Enter number of digits, to generate palindormes, where each number is product of 2 n digited numbers:")))