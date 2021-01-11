# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(5))
# => 120

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(5))