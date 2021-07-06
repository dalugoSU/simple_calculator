import unittest
from GUI import CalculatorApp


class TestCalculatorApp(unittest.TestCase):

    def setUp(self) -> None:
        self.test_calculator = CalculatorApp()

    def test_run(self):
        pass


if __name__ == "__main__":
    unittest.main()