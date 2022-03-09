from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_ware_sensor):
        self.tire_ware_sensor = tire_ware_sensor
        
        
    def needs_service(self):
        for i in self.tire_ware_sensor:
            if i >= 0.9:
                return True
            continue
        else:
            return False
        
