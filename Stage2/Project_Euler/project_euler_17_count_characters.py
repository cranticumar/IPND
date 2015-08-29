# Problem Statement: http://www.mathblog.dk/project-euler-17-letters-in-the-numbers-1-1000/
strings = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

def count_letters(start, end):
    # re-assign
    if start > end:
        start = start + end
        end = start - end
        start = start -end
    # assert(end < 10000)
    sum_of_letters = 0
    for i in range(start, end+1):
        sum_of_letters += get_thousands(i) + get_hundreds(i) + get_tens(i) + get_ones(i)
    return sum_of_letters

def get_thousands(number):
    if number/1000 > 0:
        if number % 1000 > 0 and number % 1000 < 100:
            print str(number) + ' thousands :' + strings[number/1000] + ' thousand and'
            return len(strings[number/1000]) + 11
        else:
            try:
                print str(number) + ' thousands :' + strings[number/1000] + ' thousand '
                return len(strings[number/1000]) + 8
            except KeyError:
                print '-->' + str(number) + ' thousands :' + str(get_tens(number/1000)) + str(get_ones(number/1000)) + 'thousand'
                return get_tens(number/1000) + get_ones(number/1000) + 8
    else:
        return 0

def get_hundreds(number):
    if (number % 1000)/100 > 0:
        if number % 100 > 0 and number % 100 < 100:
            print str(number) + ' hundreds :' + strings[(number % 1000)/100] + ' hundred and'
            return len(strings[(number % 1000)/100]) + 10
        else:
            print str(number) + ' hundreds :' + strings[(number % 1000)/100] + ' hundred'
            return len(strings[(number % 1000)/100]) + 7
    else:
        return 0

def get_tens(number):
    if (number % 100)/10 > 1:
        print str(number) + ' tens :' + strings[(number % 100)/10 * 10]
        return len(strings[(number % 100)/10 * 10])
    else:
        return 0

def get_ones(number):
    if (number % 100) > 19 and number%10 > 0:
        print str(number) + ' ones :' + strings[number % 10]
        return len(strings[number % 10])
    elif number%100 < 20 and  number%100 > 0:
        print str(number) + ' ones :' + strings[(number % 100)]
        return len(strings[(number % 100)])
    else:
        return 0

'''Tests'''
 print count_letters(119, 121)
 print '*' * 10
 print count_letters(99,101)
 print '*' * 10
 print count_letters(109,111)
 print '*' * 10
 print count_letters(9,11)
 print '*' * 10
 print count_letters(19,21)
 print '*' * 10
 print count_letters(899,901)
 print '*' * 10
 print count_letters(88,91)
 print '*' * 10
 print count_letters(1,1000)
 print count_letters(21201,21201)