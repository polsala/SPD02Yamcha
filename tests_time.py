# -*- coding: utf-8 -*-
import unittest
from mcwrapper import McWrapper as mw
from yamcha import MCD
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
