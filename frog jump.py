import math

nb_frogs = int(input())
distances = [float(dist) for dist in input().split()]

init_pos = input().split()
pos = (int(init_pos[0]), int(init_pos[1]))
mass = int(input())
alpha = int(input())
speed = float(input())
gravity = input().split()
gravity = (float(gravity[0]), float(gravity[1]))

def get_distance(pos, alpha, speed, gravity):
    speed_x = math.cos(math.radians(alpha)) * speed
    speed_y = math.sin(math.radians(alpha)) * speed

    delta = speed_y**2 - 4 * (gravity[1] * 1/2) * pos[1]

    time = (-speed_y - math.sqrt(delta)) / (2 * gravity[1] * 1/2)

    x = (gravity[0] * 1/2 * time**2) + (speed_x * time) + pos[0]
    x = round(x, 2)
    return x


my_jump = get_distance(pos, alpha, speed, gravity)
my_place = 1

for dist in distances:
    if dist > my_jump:
        my_place += 1

print(my_place)