import unittest
from tires.Octoprime import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    print("test needs service true")
    def test_needs_service_true(self):
        tire_ware_sensor = [0.5,0.6,1.0,2.0]
        tire = OctoprimeTires(tire_ware_sensor)
        self.assertTrue(tire.needs_service())
        
    def test_needs_service_false(self):
        tire_ware_sensor = [0.5,0.6,0.1,0.7]
        tire = OctoprimeTires(tire_ware_sensor)
        self.assertFalse(tire.needs_service())    
        
        
if __name__ == '__main__':
    unittest.main()