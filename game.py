import pygame
pygame.init()

screen = pygame.display.set_mode([800, 500])

running = true
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    pygame.display.flip()
print(running)