
import kata.formulae.main as cb
from age_finder_class import Person
import logging
import unittest


class Tests(unittest.TestCase):

    def test_age_finder_oop(self):
        johnDoe = Person(1961)
        result = johnDoe.current_age()
        self.assertEqual(result, (2017-1961))

    def test_age_finder_oop_ref(self):
        janeDoe = Person(1987)
        result = janeDoe.get_reference_age(2045)
        self.assertEqual(result, (2045-1987))

    def test_age_finder_oop_negative(self):
        kellyDoe = Person(1990)
        with self.assertRaises(ValueError):
            kellyDoe.get_reference_age(1956)




logging.info("testing has finished.")
