def gen_sigma_n(n):
    '''
    Generates sum of series
    '''
    return n*(n+1)/2

def my_own_derivation(a):
    '''
    1,0,1
    3,0+4x1, b+1
    5,0+4x2,13
    7,24,25
    9,40,41
    11,60,61
    13,84,85
    15,112,113
    17,144,145
    
    2,0,2
    4,0+3*1-0,b+2
    6,0+0+3*1-0+3*2-1,b+2
    
    0+3*1-0+3*2-1+3*3-2
    3(0+1+2+3)-(1+2)
    '''
    if a % 2 != 0:
        b = 4*gen_sigma_n(a/2)
        return [a, b, b+1]
    else:
        b = 3*gen_sigma_n(a/2 - 1) - gen_sigma_n(a/2 - 2)
        return [a, b, b+2]

def kelley_l_ross_derivation(a):
    '''
    ref: http://www.friesian.com/pythag.htm
    '''
    if a % 2 != 0:
        b = (a/2)**2 - 1
        return [a, b, b+1]
    else:
        b = (a**2 - 1)/2
        return [a, b, b+2]

def generate_pythagorean_triplet(i, my=True):
    '''
    Decide which algorithm to use
    '''
    if my:
        return my_own_derivation(i)
    else:
        return kelley_l_ross_derivation(i)

def get_pythagorean_triplet_sum_product(sum):
    '''
    get the product of triplet who sum is provided number
    '''
    i = 1
    s = 0
    while s <= sum:
        triplet = generate_pythagorean_triplet(i)
        s = reduce(lambda x, y: x + y, triplet)
        print triplet
        if s == sum:
            return reduce(lambda x, y: x * y, triplet)
        i += 1
    return "Triplet of sum " + str(sum) + " not found"


print get_pythagorean_triplet_sum_product(int(raw_input("Enter the sum of the triplet to be:")))