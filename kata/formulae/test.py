import unittest
import logging

import kata.formulae.main as cb


class Tests(unittest.TestCase):
    def test_main(self):
        cb.run()

    # test find_age() function
    def test_find_age_basecase(self):
        result = cb.find_age(1961, 2017)
        self.assertEqual(result, 56)

    def test_find_age_negative(self):
        with self.assertRaises(ValueError):
            cb.find_age(2017, 1961)

    def test_find_age_type(self):
        with self.assertRaises(TypeError):
            cb.find_age(1961, 2017.0)

    # test efficiency function
    def test_efficiency_basecase(self):
        result = cb.efficiency(30, 230, 12)
        self.assertEqual(result, (200/12.0))

    def test_efficiency_div(self):
        with self.assertRaises(ValueError):
            cb.efficiency(23, 45, 0)

    def test_efficiency_arg_order(self):
        with self.assertRaises(ValueError):
            cb.efficiency(2344, 1234, 78)

    # test planet x gravity function
    def test_gravity_basecase(self):
        result = cb.x_weight(100, 0.50)
        self.assertEqual(result, 50.0)

logging.info("all tests have finished running.")
