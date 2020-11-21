import pygame

#COLORS:

GREEN = (147,193,26)
ORANGE = (235,176,73)
BLUE = (0,0,0)

#SCREEN VARIABLES:

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
loop = True

pygame.init()
timer = pygame.time.Clock()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
screen_title = "Ping Pong dla 2 Graczy"
pygame.display.set_caption(screen_title)

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,75])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.points = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()

paddle1 = Paddle()
paddle1.rect.x = 25
paddle1.rect.y = 225

paddle2 = Paddle()
paddle2.rect.x = 715
paddle2.rect.y = 225

pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

allSprites = pygame.sprite.Group()
allSprites.add(paddle1, paddle2, pong)

def redraw():
    screen.fill(BLUE)
    allSprites.draw(screen)
    pygame.display.update()

while loop:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    redraw()
    pygame.display.update()
    timer.tick(60)

pygame.quit()