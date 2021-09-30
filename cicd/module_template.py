"""Python module template."""
import unittest


def hello_world(*arg, **kwarg):
    print("Hello World")
    if arg or kwarg:
        print(f"  - Arguments as Inputs: {arg}")
        print(f"  - Arguments as KeyVal: {kwarg}")
    return True


class Tests(unittest.TestCase):
    """Tests for `module_template` package."""
    def __init__(self, testName, value=None):
        super().__init__(testName)
        self.value = value

    @classmethod
    def setUpClass(cls):
        """Shared set up fixtures, if any (runs only once).
        """
        print("Test setUpClass")

    @classmethod
    def tearDownClass(cls):
        """Shared tear down fixtures, if any (runs only once).
        """
        print("Test tearDownClass")

    def setUp(self):
        """Set up test fixtures, if any (once per case).
        """
        print("Tests setUp")

    def tearDown(self):
        """Tear down test fixtures, if any (once per case).
        """
        print("Tests tearDown")

    def test_001(self):
        print("Param value: {}".format(self.value))
        self.assertTrue(True)

    def test_002(self):
        print("Param value: {}".format(self.value))
        self.assertIsInstance(self.value, int)
