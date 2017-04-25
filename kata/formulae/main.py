# coding=utf-8
"""
Offer a menu to solve a variety of problems.

Any of these could be a stand alone Kata, but the overhead of writing a kata makes it easier to batch them up.

Caculate your age given current year and birth year. Do same given exact dates.

Caculate gas mileate/fuel efficiency given starting mileate, ending mileage, amount to fill the tank.

Calculate weight on planet X given gravity ratio and your weight.

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


    find_age(1987, 2017)

    efficiency(25,300,10.5)

    x_weight(160, 0.38)

# 1. age kata
# given birth year (xxxx), and current year (yyyy), find age
# assume that years are 4 digit numbers A.D.

def find_age(birth_year, current_year):
    if not type(birth_year) == int or not type(current_year) == int:
        raise TypeError("please make sure years are given as 4 digit integers.")
    elif not len(str(birth_year)) == 4 or not len(str(current_year)) == 4:
        raise ValueError("please make sure years are given as 4 digit integers.")
    else:
        if current_year > birth_year:
            age = current_year - birth_year
            return age
        else:
            raise ValueError("current year should be greater than birth year.")


# 2. fuel efficiency kata
# given initial and final mileage (miles) and gas tank (gallons), find efficiency (miles/gallon)
# assume that a full tank of gas is always used before "ending mileage" is reached.

def efficiency(mileage_initial, mileage_final, tank_volume):
    if mileage_final < mileage_initial:
        raise ValueError("final mileage can not be smaller than inital mileage. you may have switched argument order.")
    elif tank_volume <= 0.0:
        raise ValueError("gas tank has to be greater than 0.")
    else:
        miles_driven = mileage_final - mileage_initial
        fuel_efficiency = miles_driven/float(tank_volume)
        return fuel_efficiency

#3. gravity kata
# given earth weight w_e (lbs), and gravity ratio R = g_x/g_e, find weight on planet x, w_x (lbs)
# w_e = m*g_e , w_x = m*g_x    -->  w_x = R*w_e

def x_weight(e_weight, R):
     return e_weight*R



if __name__ == "__main__" or __name__ == "builtins":
    # Need an environment to run this?
    # https://repl.it/languages/python3
    logging.info("The application is starting.")
    run()
