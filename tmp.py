import sys
import math
import random

# Grab the pellets as fast as you can!
class Entity:
    def __init__(self, x, y):
        self.x: int = int(x)
        self.y: int = int(y)

class Pellet(Entity):
    def __init__(self, x, y, value):
        super().__init__(x, y)
        self.value = int(value)

    def __repr__(self) -> str:
        return f"Pellet(x:{self.x}, y:{self.y}, value:{self.value})"

class Pacman(Entity):
    def __init__(self, pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown):
        super().__init__(x, y)
        self.pac_id: int = int(pac_id)
        self.mine: int = int(mine)
        self.type_id: str = type_id
        self.speed_turns_left: int = int(speed_turns_left)
        self.ability_cooldown: int = int(ability_cooldown)

    def isMine(self) -> bool:
        return self.mine == 1

    def isSomeoneInFront(self, scan_distance: int) -> bool:
        return False

    def __repr__(self) -> str:
        return f"Pacman(x:{self.x}, y:{self.y})"

# width: size of the grid
# height: top left corner is (x=0, y=0)
width, height = [int(i) for i in input().split()]
for i in range(height):
    row = input()  # one line of the grid: space " " is floor, pound "#" is wall
    print(row, file=sys.stderr)
# game loop
while True:
    my_score, opponent_score = [int(i) for i in input().split()]
    visible_pac_count = int(input())  # all your pacs and enemy pacs in sight

    print(f"visible pac count {visible_pac_count}", file=sys.stderr)

    pacmans = list(
        Pacman(*input().split())
        for i in range(visible_pac_count))
    print(f"pacmans: {pacmans}", file=sys.stderr)
    # Keep only pacman whoses mine
    my_pacmans = list(filter(lambda x: x.isMine(), pacmans))
    print(f"my pacmans: {my_pacmans}", file=sys.stderr)
    visible_pellet_count = int(input())  # all pellets in sight
    pellets = sorted(
        set( # list of all pellets
            Pellet(*input().split())
            for i in range(visible_pellet_count)
            ),
        key=lambda x: x.value,
        reverse=True
        )
    print(f"pellets: {pellets}", file=sys.stderr)
    orders = list(zip(my_pacmans, pellets))
    print(f"targets: {orders}", file=sys.stderr)
    order = ""
    for order_actor, order_target in orders:
        order+=f"MOVE {order_actor.pac_id} {order_target.x} {order_target.y}|"
    
    print(order[:-1])

