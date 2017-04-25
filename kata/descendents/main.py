# coding=utf-8
"""
Calculate how many descendents you will have after n generations if each of your descendents has x children

So just to make clear who is included or not:

   A marries B, generation one has two people.
   A & B have 2 kids, generation two has four people
   The 2 kids have two kids each, generation three has 8 people.
And so on.
"""
from __future__ import print_function, unicode_literals, absolute_import

# configure logging for file and console output.
import logging
import os.path
if os.path.isfile("log.txt"):
    os.remove("log.txt")
logging.basicConfig(filename='log.txt', format='%(asctime)s %(message)s', level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

# strongly discourage using console input and output.
# You can make testable code full of input and print statements, but it introduces
# unnecessary complexity. See kata on testing input and print with fakes and spies.
def input(*args, **kwargs):
    raise TypeError("Don't use input, log or get input from function arguments.")
def raw_input(*args, **kwargs):
    raise TypeError("Don't use raw_input, either, log or get input from function arguments.")
def print(*args, **kwargs):
    raise TypeError("Don't use print, return values from functions or callables.")

def run():
    logging.info("The application is starting. Testing...")
    generations_analytical(4,2)
    generations_recursive(4,2)
    generations_loopy(4,2)


# ** we always assume that generation 1 has 2 people ("Adam and Eve" initialization) **

# an analytical expression is easily found by observing the series
# N(n) = 2*X^(n-1)
# this is (relatively) the most efficient algorithm for this problem ~ O(1)
def generations_analytical(n,x):
    if n < 1 or x < 1:
        raise ValueError("generation number(n) and children number(x) must be greater than 1.")
    else:
        return 2*(x**(n-1))


# we can also use a recursive algorithm
# this is elegant, but less efficient ~ O(n) + f_call overhead
def generations_recursive(n,x):
    if n == 1:
        return 2
    elif n < 1 or x < 1:
        raise ValueError("generation number (n) and children number (x) must be greater than 1.")
    else:
        return x*generations_recursive(n-1,x)


# we can also use a for-loop algorithm ~ O(n)
def generations_loopy(n,x):
    if n < 1 or x < 1:
        raise ValueError("generation number(n) and children number(x) must be greater than 1.")
    else:
        current_gen = 2
        for j in range(2,n+1):
            current_gen *= x
        return current_gen



if __name__ == "__main__" or __name__ == "builtins":
    # Need an environment to run this?
    # https://repl.it/languages/python3
    logging.info("The application is starting.")
    run()
