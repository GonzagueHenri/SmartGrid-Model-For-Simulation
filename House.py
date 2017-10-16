import Battery
import EV
import Controller

class House:
    num_created_obj = 0

# Responsible of the consumption of its habitants
# Is linked with the external grid

    def __init__(self,houseId):
        self.id = houseId
        self.controller = Controller(houseId)
        House.num_created_obj += 1   # Gives the number of houses created


    def create_battery(self):
        battery = Battery(self.id)

    def create_consummer(self):
        consummer = Consummer(self.id)

    def create_ev(self):
        ev = EV(self.id)
