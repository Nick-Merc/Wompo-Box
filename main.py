from wompobox import WompoBox
from entity import Entity

WIDTH = 500
HEIGHT = 500

wompobox = WompoBox(WIDTH, HEIGHT)

dwarf = Entity(5, 5, "Dwarf")
wompobox.addEntity(dwarf)

wompobox.run()