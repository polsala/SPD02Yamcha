# -*- coding: utf-8 -*-
import unittest
from mcwrapper import McWrapper as mw
from yamcha import MCD, PRIME, FACTORS
import sys
import logging


class TestYamcha(unittest.TestCase):
    logging.basicConfig(stream=sys.stderr)

    def test_MCD(self):
        n1 = 45
        n2 = 90
        expected_mcd = 45

        res, execute_time = mw.generic_time_execution_check(
            MCD.euclid, n1, n2
        )

        res2, execute_time2 = mw.generic_time_execution_check(
            MCD.euclid, n2, n1
        )

        res3, execute_time3 = mw.generic_time_execution_check(
            MCD.bezout, n1, n2
        )

        # Check if all results are the same
        self.assertTrue(
            all([r == expected_mcd for r in [res, res2, res3[0]]])
        )

    def test_Prime(self):
        n1 = 673
        n2 = 7907
        n3 = 99191

        prime_charm_list = [n1, n2, n3]

        is_prime_res = [PRIME.is_prime(n) for n in prime_charm_list]
        is_carm = [PRIME.is_carmichael(n) for n in prime_charm_list]

        self.assertTrue(all(is_prime_res))
        self.assertTrue(all(is_carm))

        n4 = 8
        n5 = 64712
        nothing = [n4, n5]

        is_not_prime_res = [not PRIME.is_prime(n) for n in nothing]
        is_not_carm = [not PRIME.is_carmichael(n) for n in nothing]

        self.assertTrue(all(is_not_prime_res))
        self.assertTrue(all(is_not_carm))

        n6 = 1105
        self.assertTrue(PRIME.is_carmichael(n6))
        self.assertFalse(PRIME.is_prime(n6))

    def test_Factors(self):
        n10 = 126345
        expected_1 = [3, 5, 8423]
        n20 = 1263452836
        expected_2 = [2, 2, 23, 13733183]

        res1 = FACTORS.prime_factors(n10)
        res2 = FACTORS.prime_factors(n20)

        self.assertEqual(res1, expected_1)
        self.assertEqual(res2, expected_2)
