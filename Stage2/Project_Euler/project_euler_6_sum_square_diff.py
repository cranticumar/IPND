def gen_sigma_n(n):
    '''
    Generates sum of series
    '''
    return n*(n+1)/2

def gen_sigma_n_square(n):
    '''
    Generates sum of squares
    '''
    return n*(n+1)*(2*n+1)/6

n = int(raw_input("Enter n, for series till:"))
print abs((gen_sigma_n(n)**2)-gen_sigma_n_square(n))