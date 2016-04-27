#!/bin/env python
"""Run HTCondor-CE unit tests"""

import glob
import unittest

TESTS = [test.strip('.py') for test in glob.glob('test*.py')]
SUITE = unittest.TestLoader().loadTestsFromNames(TESTS)
unittest.TextTestRunner(verbosity=2).run(SUITE)


