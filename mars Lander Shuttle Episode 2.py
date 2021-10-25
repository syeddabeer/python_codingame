import sys
import math
import numpy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.

land_x=numpy.zeros(surface_n)
land_y=numpy.zeros(surface_n)

for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x[i], land_y[i] = [int(j) for j in input().split()]

land_start=0
land_end=0
land_height=0

for i in range(surface_n-1):
    if land_y[i]==land_y[i+1] and land_x[i+1]-land_x[i]>=1000:
        land_start=land_x[i]
        land_end=land_x[i+1]
        land_height=land_y[i]

    
    


# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    
    
    t_estimate=(y-land_height)/39
    
    
    
    if h_speed-t_estimate>18 and t_estimate>1:
        power=4
        rotate=180*math.acos(3.711/4)/math.pi
    elif h_speed+t_estimate<-18 and t_estimate>1:
        power=4
        rotate=-180*math.acos(3.711/4)/math.pi

    elif x+h_speed*t_estimate>land_start and x+h_speed*t_estimate<land_end: 
        rotate=0
        

        if v_speed+power-4<=-39: power=4
        else: power=0
    elif x+h_speed*t_estimate<=land_start:
        if v_speed<0:
            power=4
        else:
            power=3
        if h_speed<19:
            rotate=-180*math.acos(3.711/4)/math.pi
        else:
            rotate=0
    else:
        if v_speed<0:
            power=4
        else:
            power=3
        if h_speed>-19:
            rotate=180*math.acos(3.711/4)/math.pi
        else:
            rotate=0
        
    

    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    print(str(int(rotate))+" "+str(power))