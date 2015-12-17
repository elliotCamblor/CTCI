import unittest

if __name__ == "__main__":
    tests = unittest.TestLoader().discover('.')
    testRunner = unittest.runner.TextTestRunner()
    testRunner.run(tests)
