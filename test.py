import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello, world!")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((100, 60, 25))
clock = pygame.time.Clock()
keepGoing = True
color = (100, 100, 100)
size = (150, 50)
pos = (50, 50)
# Set up main loop
while keepGoing:
    # Timer to set frame rate
    clock.tick(30)
    touch = pygame.mouse.get_pos()
    bar = pygame.Surface(size)
    bar = bar.convert()
    bar.fill(color)
    bar.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if touch[0] >= 50 and touch[0] <= 200 and touch[1] >= 50 and touch[1] <= 100:

            if event.type == pygame.MOUSEBUTTONDOWN:
                color = (50, 50, 50)
                size = (160, 60)
                pos = (45, 45)
            if event.type == pygame.MOUSEBUTTONUP:
                color = (100, 100, 100)
                size = (150, 50)
                pos = (50, 50)

    screen.blit(background, (0, 0))
    screen.blit(bar, pos)

    pygame.display.flip()