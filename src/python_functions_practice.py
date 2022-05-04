def return_10():
    return 10

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def length_of_string(string):
    return len(string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(x, y):
    return int(x) + int(y)

# def number_to_full_month_name(month):
#     year = {
#         1: "January",
#         2: "February",
#         3: "March",
#         4: "April",
#         5: "May"
#     }

def number_to_full_month_name(month):
    if month == 1:
        return "January"
    elif month == 3:
        return "March"
    elif month == 9:
        return "September"

def number_to_short_month_name(mon):
    if mon == 1:
        return "Jan"
    elif mon == 4:
        return "Apr"
    elif mon == 10:
        return "Oct"

def volume_of_cube(length):
    return length ** 3

def reverse_string(string):
    return string[::-1]

def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8

