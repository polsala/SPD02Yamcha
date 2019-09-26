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

        n1 = pow(2, 342)
        n2 = pow(2, 442)

        res, execute_time = mw.generic_time_execution_check(
            MCD.euclid, n1, n2
        )

        log.debug(log_template.format('MCD: Euclides Sense Bezout', n1, n2, res, execute_time))

        res2, execute_time2 = mw.generic_time_execution_check(
            MCD.bezout, n1, n2
        )

        log.debug(log_template.format('MCD: Euclides amb Bezout', n1, n2, res2, execute_time2))
