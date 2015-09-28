import datetime

# List of Months in a year
months = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]
days_in_month = dict(zip(months,[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))

present = datetime.date.today()
present_year = present.year
present_month = present.month
present_day = present.day

def validate_year(year):
    """Validates year, if it is a year or not and it's range"""
    if year.isdigit():
        year = int(year)
        if year > 0:
            return year

def validate_month(month):
    """Validate its month, if it is valid month in calendar year"""
    if month.lower() in months:
        return True
    return False

def is_leap_year(year):
    """Check if provided year is a leap year or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            return True if year % 400 == 0 else False
        return True
    return False

def validate_day(day, month, year):
    """Validate day as per the year and the month"""
    if day.isdigit():
        day = int(day)
        if month.lower() == "february":
            if is_leap_year(year) and day <= (days_in_month[month.lower()] + 1):
                return day
        elif day <= days_in_month[month.lower()]:
            return day

def check_for_future_date(year, month, day):
    """Check if provide day is of future day"""
    if year > present_year:
        return False
    elif year == present_year:
        if months.index(month.lower()) + 1 > present_month:
            return False
        elif months.index(month.lower()) + 1 == present_month:
            print day
            if day <= present_day:
                return True
    return True


def validate_date(month, day, year):
    """take the input and check if it is a valid day by validating its month, day and year"""
    year = validate_year(year)
    if year is not None:
        if validate_month(month):
            day = validate_day(day, month, year)
            if day is not None:
                if check_for_future_date(year, month, day):
                    return True
    return False