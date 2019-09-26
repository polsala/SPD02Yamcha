# -*- coding: utf-8 -*-
import unittest
from mcwrapper import McWrapper as mw
from yamcha import MCD
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
