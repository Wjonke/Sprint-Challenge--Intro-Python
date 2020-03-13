# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#################################
# class Vehicle is the base class
class Vehicle:
        pass

#################################
#################################

# subClass of Vehicle
class FlightVehicle(Vehicle):
        pass

class GroundVehicle(Vehicle):
        pass
#################################
#################################

# subClass of FlightVehicle
class Starship(FlightVehicle):
        pass


class Airplane(FlightVehicle):
        pass

################################
################################
# subClass of GroundVehicle
class Car(GroundVehicle):
        pass


class Motorcycle(GroundVehicle):
        pass
################################