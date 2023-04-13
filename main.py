import pygame
import math
import time

from pygame import Vector2

SQUARE = 600

BACKGROUND = (10, 10, 10)
WHITE = (255, 255, 255)

ORDER = 6
N = int(math.pow(2, ORDER))
TOTAL = N * N

COUNTER = 0

PATH: [Vector2] = [0] * TOTAL


def hilbert(i: int) -> Vector2:
    points: [Vector2] = [
        Vector2(0, 0),
        Vector2(0, 1),
        Vector2(1, 1),
        Vector2(1, 0)
    ]

    index = i & 3
    v: Vector2 = points[index]

    for j in range(1, ORDER):
        i = i >> 2
        index = i & 3

        lenth: float = math.pow(2, j)
        if index == 0:
            temp = v.x
            v.x = v.y
            v.y = temp
        elif index == 1:
            v.y += lenth
        elif index == 2:
            v.y += lenth
            v.x += lenth
        elif index == 3:
            temp = lenth-1-v.x
            v.x = lenth-1-v.y
            v.y = temp

            v.x += lenth

    return v


def main():
    global PATH, COUNTER
    pygame.init()
    screen = pygame.display.set_mode((SQUARE, SQUARE))

    for i in range(TOTAL):
        PATH[i] = hilbert(i)
        lenth = SQUARE / N
        PATH[i].x *= lenth
        PATH[i].y *= lenth
        PATH[i].x += lenth / 2
        PATH[i].y += lenth / 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            screen.fill(BACKGROUND)

            for i in range(COUNTER - 1):
                pygame.draw.line(screen, WHITE, (PATH[i].x, PATH[i].y), (PATH[i + 1].x, PATH[i + 1].y), 2)

            COUNTER += 1
            if COUNTER == len(PATH) + 1:
                COUNTER = 0

            pygame.display.flip()
            pygame.display.update()


if __name__ == '__main__':
    main()
