from wompobox import WompoBox
from entity import Entity
from position import Position

WIDTH = 500
HEIGHT = 500

wompobox = WompoBox(WIDTH, HEIGHT)

dwarf = Entity(Position(200, 30), "Dwarf")
wompobox.addEntity(dwarf)

wompobox.run()