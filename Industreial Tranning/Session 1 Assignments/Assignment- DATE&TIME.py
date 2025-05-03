# Assignment 1: Write a function that calculates compound interest using the formula A = P(1 + r/n)^(nt).

def compound_interest(principal, rate, times_compounded, years):
    amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
    return amount

principal = 1000
rate = 0.05
times_compounded = 12
years = 5

result = compound_interest(principal, rate, times_compounded, years)
print("Compound Interest after", years, "years:", format(result, ".2f"))





# Assignment 2: Create a script that prints the current time and updates every second.

import datetime
import time

def print_current_time():
    while True:
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")
        print("Current time:", formatted_time, end="\r")
        time.sleep(1)

print_current_time()
