import math

# You have shapes with measurements:
# Cuboid: Height (h): 25/7, Width (w): 25/2, Length (l): 35
# Cone: Height (h): 10, Radius of base (r): 3
#Calculate the volume and surface areas of the shapes using the following equations.
h = 25/7
w = 25/2
l = 35
h_2 = 10
r = 3
pi = 3.14

cuboid = "cuboid"
cone = "cone"

lw = l * w 
lh = l * h 
hw = h * w
cuboid_volume = l * w * h
cuboid_surface_area = 2*lw + 2*lh + 2*hw

cone_volume = pi * r**2 * h_2 / 3
cone_surface_area = pi * r * (r + math.sqrt(h_2**2 + r**2))
