#Single Elevator Program
#----Gives the best route for an elevator for N number of users with single destinations

#Author: VAibhav GArg
#Date: 02-08-2020

pick = []
drop = []
drn = []
stations0 = []
stations1 = []

n = input("Input the number of people in building: ")
n = int(n)
print("Input the position and destination for users:")

for i in range(n):
    p = input("Position of " + str(i+1) +": ")
    pick.append(int(p))
    d = input("Destination of " + str(i+1) + ": ")
    drop.append(int(d))
print("Pickups: ")
print(*pick, sep=", ")
print("Drops: ")
print(*drop, sep=", ")

for j in range(len(pick)):
    drn.append(0) if pick[j]<drop[j] else drn.append(1)
print("Directions: ")
print(*drn, sep=", ")

f = max(pick) if max(pick)>max(drop) else max(drop)

for k in range(len(pick)):
    if drn[k]==0:
        stations0.append(pick[k])
        stations0.append(drop[k])
    else:
        stations1.append(pick[k])
        stations1.append(drop[k])

stations0.sort()
stations1.sort(reverse=True)

print("Stations while going up: ")
print(*stations0, sep=", ")
print("Stations while going down: ")
print(*stations1, sep=", ")

#================SAMPLE OUTPUT 1================

# Input the number of people in building: 4
# Input the position and destination for users:
# Position of 1: 0
# Destination of 1: 9
# Position of 2: 6
# Destination of 2: 9
# Position of 3: 9
# Destination of 3: 1
# Destination of 4: 6
# Pickups:
# 0, 6, 9, 5
# Drops:
# 9, 9, 1, 6
# Directions:
# 0, 0, 1, 0
# Stations while going up:
# 0, 5, 6, 6, 9, 9
# Stations while going down:
# 9, 1


#================SAMPLE OUTPUT 2================

# Input the number of people in building: 4
# Input the position and destination for users:
# Position of 1: 1
# Destination of 1: 7
# Position of 2: 2
# Destination of 2: 3
# Position of 3: 4
# Destination of 3: 2
# Position of 4: 7
# Destination of 4: 1
# Pickups:
# 1, 2, 4, 7
# Drops:
# 7, 3, 2, 1
# Directions:
# 0, 0, 1, 1
# Stations while going up:
# 1, 7, 2, 3
# Stations while going down:
# 4, 2, 7, 1