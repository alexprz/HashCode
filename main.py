from objects import *
from reading import *

listRides = listRides("a_example.in")

r = Ride()
r.index = 0



v = Vehicle()
v.addRide(r)
r.index = 1
v.addRide(r)
r.index = 3
v.addRide(r)
r.index = 2
v.addRide(r)
r.index = 5
v.addRide(r)


listVehicles = [v]

write(listVehicles)
