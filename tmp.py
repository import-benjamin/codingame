import sys
import math
import random
from typing import List
import copy
# Grab the pellets as fast as you can!

class Entity:
    
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)
    
    def get_pos(self) -> tuple:
        return self.x, self.y
    
    def __str__():
        return "E"


class Wall(Entity):

    def __init__(self, x, y):
        super().__init__(x, y)
    
    def __str__(self) -> str:
        return "#"

class Pellet(Entity):

    def __init__(self, x: int, y:int, value: int):
        super().__init__(x, y)
        self.value = int(value)

    def __str__(self) -> str:
        return "O" if self.value == 10 else "o"

class Air(Pellet):
    # Since pacman is able to pass through air we consider them as pellet of 0
    def __init__(self, x: int, y: int):
        super().__init__(x, y, 0)
    
    def __str__(self) -> str:
        return " "


class Map(List[List[Entity]]):
    def __init__(self, height: int, width: int):
        super().__init__()
        self.width = width
        self.height = height
        for x in range(self.width):
            self.append([
                Entity(x, y)
                for y in range(self.height)
            ])

    def init_line(self, y: int, line: str) -> bool:
        for i, c in enumerate(line):
            if c is '#': self.set_entity(Wall(i, y))
            if c is ' ': self.set_entity(Air(i, y))
    
    def set_entity(self, entity: Entity) -> bool:
        x, y = entity.get_pos()
        self[x][y] = entity
        return True
    
    def set_entities(self, entities: List[Entity]) -> bool:
        for entity in entities:
            self.set_entity(entity)
    
    def get_entity(x: int, y: int) -> Entity:
        return self[x][y]

    def __str__(self):
        str_map = ""
        for y in range(self.height):
            for x in range(self.width):
                str_map += str(self[x][y])
            str_map += '\n'
        return str_map

class Pacman(Entity):
    def __init__(self, pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown):
        super().__init__(x, y)
        self.pac_id: int = int(pac_id)
        self.mine: int = int(mine)
        self.type_id: str = type_id
        self.speed_turns_left: int = int(speed_turns_left)
        self.ability_cooldown: int = int(ability_cooldown)


    def scan_nearby(self, x: int, y: int, current_map: Map) -> tuple:
        valid_nodes = []
        for _x, _y in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            entity = current_map.get_entity(_x, _y)
            if type(entity) is any(Pellet, Air):
                valid_nodes.append(entity)

    def compute_best_path(self, current_map: Map) -> tuple:
        x, y = self.get_pos()
        nodes = self.scan_nearby(x, y, current_map)
        return tuple(nodes)



    def isMine(self) -> bool:
        return self.mine == 1

    def __str__(self) -> str:
        return f"C"



# width: size of the grid
# height: top left corner is (x=0, y=0)
width, height = [int(i) for i in input().split()]
party_map = Map(height, width)
for y in range(height):
    row = input()  # one line of the grid: space " " is floor, pound "#" is wall
    party_map.init_line(y, row)

print(str(party_map), file=sys.stderr)
# game loop
while True:
    current_map = copy.deepcopy(party_map)
    my_score, opponent_score = [int(i) for i in input().split()]
    visible_pac_count = int(input())  # all your pacs and enemy pacs in sight

    my_pacmans = []
    for i in range(visible_pac_count): # pacmans
        pacman = Pacman(*input().split())
        current_map.set_entity(pacman)
        if pacman.isMine:
            my_pacmans.append(pacman)
    
    for i in range(int(input())): # pellets
        pellet = Pellet(*input().split())
        current_map.set_entity(pellet)

    for pacman in my_pacmans:
        print(pacman.compute_best_path(current_map))

    print(str(current_map), file=sys.stderr)
    del(current_map)

