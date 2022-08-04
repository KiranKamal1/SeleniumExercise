import unittest
from tests.testCase import test_googlesearch
#from tests.testCase2 import test_dragAnddrop

tc1 = unittest.TestLoader().loadTestsFromTestCase(test_googlesearch)
#tc2 = unittest.TestLoader().loadTestsFromTestCase(test_dragAnddrop)


smokeTest = unittest.TestSuite([tc1])
unittest.TextTestRunner(verbosity=2).run(smokeTest)
