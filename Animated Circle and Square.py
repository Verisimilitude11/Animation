import pygame
pygame.init()

window = pygame.display.set_mode([600, 400])
window.fill((255, 255, 255))

r = pygame.Rect(300, 150, 25, 25)

b = (0, 0, 0)
offset = 0
while (50 + offset) < 600:

    window.fill((255, 255, 255))
    
    r.x = 300 + offset
    r.y = 150 + offset
    
    pygame.draw.circle(window, b, (50 + offset, 200), 20)
    pygame.draw.rect(window, (0, 0, 0), r)
    offset += 10
    pygame.time.wait(20)
    
    pygame.display.flip()

input("Press enter to close window")
