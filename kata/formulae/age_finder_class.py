# this is an object oriented way of solving the age finding problem

from time import localtime, strftime


class Person:
    def __init__(self, birth_year):
        self.birth_year = birth_year
        self.age = self.current_age()

    def current_age(self):
        current_year = int(strftime("%Y", localtime()))
        return self.get_reference_age(current_year)

    def get_reference_age(self, reference_year):
        if not type(self.birth_year) == int or not type(reference_year) == int:
            raise TypeError("please make sure years are given as 4 digit integers.")
        elif not len(str(self.birth_year)) == 4 or not len(str(reference_year)) == 4:
            raise ValueError("please make sure years are given as 4 digit integers.")
        else:
            if reference_year > self.birth_year:
                age = reference_year - self.birth_year
                return age
            else:
                raise ValueError("current year should be greater than birth year.")
