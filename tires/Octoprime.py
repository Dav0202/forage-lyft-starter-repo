from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_ware_sensor):
        self.tire_ware_sensor = tire_ware_sensor
        
    def needs_service(self):
        if sum(self.tire_ware_sensor) >= 3:
            return True
        else:
            return False
        