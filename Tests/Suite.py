import unittest
import Scenarios

suite_smoke = unittest.TestLoader().loadTestsFromModule(Scenarios)
unittest.TextTestRunner().run(suite_smoke)