import unittest
from datetime import date
import sys
sys.path.append(".")
from battery.spindlerbattery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2017-01-25")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())



if __name__ == '__main__':
    unittest.main()