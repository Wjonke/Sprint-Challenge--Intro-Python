# To the GroundVehicle class, add method drive() that returns "vroooom".
class GroundVehicle():
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.
    def drive(self):
        print("vroooom")


    # TODO
# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels = 2):
        super().__init__(num_wheels)
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"
    def drive(self):
        print("BRAAAP!!")


# TODO

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.
for i in vehicles:
    i.drive()
    # print("Im cruisin on", i.num_wheels, "wheels")
# TODO
