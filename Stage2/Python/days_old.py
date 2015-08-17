# Problem Statement: Given your birthday and current date, calculate your age in days
# Compensate for leap days. Assume that the birthday and current date are correct dates
# (no time travel). Simply put, if you were born 1 Jan 2012 and todays date is 2 Jan 2012
# you are 1 days old.

from datetime import date, datetime
import sys

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_age_in_days(birth_date, today_date=0, inbuilt=False):
    if inbuilt:
        today_date = date.today()
        return today_date - datetime.strptime(birth_date, '%Y,%m,%d').date()
    else:
        days = 0
        (byear, bmonth, bday) = get_split_and_check(birth_date)
        (tyear, tmonth, tday) = get_split_and_check(today_date)
        for year in range(byear+1, tyear):
            print year
            if year%4 == 0:
                days += 366
            else:
                days +=365
        if byear != tyear:
            for month in range(bmonth, len(days_in_month)):
                days += days_in_month[month]
                if month == 1 and byear%4 == 0:
                    days += 1
            for month in range(0,tmonth-1):
                days += days_in_month[month]
                if month == 1 and tyear%4 == 0:
                    days += 1
            days = days + tday + days_in_month[bmonth-1] - bday
        else:
            if bmonth != tmonth:
                for month in (range(bmonth, tmonth-1)):
                    days += days_in_month[month]
                    if month == 1 and byear%4 == 0:
                        days += 1
                days = days + tday + days_in_month[bmonth-1] - bday
            else:
                days = tday - bday
        return days 

def get_split_and_check(anydate):
    location = 0
    positions = []
    while anydate.find(',', location) != -1:
        location = anydate.find(',', location) + 1
        positions.append(location-1)
    if len(positions) == 2:
        if int(anydate[positions[0]+1:positions[1]]) > 12:
            print "Invalid Month"
            sys.exit(0)
        if int(anydate[positions[0]+1:positions[1]]) != 2:
            if int(anydate[positions[1]+1:]) > days_in_month[int(anydate[positions[0]+1:positions[1]]) - 1]:
                print "Invalid Day in month " + anydate[positions[0]+1:positions[1]]
                sys.exit(0)
        else:
            if int(anydate[0:positions[0]]) % 4 == 0:
                if int(anydate[positions[1]+1:]) > 29:
                    print "Invalid Day in month " + anydate[positions[0]+1:positions[1]]
                    sys.exit(0)
                elif int(anydate[positions[1]+1:]) > 28:
                    print "Invalid Day in month " + anydate[positions[0]+1:positions[1]]
                    sys.exit(0)
        return (int(anydate[0:positions[0]]), int(anydate[positions[0]+1:positions[1]]), int(anydate[positions[1]+1:]))
    else:
        raise Exception("improper fomrat of date")

# print 'you are ' + str(get_age_in_days(datetime.strptime(raw_input(
#     "Provide your birth date in yyyy,m,d: "), '%Y,%m,%d'))) + ' old'

days = get_age_in_days(raw_input("birth date(yyyy,m,d): "), raw_input("input today's date(yyyy,m,d): "), False
    )
print days