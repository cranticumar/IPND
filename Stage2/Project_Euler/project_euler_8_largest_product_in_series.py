def largest_product(series, seq):
    '''
    largest product of seq sequence digits in series
    '''
    if seq > len(series):
        raise Exception("Sequence less than series")

    largest = 1
    for i in range(0, len(series)):
        if i + seq <= len(series):
            product = reduce(lambda x, y: int(x) * int(y), series[i:i+seq])
            print product
            if largest < product:
                largest = product
    return largest

print largest_product(raw_input("Enter the series:"), int(raw_input("sequence:")))