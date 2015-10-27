import datetime
import string
import logging
import re
from crypto import Crypto
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
    """
    Validates sign up form while registration for correctness of the details
    """
    errors = dict()
    password_elist = list()
    if not (kw.get("uname") and re.match("^[a-z0-9_\.]{5,20}$", kw.get("uname"))):
        errors["error_username"] = "That is an invalid username"
    elif Users.get_by_username(Crypto.encrypto_wo_salt(kw.get("uname"))):
        # If username (each username has its own encrypted version) already exists in database,
        # this sets an error
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
    """
    Validates Login form and sets errors in case of login failure
    """
    errors = dict()
    usr = Users.login(kw.get("uname"), kw.get("pwd"))
    if usr is None:
        # If username is not found in the datastore, sets an error for login
        errors["error_login"] = "Login failed"
    return errors

def rot13cipher(text):
    """
    ROT13 - advances character by 13 places in cyclic manner. Technique used is
    add 13 to current letter index and get reminder beyond 26 to traverse in
    cyclic manner.
    """
    content = list(text)
    # as this is ROT13 cipher, advance_by variable is used for advancing the index
    advance_by = 13
    smallalpha = list(string.ascii_lowercase)
    alpha = list(string.ascii_uppercase)
    ciphered_text = ''
    for letter in content:
        if letter in smallalpha:
            ciphered_text += smallalpha[(smallalpha.index(letter) + advance_by) % len(smallalpha)]
        elif letter in alpha:
            ciphered_text += alpha[(alpha.index(letter) + advance_by) % len(alpha)]
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
            # though divisible y 4, only every 400th year is a leap year
            # http://science.howstuffworks.com/science-vs-myth/everyday-myths/question50.htm
            return True if year % 400 == 0 else False
        return True
    return False

def _validate_day(day, month, year):
    """Validate day as per the year and the month"""
    if day.isdigit():
        day = int(day)
        # usually there is no leap day, based on february and leap year, an additional day is set
        leap_day = 0
        if month.lower() == "february" and _is_leap_year(year):
            leap_day = 1

        if day <= days_in_month[month.lower()] + leap_day:
            return day

def _check_for_future_date(year, month, day):
    """Check if provide day is of future day"""
    if year > present_year:
        return False
    elif year == present_year:
        # in list, indices starts with 0, so as to match with month number, advance it by 1
        index_to_position = 1
        if months.index(month.lower()) + index_to_position > present_month:
            return False
        elif months.index(month.lower()) + index_to_position == present_month:
            print day
            if day <= present_day:
                return True
    return True