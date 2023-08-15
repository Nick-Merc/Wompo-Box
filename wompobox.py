import pygame
import entity
from position import Position

class WompoBox:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.dwarf = None
        self.entities = []

    def setDwarf(self, dwarf):
        self.dwarf = dwarf

    def addEntity(self, entity):
        self.entities.append(entity)

    def initialize(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('WompoBox Window')

        self.background_image = pygame.transform.scale(pygame.image.load("media/background.png").convert(), (self.width, self.height))

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
            x = entity.position.x - SQUARE_SIZE / 2
            y = entity.position.y - SQUARE_SIZE / 2
            # create a rectangle object with the coordinates and size
            rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
            # draw the rectangle on the surface
            pygame.draw.rect(self.screen, GREEN, rect)

    def drawAll(self):
        self.drawBackground()
        self.drawEntities()

        pygame.display.flip()

    def getMovement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            return (0, -1)
        elif keys[pygame.K_DOWN]:
            return (0, 1)
        elif keys[pygame.K_LEFT]:
            return (-1, 0)
        elif keys[pygame.K_RIGHT]:
            return (1, 0)
        else:
            return (0, 0)

    def newPosition(self, current_position, movement):
        x = current_position.x
        y = current_position.y
        dx = movement[0]
        dy = movement[1]
        return(Position(x + dx, y + dy))

    def validPosition(self, newPos):
        if 0 <= newPos.x <= self.width and 0 <= newPos.y <= self.height:
            return True
        else:
            return False


    def run(self):
        self.initialize()
        
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            movement = self.getMovement()
            newPos = self.newPosition(self.entities[0].position, movement)
            if self.validPosition(newPos):
                self.entities[0].position = newPos

            self.drawAll()
                    
        pygame.quit()
