import pygame

class WompoBox:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.entities = []

    def addEntity(entity):
        self.entities.append(entity)

    def initialize(self):
        pygame.init()

    def run(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('WompoBox Window')
        
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
        pygame.quit()
