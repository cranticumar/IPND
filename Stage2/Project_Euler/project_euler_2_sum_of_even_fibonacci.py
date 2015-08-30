def gen_fib(maxi):
    '''
    Generates fibonacci series till specified maxi
    '''
    li_fib = []
    prev = 1
    current = 2
    if maxi > 0:
        li_fib.append(prev)
    if maxi > 1:
        li_fib.append(current)
    while (prev + current) <= maxi:
        li_fib.append(prev + current)
        prev = current
        current = li_fib[-1]
    return li_fib

def gen_fib_sum(maxi, filter):
    '''
    Generates sum of numbers in provided list
    '''
    if not isinstance(maxi, int):
        raise Exception("{0} is not an integer".format(maxi))
    li = gen_fib(maxi)
    sum = 0
    for number in li:
        if filter != 'all':
            if (number % 2 == 0) and filter == 'even':
                sum += number
            elif filter == 'odd':
                sum += number
        elif filter == 'all':
            sum += number
        else:
            raise Exception("unknown filter")
    return sum
 
'''Tests'''
print gen_fib_sum(int(raw_input("Enter maximum Limit to Fibonacci Series: ")), 'even')