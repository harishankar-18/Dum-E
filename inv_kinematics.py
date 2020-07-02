import numpy as np
import math

position_0 = []
position_2 = []

for i in range(2):
    position_0.append(float(input()))
    
for i in range(2):
    position_2.append(float(input())
    
length_1 = float(input())
length_2 = float(input())

pos0 = np.array(position_0)
pos2 = np.array(position_2)

alpha = math.atan(pos2[1]/pos2[0])

offset=pos0
pos2=pos2-pos0
pos0=pos0-pos0
length_3=(pos2[0]**2+pos2[1]**2)**0.5

theta2 = m.acos((length_3**2-l1**2-l2**2)/(2*l1*l2))

beta = m.atan((l2*m.sin(theta2))/(l1+l2*m.cos(theta2)))

theta1 = alpha - beta

p1 = np.zeros(2)
p1[0] = length_1*math.cos(theta1)
p1[1] = length_11*math.sin(theta1)

print("theta1: ",theta1)
print("theta2: ",theta2)
p1 = np.asarray(p1)
print(p1)
  
