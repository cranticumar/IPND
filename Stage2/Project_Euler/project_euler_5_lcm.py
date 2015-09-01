def gen_lcm(series):
    '''
    Generates LCM of series numbers
    '''
    quotients = series
    lcm = 1
    m = 2
    while True:
        reminders = [n % m for n in quotients]
        print reminders
        if 0 in reminders:
            quotients = [n / m if n % m == 0 else n for n in quotients]
            lcm = lcm * m
        else:
            m += 1
        print quotients
        if reduce(lambda x, y: x * y, quotients) == 1:
            break

    return lcm

print gen_lcm(map(int, raw_input("Enter series of number with space in between:").split(" ")))