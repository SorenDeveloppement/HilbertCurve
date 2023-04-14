import pygame
import math
import time

from pygame import Vector2

SQUARE = 1000

BACKGROUND = (10, 10, 10)
WHITE = (255, 255, 255)
COLOR = (0, 177, 255)

ORDER = 7
N = int(math.pow(2, ORDER))
TOTAL = N * N

COUNTER = 0

PATH: [Vector2] = [0] * TOTAL

rr = False
gr = False
br = False


def rainbowColor(color):
    global rr, gr, br
    red, green, blue = color

    if rr:
        if red <= 1:
            rr = False
            red = 2
        else:
            red -= 1
    else:
        if red >= 254:
            rr = True
            red = 253
        else:
            red += 1

    if gr:
        if green <= 1:
            gr = False
            green = 2
        else:
            green -= 1
    else:
        if green >= 254:
            gr = True
            green = 253
        else:
            green += 1

    if br:
        if blue <= 1:
            br = False
            blue = 2
        else:
            blue -= 1
    else:
        if blue >= 254:
            br = True
            blue = 253
        else:
            blue += 1

    return red, green, blue


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
            temp = lenth - 1 - v.x
            v.x = lenth - 1 - v.y
            v.y = temp

            v.x += lenth

    return v


def checkQuitEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return


def main():
    global PATH, COUNTER, COLOR
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
        checkQuitEvent()

        screen.fill(BACKGROUND)

        if COUNTER == len(PATH):
            COUNTER = 0
        COUNTER += 10
        if COUNTER >= len(PATH):
            COUNTER = len(PATH)

        for i in range(len(PATH) - 1):
            if (i % (N/4)) == 0:
                COLOR = rainbowColor(COLOR)
            pygame.draw.line(screen, COLOR, (PATH[i].x, PATH[i].y), (PATH[i + 1].x, PATH[i + 1].y), 2)
            """time.sleep(0.00000001)
            pygame.display.update()
            checkQuitEvent()"""

        pygame.display.update()


if __name__ == '__main__':
    main()
