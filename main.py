import pygame
from card import Card

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((900, 900))
font1 = pygame.font.SysFont('freesanbold.ttf', 100)
pygame.display.init()
pygame.display.set_caption("Tower of Hanoi Solver")
cards = [Card(560, 10, 200, 280, 3), Card(350, 10, 200, 280, 2), Card(140, 10, 200, 280, 1)]

running = True
while running:
    m_pos = pygame.mouse.get_pos()
    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for c in cards:
        moved = []
        for c2 in cards:
            if not c2 == c:
                moved.append(c2.moving)
        if c.left < m_pos[0] < c.left + c.w and c.top < m_pos[1] < c.top + c.h and pygame.mouse.get_pressed()[0] and True not in moved:
            c.moving = True
            c.left = m_pos[0] - c.w / 2
            c.top = m_pos[1] - c.h / 2
        else:
            c.moving = False

        if not c.moving:
            pygame.draw.rect(win, (0, 0, 0), pygame.Rect(c.left - 5, c.top - 5, c.w + 10, c.h + 10))
            pygame.draw.rect(win, (255, 255, 255), c)
            win.blit(font1.render(str(c.number), True, (0, 0, 0)), c)

    for c in cards:
        if c.moving:
            pygame.draw.rect(win, (0, 0, 0), pygame.Rect(c.left - 5, c.top - 5, c.w + 10, c.h + 10))
            pygame.draw.rect(win, (255, 255, 255), c)
            win.blit(font1.render(str(c.number), True, (0, 0, 0)), c)


    pygame.display.flip()