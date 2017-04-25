import unittest
import logging

import kata.descendents.main as cb


class Tests(unittest.TestCase):
    def test_main(self):
        cb.run()

    # we use the analytical solution to check the recursive and loopy solutions
    def test_generations_loopy(self):
        results_loopy = [cb.generations_loopy(j,3) for j in range(1, 8)]
        results_analytic = [cb.generations_analytical(j,3) for j in range(1,8)]
        self.assertEqual(results_analytic, results_loopy)

    def test_generations_recursive(self):
        results_recur = [cb.generations_recursive(j,2) for j in range(1, 8)]
        results_analytic = [cb.generations_analytical(j,2) for j in range(1,8)]
        self.assertEqual(results_analytic, results_recur)

    def test_generations_recursive_errors(self):
        with self.assertRaises(ValueError):
            cb.generations_recursive(12,0)

logging.info("testing has finished.")
