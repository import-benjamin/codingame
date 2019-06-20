import sys
import math

# Save the Planet.
# Use less Fossil Fuel.
base_start = 0
old_y = 0
old_x = 0


class Path:
    
    def __init__(this):
        this.rotation = 0
        this.power = 0
    
    def getOrientation(this, base_start, x):
        return "-60" if base_start > x else "20" if base_start < x else "0"
    
    def getPower(this, vs, base_start, x):
        this.power += 1 if vs < -35 and this.power < 4 else -1 if vs > 0 and this.power < 0 else 0
        this.power = 2 if base_start > x else this.power
        return this.power
    
    def toString(this, base_start, x, vs):
        return this.getOrientation(base_start, x) + " " + str(this.getPower(vs, base_start, x))

n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    
    base_start = old_x if land_y == old_y else base_start
    old_x, old_y= land_x, land_y
    

# game loop
while True:
    # hs: the horizontal speed (in m/s), can be negative.
    # vs: the vertical speed (in m/s), can be negative.
    # f: the quantity of remaining fuel in liters.
    # r: the rotation angle in degrees (-90 to 90).
    # p: the thrust power (0 to 4).
    x, y, hs, vs, f, r, p = [int(i) for i in input().split()]
    
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    path = Path()
    print(path.toString(base_start, x, vs))

    # R P. R is the desired rotation angle. P is the desired thrust power.
