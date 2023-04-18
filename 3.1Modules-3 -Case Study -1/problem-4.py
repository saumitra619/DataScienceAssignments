

from math import sin, cos, sqrt, radians ,asin

# approximate radius of earth in km 
R = 6373.0 

latt_of_mumbai = radians(18.927090) 
long_of_mumbai = radians(72.829681) 
latt_of_delhi = radians(28.656158) 
long_of_delhi = radians(77.241020) 

dlon = latt_of_delhi - latt_of_mumbai 
dlat = long_of_delhi - long_of_mumbai 

a = sin(dlat / 2)**2 + cos(latt_of_mumbai) * cos(latt_of_delhi) * sin(dlon / 2)**2 

c = 2 * asin(sqrt(a))

distance = R * c 

print("Result:", distance) 