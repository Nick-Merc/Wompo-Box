import pygame
import entity

class WompoBox:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.entities = []
        self.tilemap = [] # WidthXHeight matrix of 'o' characters, will be used to draw respective tile.

    def addEntity(self, entity):
        self.entities.append(entity)

    def initialize(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('WompoBox Window')

        self.background_image = pygame.image.load("media/background.png").convert()

    def drawBackground(self):
        self.screen.blit(self.background_image, (0, 0))

    def drawEntities(self):
        for entity in self.entities:
            # draw green square at entity.position
            # define the size of the square
            SQUARE_SIZE = 20
            # get the color of green
            GREEN = (0, 255, 0)
            # calculate the top-left corner of the square
            x = entity.x - SQUARE_SIZE / 2
            y = entity.y - SQUARE_SIZE / 2
            # create a rectangle object with the coordinates and size
            rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
            # draw the rectangle on the surface
            pygame.draw.rect(self.screen, GREEN, rect)

    def loadAll(self):
        # Reflect all entities in the tilemap.
        for entity in self.entities:
            self.tilemap[entity.position.y][entity.position.x] = entity.name[0]

    def drawAll(self):
        self.drawBackground()
        self.drawEntities()

        pygame.display.flip()

    def run(self):
        self.initialize()
        
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.drawAll()
                    
        pygame.quit()
