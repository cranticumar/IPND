import datetime
import string
import logging
import re
from udacity_datastore import *

# List of Months in a year
months = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]
days_in_month = dict(zip(months,[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))

present = datetime.date.today()
present_year = present.year
present_month = present.month
present_day = present.day

def validate_signupform(**kw):
    errors = dict()
    password_elist = list()
    if not (kw.get("uname") and re.match("^[a-z0-9_\.]{5,20}$", kw.get("uname"))):
        errors["error_username"] = "That is an invalid username"
    elif Users.get_by_username(kw.get("uname")):
        errors["error_username"] = "User already exists"

    if not (kw.get("disname") and re.match("^[a-zA-Z]{3,20}$", kw.get("disname"))):
        errors["error_dispname"] = "That is an invalid name"

    if not (kw.get("pwd") and re.match("^.{5,10}$", kw.get("pwd"))):
        password_elist.append("Character Limit of 5 (min) - 10 (max)")
    if not (re.match(".*[a-z].*", kw.get("pwd"))):
        password_elist.append("Password must contain atleast 1 small alphabet")
    if not (re.match(".*[A-Z].*", kw.get("pwd"))):
        password_elist.append("Password must contain atleast 1 Capital Letter")
    if not (re.match(".*[0-9].*", kw.get("pwd"))):
        password_elist.append("Password must contain atleast 1 number")

    if password_elist:
        errors["error_password"] = password_elist

    if not (kw.get("verify") and kw.get("verify") == kw.get("pwd")):
        errors["error_verify"] = "Passwords did not match"

    if kw.get("email"):
       if not re.match("^[\S]+@[\S]+\.[\S]+$", kw.get("email")):
           errors["error_email"] = "Not a valid email address"

    return errors

def validate_loginform(**kw):
    errors = dict()
    usr = Users.login(kw.get("uname"), kw.get("pwd"))
    if usr is None:
        errors["error_login"] = "Login failed"
    return errors

def rot13cipher(text):
    content = list(text)
    smallalpha = list(string.ascii_lowercase)
    alpha = list(string.ascii_uppercase)
    ciphered_text = ''
    for letter in content:
        if letter in smallalpha:
            ciphered_text += smallalpha[(smallalpha.index(letter) + 13) % len(smallalpha)]
        elif letter in alpha:
            ciphered_text += alpha[(alpha.index(letter) + 13) % len(alpha)]
        else:
            ciphered_text += letter
    return ciphered_text

def validate_date(month, day, year):
    """take the input and check if it is a valid day by validating its month, day and year"""
    year = _validate_year(year)
    if year is not None:
        if _validate_month(month):
            day = _validate_day(day, month, year)
            if day is not None:
                if _check_for_future_date(year, month, day):
                    return True
    return False

def _validate_year(year):
    """Validates year, if it is a year or not and it's range"""
    if year.isdigit():
        year = int(year)
        if year > 0:
            return year

def _validate_month(month):
    """Validate its month, if it is valid month in calendar year"""
    if month.lower() in months:
        return True
    return False

def _is_leap_year(year):
    """Check if provided year is a leap year or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            return True if year % 400 == 0 else False
        return True
    return False

def _validate_day(day, month, year):
    """Validate day as per the year and the month"""
    if day.isdigit():
        day = int(day)
        if month.lower() == "february":
            if is_leap_year(year) and day <= (days_in_month[month.lower()] + 1):
                return day
        elif day <= days_in_month[month.lower()]:
            return day

def _check_for_future_date(year, month, day):
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