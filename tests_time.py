# -*- coding: utf-8 -*-
import unittest
from mcwrapper import McWrapper as mw
from yamcha import MCD, PRIME, FACTORS, MODULAR
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

        n10 = 337
        n17 = 31891
        n4 = 1105  # Carmichael and not prime

        # 4 Digits
        res4_prime, execute_time4_prime = mw.generic_time_execution_check(
            PRIME.is_prime, n4
        )

        res4_cha, execute_time4_cha = mw.generic_time_execution_check(
            PRIME.is_carmichael, n4
        )

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
            "\n\n"
            "3 Digits Number:\n"
            "-----------------\n"
            "Method: is_Prime\n"
            "  - Number: {}\n"
            "  - Result: {}\n"
            "  - Time: {}\n\n"
            "\n"
            "Method: carmichael\n"
            "  - Number: {}\n"
            "  - Result: {}\n"
            "  - Time: {}\n\n"
            "4 Digits Number:\n"
            "-----------------\n"
            "Method: is_Prime\n"
            "  - Number: {}\n"
            "  - Result: {}\n"
            "  - Time: {}\n\n"
            "\n"
            "Method: carmichael\n"
            "  - Number: {}\n"
            "  - Result: {}\n"
            "  - Time: {}\n\n"
            "5 Digits Number:\n"
            "-----------------\n"
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
            n4, res4_prime, execute_time4_prime,
            n4, res4_cha, execute_time4_cha,
            n17, res17_prime, execute_time17_prime,
            n17, res17_prime, execute_time17_cha
        )

        log.debug(statics_res)
        self.assertTrue(all([res10_prime, res10_cha, res17_prime, res17_cha, res4_cha]))
        self.assertFalse(res4_prime)

    def test_time_execution_over_prime_factors(self):
        logging.getLogger("TestTimeFunctions.test_time_execution_over_prime_factors").setLevel(logging.DEBUG)
        log = logging.getLogger("TestTimeFunctions.test_time_execution_over_prime_factors")

        n10 = 1263452836
        n20 = 12634528361263452836

        res10_cha, execute_time10_cha = mw.generic_time_execution_check(
            FACTORS.prime_factors, n10
        )

        res20_cha, execute_time20_cha = mw.generic_time_execution_check(
            FACTORS.prime_factors, n20
        )

        statics_r = (
            "Method: prime_factors(n)\n"
            "Number 10 digits:\n"
            "N: {}\n"
            "Result: {}\n"
            "Time: {}\n\n"
            "Number 20 digits:\n"
            "N: {}\n"
            "Result: {}\n"
            "Time: {}\n\n"
        )

        log.debug(
            statics_r.format(
                n10, res10_cha, execute_time10_cha,
                n20, res20_cha, execute_time20_cha
            )
        )

    def test_time_over_modular_invert(self):
        logging.getLogger("TestTimeFunctions.test_time_over_modular_invert").setLevel(logging.DEBUG)
        log = logging.getLogger("TestTimeFunctions.test_time_over_modular_invert")

        n1 = 123
        k1 = 223

        n2 = 423432423452435345345
        k2 = 643543552344563453453

        res1, execute_time1 = mw.generic_time_execution_check(
            MODULAR.invert_modular, n1, k1
        )

        res2, execute_time2 = mw.generic_time_execution_check(
            MODULAR.invert_modular, n2, k2
        )

        statics_t = (
            "\n"
            "Number: {}\n"
            "Result: {}\n"
            "Time: {}\n\n"
            "Number: {}\n"
            "Result: {}\n"
            "Time: {}\n\n"
        )

        log.debug(statics_t.format((n1, k1), res1, execute_time1, (n2, k2), res2, execute_time2))
