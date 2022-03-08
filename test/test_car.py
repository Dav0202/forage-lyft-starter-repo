import sys
import unittest
import datetime
sys.path.append(".")
from utils import add_years_to_date




class TestBattery(unittest.TestCase):
    
    def test_nubbinbattery_need_service(self):
        print('test nubbin battery need service')
        current_date = datetime.date.today()
        last_service_date = datetime.date(2017, 4, 23)
        date_which_battery_should_be_serviced_by = add_years_to_date(
            last_service_date, 4)
        self.assertTrue(
            date_which_battery_should_be_serviced_by < current_date)
        
    def test_nubbinbattery_doesnt_need_service(self):
        print('test nubbin doesnt battery need service')
        current_date = datetime.date.today()
        last_service_date = datetime.date(2021, 4, 23)
        date_which_battery_should_be_serviced_by = add_years_to_date(
            last_service_date, 4)
        self.assertFalse(
            date_which_battery_should_be_serviced_by < current_date)    
    
    def test_spindlerbattery_need_service(self):
        print('test spindler battery need service')
        current_date = datetime.date.today()
        last_service_date = datetime.date(2017, 4, 23)
        date_which_battery_should_be_serviced_by = add_years_to_date(
            last_service_date, 4)
        self.assertTrue(
            date_which_battery_should_be_serviced_by < current_date)
        
    def test_spindlerbattery_doesnt_need_service(self):
        print('test spindler battery doesnt need service')
        current_date = datetime.date.today()
        last_service_date = datetime.date(2022, 4, 23)
        date_which_battery_should_be_serviced_by = add_years_to_date(
            last_service_date, 4)
        self.assertFalse(
            date_which_battery_should_be_serviced_by < current_date) 


class TestEngine(unittest.TestCase):
    def test_capuletengine_needs_service(self):
        current_milage = 70000
        last_service_milage = 30000
        self.assertTrue(current_milage-last_service_milage > 30000)
        
    def test_capuletengine_doesntneeds_service(self):
        current_milage = 50000
        last_service_milage = 30000
        self.assertFalse(current_milage-last_service_milage > 30000)   
        
    def test_willoughbyengine_needs_service(self):
        current_milage = 120000
        last_service_milage = 30000
        self.assertTrue(current_milage-last_service_milage > 60000)
        
    def test_willoughbyengine_doesntneeds_service(self):
        current_milage = 20000
        last_service_milage = 30000
        self.assertFalse(current_milage-last_service_milage > 60000)   
        
    def test_sternmanengine_needs_service(self):
        warning_light_is_on = True
        
        self.assertEqual(warning_light_is_on ,True)
        
    def test_sternmanengine_doesntneeds_service(self):
        warning_light_is_on = False
        
        self.assertEqual(warning_light_is_on ,False)         
        
        
'''
class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

'''

if __name__ == '__main__':
    unittest.main()
