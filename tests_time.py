# -*- coding: utf-8 -*-
import unittest
from mcwrapper import McWrapper as mw
from yamcha import MCD, PRIME
import sys
import logging
from math import pow


class TestTimeFunctions(unittest.TestCase):
    logging.basicConfig(stream=sys.stderr)

    def test_time_execution_over_euclid_mcd(self):
        logging.getLogger("TestTimeFunctions.test_time_execution_over_euclid_mcd").setLevel(logging.DEBUG)
        log = logging.getLogger("TestTimeFunctions.test_time_execution_over_euclid_mcd")

        log_template = (
            "\n"
            "Method: {}\n"
            "N1: {}\n"
            "N2: {}\n"
            "Result: {}\n"
            "Time: {}\n"
        )

        n1 = 45
        n2 = 90

        n3 = pow(2, 342)
        n4 = pow(2, 442)

        self.assertTrue(n3 > n1)
        self.assertTrue(n4 > n2)

        res, execute_time = mw.generic_time_execution_check(
            MCD.euclid, n1, n2
        )

        log.debug(log_template.format('MCD: Euclides Sense Bezout', n1, n2, res, execute_time))

        res2, execute_time2 = mw.generic_time_execution_check(
            MCD.bezout, n1, n2
        )

        log.debug(log_template.format('MCD: Euclides amb Bezout', n1, n2, res2, execute_time2))

        res3, execute_time3 = mw.generic_time_execution_check(
            MCD.euclid, n3, n4
        )

        log.debug(log_template.format('MCD: Euclides Sense Bezout', n3, n4, res3, execute_time3))

        res4, execute_time4 = mw.generic_time_execution_check(
            MCD.bezout, n3, n4
        )

        log.debug(log_template.format('MCD: Euclides amb Bezout', n3, n4, res4, execute_time4))

        statics = (
            "\n"
            "Time without Bezout:\n"
            "   Lower Values:  {}\n"
            "   Higher Values: {}\n"
            "Time with Bezout:\n"
            "   Lower Values:  {}\n"
            "   Higher Values: {}\n"
        )
        log.debug(statics.format(execute_time, execute_time3, execute_time2, execute_time4))

    def test_time_execution_over_is_prime(self):
        logging.getLogger("TestTimeFunctions.test_time_execution_over_is_prime").setLevel(logging.DEBUG)
        log = logging.getLogger("TestTimeFunctions.test_time_execution_over_is_prime")

        n10 = 1895625673
        n13 = 7711819029511
        n15 = 292824577079257
        n17 = 10646454924419263

        # 10 Digits
        res10, execute_time10 = mw.generic_time_execution_check(
            PRIME.is_prime, n10
        )

        # 13 Digits
        res13, execute_time13 = mw.generic_time_execution_check(
            PRIME.is_prime, n13
        )

        # 15 Digits
        res15, execute_time15 = mw.generic_time_execution_check(
            PRIME.is_prime, n15
        )

        # 17 Digits
        res17, execute_time17 = mw.generic_time_execution_check(
            PRIME.is_prime, n17
        )

        statics_res = (
            "\n"
            "10 Digits Number:\n"
            "  - Number: {}\n"
            "  - Result: {}\n"
            "  - Time: {}\n\n"
            "13 Digits Number:\n"
            "  - Number: {}\n"
            "  - Result: {}\n"
            "  - Time: {}\n\n"
            "15 Digits Number:\n"
            "  - Number: {}\n"
            "  - Result: {}\n"
            "  - Time: {}\n\n"
            "17 Digits Number:\n"
            "  - Number: {}\n"
            "  - Result: {}\n"
            "  - Time: {}\n\n"
        ).format(
            n10, res10, execute_time10,
            n13, res13, execute_time13,
            n15, res15, execute_time15,
            n17, res17, execute_time17
        )

        log.debug(statics_res)

    def test_time_execution_over_is_prime_vs_carmichael(self):
        logging.getLogger("TestTimeFunctions.test_time_execution_over_is_prime_vs_carmichael").setLevel(logging.DEBUG)
        log = logging.getLogger("TestTimeFunctions.test_time_execution_over_is_prime_vs_carmichael")

        n10 = 1895625673
        n17 = 10646454924419263

        # 10 Digits
        res10_prime, execute_time10_prime = mw.generic_time_execution_check(
            PRIME.is_prime, n10
        )

        res10_cha, execute_time10_cha = mw.generic_time_execution_check(
            PRIME.is_carmichael, n10
        )

        # 17 Digits
        res17_prime, execute_time17_prime = mw.generic_time_execution_check(
            PRIME.is_prime, n17
        )

        res17_cha, execute_time17_cha = mw.generic_time_execution_check(
            PRIME.is_carmichael, n17
        )

        statics_res = (
            "\n"
            "10 Digits Number:\n"
            "-----------------"
            "Method: is_Prime\n"
            "  - Number: {}\n"
            "  - Result: {}\n"
            "  - Time: {}\n\n"
            "\n"
            "Method: carmichael\n"
            "  - Number: {}\n"
            "  - Result: {}\n"
            "  - Time: {}\n\n"
            "17 Digits Number:\n"
            "-----------------"
            "Method: is_Prime\n"
            "  - Number: {}\n"
            "  - Result: {}\n"
            "  - Time: {}\n\n"
            "\n"
            "Method: carmichael\n"
            "  - Number: {}\n"
            "  - Result: {}\n"
            "  - Time: {}\n\n"
        ).format(
            n10, res10_prime, execute_time10_prime,
            n10, res10_cha, execute_time10_cha,
            n17, res17_prime, execute_time17_prime,
            n17, res17_prime, execute_time17_cha
        )

        log.debug(statics_res)
