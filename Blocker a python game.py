import pygame, sys, random

#dope code

pygame.init()

WIDTH, HEIGHT = 1000, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blocker")

font1 = pygame.font.SysFont(None, 30)

class levels:
    def __init__(self, cLevel):
        self.cLevel = cLevel

class player:
    def __init__(self, colour, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.colour = colour

class enemy:
    def __init__(self, colour, x, y, height, width, speed):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.speed = speed

def drawText(text, colour, font, surface, x, y):
    textobj = font.render(text, 1, colour)
    textRect = textobj.get_rect()
    textRect.topleft = (x,y)
    surface.blit(textobj, textRect)

def menu():
    bu1 = player((0,255,0), 400, 300, 50, 200)
    bu2 = player((0,255,0), 400, 360, 50, 200)

    while True:
        win.fill((255,255,255))

        drawText("Bloker", (0,0,0), pygame.font.SysFont(None, 150), win, 350, 50)
        drawText("Game by Emaad Hakeem", (0,0,0), pygame.font.SysFont(None, 20), win, 840, 580)

        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(bu1.x, bu1.y, bu1.width, bu1.height)
        buttonHowTo = pygame.Rect(bu2.x, bu2.y, bu2.width, bu2.height)

        click = False
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        if button1.collidepoint((mx,my)):
            if click:
                level1()
        elif buttonHowTo.collidepoint((mx,my)):
            if click:
                howTo()

        pygame.draw.rect(win, bu1.colour, button1)
        pygame.draw.rect(win, bu1.colour, buttonHowTo)

        drawText("start", (255,255,255), font1, win, 420, 315)
        drawText("how to play", (255,255,255), font1, win, bu2.x + 20, bu2.y + 15)

        pygame.display.update()

def level1():
    levels.cLevel = 1

    pl1 = player((255,0,0),200, 200, 30, 30)
    en1 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 2)
    en2 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 2)

    points = 0

    while True:
        win.fill((255,255,255))
        drawText("Level 1", (0,0,0), font1, win, 400, 25)
        drawText("objective: to get 10 points", (0,0,0), font1, win, 400, 50)
        drawText(str(points), (0,0,0), font1, win, 900, 50)

        click = False
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        en1.x -= en1.speed
        en2.x -= en2.speed

        if en1.x < 0:
            en1.y = random.randint(20, HEIGHT-20)
            en1.x = WIDTH
            points+=1
        if en2.x < 0:
            en2.y = random.randint(20, HEIGHT-20)
            en2.x = WIDTH

        mx, my = pygame.mouse.get_pos()

        if 0 < mx < WIDTH-pl1.width and 0 < my < HEIGHT-pl1.height:
            pl1.x = mx
            pl1.y = my

        if pl1.x < en1.x < pl1.x+pl1.width and pl1.y < en1.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en2.x < pl1.x+pl1.width and pl1.y < en2.y < pl1.y+pl1.height:
            losingScreen()

        if points >= 10:
            winningScreen()

        pygame.draw.rect(win, pl1.colour, (pl1.x, pl1.y, pl1.width, pl1.height))
        pygame.draw.rect(win, en1.colour, (en1.x, en1.y, en1.width, en1.height))
        pygame.draw.rect(win, en2.colour, (en2.x, en2.y, en2.width, en2.height))

        pygame.display.update()

def level2():
    levels.cLevel = 2

    pl1 = player((255,0,0),200, 200, 30, 30)
    en1 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 2)
    en2 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 2)

    points = 0

    while True:
        win.fill((255,255,255))
        drawText("Level 2", (0,0,0), font1, win, 400, 25)
        drawText("objective: to get 20 points", (0,0,0), font1, win, 400, 50)
        drawText(str(points), (0,0,0), font1, win, 900, 50)

        click = False
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        en1.x -= en1.speed
        en2.x -= en2.speed

        if en1.x < 0:
            en1.y = random.randint(20, HEIGHT-20)
            en1.x = WIDTH
            points+=1
        if en2.x < 0:
            en2.y = random.randint(20, HEIGHT-20)
            en2.x = WIDTH

        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()

        if 0 < mx < WIDTH-pl1.width and 0 < my < HEIGHT-pl1.height:
            pl1.x = mx
            pl1.y = my

        if pl1.x < en1.x < pl1.x+pl1.width and pl1.y < en1.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en2.x < pl1.x+pl1.width and pl1.y < en2.y < pl1.y+pl1.height:
            losingScreen()

        if points >= 20:
            winningScreen()

        pygame.draw.rect(win, pl1.colour, (pl1.x, pl1.y, pl1.width, pl1.height))
        pygame.draw.rect(win, en1.colour, (en1.x, en1.y, en1.width, en1.height))
        pygame.draw.rect(win, en2.colour, (en2.x, en2.y, en2.width, en2.height))

        pygame.display.update()

def level3():
    levels.cLevel = 3

    pl1 = player((255,0,0),200, 200, 30, 30)
    en1 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 2)
    en2 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 2)
    en3 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 2)
    en4 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 2)

    points = 0

    while True:
        win.fill((255,255,255))
        drawText("Level 3", (0,0,0), font1, win, 400, 25)
        drawText("objective: to get 20 points", (0,0,0), font1, win, 400, 50)
        drawText(str(points), (0,0,0), font1, win, 900, 50)

        click = False
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        en1.x -= en1.speed
        en2.x -= en2.speed
        en3.x -= en3.speed
        en4.x -= en4.speed

        if en1.x < 0:
            en1.y = random.randint(20, HEIGHT-20)
            en1.x = WIDTH
            points+=1
        if en2.x < 0:
            en2.y = random.randint(20, HEIGHT-20)
            en2.x = WIDTH
        if en3.x < 0:
            en3.y = random.randint(20, HEIGHT-20)
            en3.x = WIDTH
        if en4.x < 0:
            en4.y = random.randint(20, HEIGHT-20)
            en4.x = WIDTH

        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()

        if 0 < mx < WIDTH-pl1.width and 0 < my < HEIGHT-pl1.height:
            pl1.x = mx
            pl1.y = my

        if pl1.x < en1.x < pl1.x+pl1.width and pl1.y < en1.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en2.x < pl1.x+pl1.width and pl1.y < en2.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en3.x < pl1.x+pl1.width and pl1.y < en3.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en4.x < pl1.x+pl1.width and pl1.y < en4.y < pl1.y+pl1.height:
            losingScreen()

        if points >= 20:
            winningScreen()

        pygame.draw.rect(win, pl1.colour, (pl1.x, pl1.y, pl1.width, pl1.height))
        pygame.draw.rect(win, en1.colour, (en1.x, en1.y, en1.width, en1.height))
        pygame.draw.rect(win, en2.colour, (en2.x, en2.y, en2.width, en2.height))
        pygame.draw.rect(win, en3.colour, (en3.x, en3.y, en3.width, en3.height))
        pygame.draw.rect(win, en4.colour, (en4.x, en4.y, en4.width, en4.height))

        pygame.display.update()

def level4():
    levels.cLevel = 4

    pl1 = player((255,0,0),200, 200, 30, 30)
    en1 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)
    en2 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)
    en3 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)
    en4 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)

    points = 0

    while True:
        win.fill((255,255,255))
        drawText("Level 4", (0,0,0), font1, win, 400, 25)
        drawText("objective: to get 25 points", (0,0,0), font1, win, 400, 50)
        drawText(str(points), (0,0,0), font1, win, 900, 50)

        click = False
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        en1.x -= en1.speed
        en2.x -= en2.speed
        en3.x -= en3.speed
        en4.x -= en4.speed

        if en1.x < 0:
            en1.y = random.randint(20, HEIGHT-20)
            en1.x = WIDTH
            points+=1
        if en2.x < 0:
            en2.y = random.randint(20, HEIGHT-20)
            en2.x = WIDTH
        if en3.x < 0:
            en3.y = random.randint(20, HEIGHT-20)
            en3.x = WIDTH
        if en4.x < 0:
            en4.y = random.randint(20, HEIGHT-20)
            en4.x = WIDTH

        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()

        if 0 < mx < WIDTH-pl1.width and 0 < my < HEIGHT-pl1.height:
            pl1.x = mx
            pl1.y = my

        if pl1.x < en1.x < pl1.x+pl1.width and pl1.y < en1.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en2.x < pl1.x+pl1.width and pl1.y < en2.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en3.x < pl1.x+pl1.width and pl1.y < en3.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en4.x < pl1.x+pl1.width and pl1.y < en4.y < pl1.y+pl1.height:
            losingScreen()

        if points >= 25:
            winningScreen()

        pygame.draw.rect(win, pl1.colour, (pl1.x, pl1.y, pl1.width, pl1.height))
        pygame.draw.rect(win, en1.colour, (en1.x, en1.y, en1.width, en1.height))
        pygame.draw.rect(win, en2.colour, (en2.x, en2.y, en2.width, en2.height))
        pygame.draw.rect(win, en3.colour, (en3.x, en3.y, en3.width, en3.height))
        pygame.draw.rect(win, en4.colour, (en4.x, en4.y, en4.width, en4.height))

        pygame.display.update()

def level5():
    levels.cLevel = 5

    pl1 = player((255,0,0),200, 200, 30, 30)
    en1 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 4)
    en2 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)
    en3 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 4)
    en4 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)

    points = 0

    while True:
        win.fill((255,255,255))
        drawText("Level 5", (0,0,0), font1, win, 400, 25)
        drawText("objective: to get 30 points", (0,0,0), font1, win, 400, 50)
        drawText(str(points), (0,0,0), font1, win, 900, 50)

        click = False
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        en1.x -= en1.speed
        en2.x -= en2.speed
        en3.x -= en3.speed
        en4.x -= en4.speed

        if en1.x < 0:
            en1.y = random.randint(20, HEIGHT-20)
            en1.x = WIDTH
            points+=1
        if en2.x < 0:
            en2.y = random.randint(20, HEIGHT-20)
            en2.x = WIDTH
        if en3.x < 0:
            en3.y = random.randint(20, HEIGHT-20)
            en3.x = WIDTH
        if en4.x < 0:
            en4.y = random.randint(20, HEIGHT-20)
            en4.x = WIDTH

        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()

        if 0 < mx < WIDTH-pl1.width and 0 < my < HEIGHT-pl1.height:
            pl1.x = mx
            pl1.y = my

        if pl1.x < en1.x < pl1.x+pl1.width and pl1.y < en1.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en2.x < pl1.x+pl1.width and pl1.y < en2.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en3.x < pl1.x+pl1.width and pl1.y < en3.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en4.x < pl1.x+pl1.width and pl1.y < en4.y < pl1.y+pl1.height:
            losingScreen()

        if points >= 30:
            winningScreen()

        pygame.draw.rect(win, pl1.colour, (pl1.x, pl1.y, pl1.width, pl1.height))
        pygame.draw.rect(win, en1.colour, (en1.x, en1.y, en1.width, en1.height))
        pygame.draw.rect(win, en2.colour, (en2.x, en2.y, en2.width, en2.height))
        pygame.draw.rect(win, en3.colour, (en3.x, en3.y, en3.width, en3.height))
        pygame.draw.rect(win, en4.colour, (en4.x, en4.y, en4.width, en4.height))

        pygame.display.update()

def level6():
    levels.cLevel = 6

    pl1 = player((255,0,0),200, 200, 30, 30)
    en1 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 4)
    en2 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)
    en3 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 4)
    en4 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)
    en5 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)

    points = 0

    while True:
        win.fill((255,255,255))
        drawText("Level 6", (0,0,0), font1, win, 400, 25)
        drawText("objective: to get 15 points", (0,0,0), font1, win, 400, 50)
        drawText(str(points), (0,0,0), font1, win, 900, 50)

        click = False
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        en1.x -= en1.speed
        en2.x -= en2.speed
        en3.x -= en3.speed
        en4.x -= en4.speed
        en5.x -= en5.speed

        if en1.x < 0:
            en1.y = random.randint(20, HEIGHT-20)
            en1.x = WIDTH
            points+=1
        if en2.x < 0:
            en2.y = random.randint(20, HEIGHT-20)
            en2.x = WIDTH
        if en3.x < 0:
            en3.y = random.randint(20, HEIGHT-20)
            en3.x = WIDTH
        if en4.x < 0:
            en4.y = random.randint(20, HEIGHT-20)
            en4.x = WIDTH
        if en5.x < 0:
            en5.y = random.randint(20, HEIGHT-20)
            en5.x = WIDTH

        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()

        if 0 < mx < WIDTH-pl1.width and 0 < my < HEIGHT-pl1.height:
            pl1.x = mx
            pl1.y = my

        if pl1.x < en1.x < pl1.x+pl1.width and pl1.y < en1.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en2.x < pl1.x+pl1.width and pl1.y < en2.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en3.x < pl1.x+pl1.width and pl1.y < en3.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en4.x < pl1.x+pl1.width and pl1.y < en4.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en5.x < pl1.x+pl1.width and pl1.y < en5.y < pl1.y+pl1.height:
            losingScreen()

        if points >= 15:
            winningScreen()

        pygame.draw.rect(win, pl1.colour, (pl1.x, pl1.y, pl1.width, pl1.height))
        pygame.draw.rect(win, en1.colour, (en1.x, en1.y, en1.width, en1.height))
        pygame.draw.rect(win, en2.colour, (en2.x, en2.y, en2.width, en2.height))
        pygame.draw.rect(win, en3.colour, (en3.x, en3.y, en3.width, en3.height))
        pygame.draw.rect(win, en4.colour, (en4.x, en4.y, en4.width, en4.height))
        pygame.draw.rect(win, en5.colour, (en5.x, en5.y, en5.width, en5.height))

        pygame.display.update()

def level7():
    levels.cLevel = 7

    pl1 = player((255,0,0),200, 200, 30, 30)
    en1 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 4)
    en2 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)
    en3 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 4)
    en4 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)
    en5 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)

    points = 0

    while True:
        win.fill((255,255,255))
        drawText("Level 7", (0,0,0), font1, win, 400, 25)
        drawText("objective: to get 20 points", (0,0,0), font1, win, 400, 50)
        drawText(str(points), (0,0,0), font1, win, 900, 50)

        click = False
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        en1.x -= en1.speed
        en2.x -= en2.speed
        en3.x -= en3.speed
        en4.x -= en4.speed
        en5.x -= en5.speed

        if en1.x < 0:
            en1.y = random.randint(20, HEIGHT-20)
            en1.x = WIDTH
            points+=1
        if en2.x < 0:
            en2.y = random.randint(20, HEIGHT-20)
            en2.x = WIDTH
        if en3.x < 0:
            en3.y = random.randint(20, HEIGHT-20)
            en3.x = WIDTH
        if en4.x < 0:
            en4.y = random.randint(20, HEIGHT-20)
            en4.x = WIDTH
        if en5.x < 0:
            en5.y = random.randint(20, HEIGHT-20)
            en5.x = WIDTH

        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()

        if 0 < mx < WIDTH-pl1.width and 0 < my < HEIGHT-pl1.height:
            pl1.x = mx
            pl1.y = my

        if pl1.x < en1.x < pl1.x+pl1.width and pl1.y < en1.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en2.x < pl1.x+pl1.width and pl1.y < en2.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en3.x < pl1.x+pl1.width and pl1.y < en3.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en4.x < pl1.x+pl1.width and pl1.y < en4.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en5.x < pl1.x+pl1.width and pl1.y < en5.y < pl1.y+pl1.height:
            losingScreen()

        if points >= 20:
            winningScreen()

        pygame.draw.rect(win, pl1.colour, (pl1.x, pl1.y, pl1.width, pl1.height))
        pygame.draw.rect(win, en1.colour, (en1.x, en1.y, en1.width, en1.height))
        pygame.draw.rect(win, en2.colour, (en2.x, en2.y, en2.width, en2.height))
        pygame.draw.rect(win, en3.colour, (en3.x, en3.y, en3.width, en3.height))
        pygame.draw.rect(win, en4.colour, (en4.x, en4.y, en4.width, en4.height))
        pygame.draw.rect(win, en5.colour, (en5.x, en5.y, en5.width, en5.height))

        pygame.display.update()

def level8():
    levels.cLevel = 8

    pl1 = player((255,0,0),200, 200, 30, 30)
    en1 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 4)
    en2 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)
    en3 = enemy((0,0,0), random.randint(20, HEIGHT - 20), 0, 10, 10, 4)
    en4 = enemy((0,0,0), random.randint(20, HEIGHT - 20), 0, 10, 10, 3)

    points = 0

    while True:
        win.fill((255,255,255))
        drawText("Level 8", (0,0,0), font1, win, 400, 25)
        drawText("objective: to get 10 points", (0,0,0), font1, win, 400, 50)
        drawText(str(points), (0,0,0), font1, win, 900, 50)

        click = False
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        en1.x -= en1.speed
        en2.x -= en2.speed
        en3.y += en3.speed
        en4.y += en4.speed

        if en1.x < 0:
            en1.y = random.randint(20, HEIGHT-20)
            en1.x = WIDTH
            points+=1
        if en2.x < 0:
            en2.y = random.randint(20, HEIGHT-20)
            en2.x = WIDTH
        if en3.y > HEIGHT:
            en3.x = random.randint(20, WIDTH-20)
            en3.y = 0
        if en4.y > HEIGHT:
            en4.x = random.randint(20, WIDTH-20)
            en4.y = 0

        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()

        if 0 < mx < WIDTH-pl1.width and 0 < my < HEIGHT-pl1.height:
            pl1.x = mx
            pl1.y = my

        if pl1.x < en1.x < pl1.x+pl1.width and pl1.y < en1.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en2.x < pl1.x+pl1.width and pl1.y < en2.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en3.x < pl1.x+pl1.width and pl1.y < en3.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en4.x < pl1.x+pl1.width and pl1.y < en4.y < pl1.y+pl1.height:
            losingScreen()

        if points >= 10:
            winningScreen()

        pygame.draw.rect(win, pl1.colour, (pl1.x, pl1.y, pl1.width, pl1.height))
        pygame.draw.rect(win, en1.colour, (en1.x, en1.y, en1.width, en1.height))
        pygame.draw.rect(win, en2.colour, (en2.x, en2.y, en2.width, en2.height))
        pygame.draw.rect(win, en3.colour, (en3.x, en3.y, en3.width, en3.height))
        pygame.draw.rect(win, en4.colour, (en4.x, en4.y, en4.width, en4.height))

        pygame.display.update()

def level9():
    levels.cLevel = 9

    pl1 = player((255,0,0),200, 200, 30, 30)
    en1 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 4)
    en2 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)
    en3 = enemy((0,0,0), random.randint(20, HEIGHT - 20), 0, 10, 10, 4)
    en4 = enemy((0,0,0), random.randint(20, HEIGHT - 20), 0, 10, 10, 3)

    points = 0

    while True:
        win.fill((255,255,255))
        drawText("Level 9", (0,0,0), font1, win, 400, 25)
        drawText("objective: to get 20 points", (0,0,0), font1, win, 400, 50)
        drawText(str(points), (0,0,0), font1, win, 900, 50)

        click = False
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        en1.x -= en1.speed
        en2.x -= en2.speed
        en3.y += en3.speed
        en4.y += en4.speed

        if en1.x < 0:
            en1.y = random.randint(20, HEIGHT-20)
            en1.x = WIDTH
            points+=1
        if en2.x < 0:
            en2.y = random.randint(20, HEIGHT-20)
            en2.x = WIDTH
        if en3.y > HEIGHT:
            en3.x = random.randint(20, WIDTH-20)
            en3.y = 0
        if en4.y > HEIGHT:
            en4.x = random.randint(20, WIDTH-20)
            en4.y = 0

        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()

        if 0 < mx < WIDTH-pl1.width and 0 < my < HEIGHT-pl1.height:
            pl1.x = mx
            pl1.y = my

        if pl1.x < en1.x < pl1.x+pl1.width and pl1.y < en1.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en2.x < pl1.x+pl1.width and pl1.y < en2.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en3.x < pl1.x+pl1.width and pl1.y < en3.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en4.x < pl1.x+pl1.width and pl1.y < en4.y < pl1.y+pl1.height:
            losingScreen()

        if points >= 20:
            winningScreen()

        pygame.draw.rect(win, pl1.colour, (pl1.x, pl1.y, pl1.width, pl1.height))
        pygame.draw.rect(win, en1.colour, (en1.x, en1.y, en1.width, en1.height))
        pygame.draw.rect(win, en2.colour, (en2.x, en2.y, en2.width, en2.height))
        pygame.draw.rect(win, en3.colour, (en3.x, en3.y, en3.width, en3.height))
        pygame.draw.rect(win, en4.colour, (en4.x, en4.y, en4.width, en4.height))

        pygame.display.update()

def level10():
    levels.cLevel = 10

    pl1 = player((255,0,0),200, 200, 30, 30)
    en1 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 4)
    en2 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)
    en6 = enemy((0,0,0), WIDTH, random.randint(20, HEIGHT - 20), 10, 10, 3)
    en3 = enemy((0,0,0), random.randint(20, HEIGHT - 20), 0, 10, 10, 4)
    en4 = enemy((0,0,0), random.randint(20, HEIGHT - 20), 0, 10, 10, 3)
    en5 = enemy((0,0,0), random.randint(20, HEIGHT - 20), 0, 10, 10, 3)
    

    points = 0

    while True:
        win.fill((255,255,255))
        drawText("Level 9", (0,0,0), font1, win, 400, 25)
        drawText("objective: to get 30 points", (0,0,0), font1, win, 400, 50)
        drawText(str(points), (0,0,0), font1, win, 900, 50)

        click = False
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        en1.x -= en1.speed
        en2.x -= en2.speed
        en3.y += en3.speed
        en4.y += en4.speed
        en5.y += en5.speed
        en6.y += en6.speed

        if en1.x < 0:
            en1.y = random.randint(20, HEIGHT-20)
            en1.x = WIDTH
            points+=1
        if en2.x < 0:
            en2.y = random.randint(20, HEIGHT-20)
            en2.x = WIDTH
        if en6.x < 0:
            en6.y = random.randint(20, HEIGHT-20)
            en6.x = WIDTH
        if en3.y > HEIGHT:
            en3.x = random.randint(20, WIDTH-20)
            en3.y = 0
        if en4.y > HEIGHT:
            en4.x = random.randint(20, WIDTH-20)
            en4.y = 0
        if en5.y > HEIGHT:
            en5.x = random.randint(20, WIDTH-20)
            en5.y = 0

        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()

        if 0 < mx < WIDTH-pl1.width and 0 < my < HEIGHT-pl1.height:
            pl1.x = mx
            pl1.y = my

        if pl1.x < en1.x < pl1.x+pl1.width and pl1.y < en1.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en2.x < pl1.x+pl1.width and pl1.y < en2.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en3.x < pl1.x+pl1.width and pl1.y < en3.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en4.x < pl1.x+pl1.width and pl1.y < en4.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en5.x < pl1.x+pl1.width and pl1.y < en5.y < pl1.y+pl1.height:
            losingScreen()
        if pl1.x < en6.x < pl1.x+pl1.width and pl1.y < en6.y < pl1.y+pl1.height:
            losingScreen()

        if points >= 20:
            finalScreen()

        pygame.draw.rect(win, pl1.colour, (pl1.x, pl1.y, pl1.width, pl1.height))
        pygame.draw.rect(win, en1.colour, (en1.x, en1.y, en1.width, en1.height))
        pygame.draw.rect(win, en2.colour, (en2.x, en2.y, en2.width, en2.height))
        pygame.draw.rect(win, en3.colour, (en3.x, en3.y, en3.width, en3.height))
        pygame.draw.rect(win, en4.colour, (en4.x, en4.y, en4.width, en4.height))
        pygame.draw.rect(win, en5.colour, (en5.x, en5.y, en5.width, en5.height))
        pygame.draw.rect(win, en6.colour, (en6.x, en6.y, en6.width, en6.height))

        pygame.display.update()

def losingScreen():
    bu1 = player((0,255,0), 400, 300, 50, 200)
    bu2 = player((0,255,0), 400, 360, 50, 200)
    bu3 = player((0,255,0), 400, 420, 50, 200)

    while True:
        win.fill((255,255,255))

        click = False
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True        

        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(bu1.x, bu1.y, bu1.width, bu1.height)
        buttonQuitGame = pygame.Rect(bu2.x, bu2.y, bu2.width, bu2.height)
        buttonMenu = pygame.Rect(bu3.x, bu3.y, bu3.width, bu3.height)

        if button1.collidepoint((mx, my)):
            if click:
                if levels.cLevel == 1:
                    level1()
                elif levels.cLevel == 2:
                    level2()
                elif levels.cLevel == 3:
                    level3()
                elif levels.cLevel == 4:
                    level4()
                elif levels.cLevel == 5:
                    level5()
                elif levels.cLevel == 6:
                    level6()
                elif levels.cLevel == 7:
                    level7()
                elif levels.cLevel == 8:
                    level8()
                elif levels.cLevel == 9:
                    level9()
                elif levels.cLevel == 10:
                    level10()
        elif buttonQuitGame.collidepoint((mx,my)):
            if click:
                sys.exit()
        elif buttonMenu.collidepoint((mx,my)):
            if click:
                menu()

        pygame.draw.rect(win, bu1.colour, button1)
        pygame.draw.rect(win, bu2.colour, buttonQuitGame)
        pygame.draw.rect(win, bu2.colour, buttonMenu)

        drawText("Try Again", (0,0,0), pygame.font.SysFont(None, 150), win, 350, 50)
        drawText("restart level", (255,255,255), font1, win, 420, 315)
        drawText("quit", (255,255,255), font1, win, 430, 380)
        drawText("menu", (255,255,255), font1, win, bu3.x+20,bu3.y + 15)

        pygame.display.update()

def winningScreen():
    bu1 = player((0,255,0), 400, 300, 50, 200)
    bu2 = player((0,255,0), 400, 360, 50, 200)
    bu3 = player((0,255,0), 400, 420, 50, 200)

    while True:
        win.fill((255,255,255))

        mx, my = pygame.mouse.get_pos()

        buttonNextLevel = pygame.Rect(bu1.x, bu1.y, bu1.width, bu1.height)
        buttonRestartLevel = pygame.Rect(bu2.x, bu2.y, bu2.width, bu2.height)
        buttonMenu = pygame.Rect(bu3.x, bu3.y, bu3.width, bu3.height)

        click = False
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        if buttonNextLevel.collidepoint((mx,my)):
            if click:
                if levels.cLevel == 1:
                    level2()
                elif levels.cLevel == 2:
                    level3()
                elif levels.cLevel == 3:
                    level4()
                elif levels.cLevel == 4:
                    level5()
                elif levels.cLevel == 5:
                    level6()
                elif levels.cLevel == 6:
                    level7()
                elif levels.cLevel == 7:
                    level8()
                elif levels.cLevel == 8:
                    level9()
                elif levels.cLevel == 9:
                    level10()
        elif buttonRestartLevel.collidepoint((mx,my)):
            if click:
                if levels.cLevel == 1:
                    level1()
                elif levels.cLevel == 2:
                    level2()
                elif levels.cLevel == 3:
                    level3()
                elif levels.cLevel == 4:
                    level4()
                elif levels.cLevel == 5:
                    level5()
                elif levels.cLevel == 6:
                    level6()
                elif levels.cLevel == 7:
                    level7()
                elif levels.cLevel == 8:
                    level8()
                elif levels.cLevel == 9:
                    level9()
                elif levels.cLevel == 10:
                    level10()
        elif buttonMenu.collidepoint((mx,my)):
            if click:
                menu()

        pygame.draw.rect(win, bu1.colour, buttonNextLevel)
        pygame.draw.rect(win, bu2.colour, buttonRestartLevel)
        pygame.draw.rect(win, bu3.colour, buttonMenu)

        drawText("Amazing, now you have completed this level", (0,0,0), pygame.font.SysFont(None, 60), win, 50, 50)
        drawText("Next Level", (255,255,255), font1, win, 420, bu1.y + 15)
        drawText("Restart", (255,255,255), font1, win, 420, 375)
        drawText("Menu", (255,255,255), font1, win, 420, bu3.y + 15)

        pygame.display.update()

def AllLevels():

    l1 = player((0,255,0), 50, 50, 50, 200)
    l2 = player((0,255,0), 260, 50, 50, 200)
    l3 = player((0,255,0), 470, 50, 50, 200)
    l4 = player((0,255,0), 680, 50, 50, 200)
    l5 = player((0,255,0), 50, 110, 50, 200)
    l6 = player((0,255,0), 260, 110, 50, 200)
    l7 = player((0,255,0), 470, 110, 50, 200)
    l8 = player((0,255,0), 680, 110, 50, 200)
    l9 = player((0,255,0), 50, 170, 50, 200)
    l10 = player((0,255,0), 260, 170, 50, 200)

    while True:
        win.fill((255,255,255))

        mx, my = pygame.mouse.get_pos()

        buttonLevel1 = pygame.Rect(l1.x, l1.y, l1.width, l1.height)
        buttonLevel2 = pygame.Rect(l2.x, l2.y, l2.width, l2.height)
        buttonLevel3 = pygame.Rect(l3.x, l3.y, l3.width, l3.height)
        buttonLevel4 = pygame.Rect(l4.x, l4.y, l4.width, l4.height)
        buttonLevel5 = pygame.Rect(l5.x, l5.y, l5.width, l5.height)
        buttonLevel6 = pygame.Rect(l6.x, l6.y, l6.width, l6.height)
        buttonLevel7 = pygame.Rect(l7.x, l7.y, l7.width, l7.height)
        buttonLevel8 = pygame.Rect(l8.x, l8.y, l8.width, l8.height)
        buttonLevel9 = pygame.Rect(l9.x, l9.y, l9.width, l9.height)
        buttonLevel10 = pygame.Rect(l10.x, l10.y, l10.width, l10.height)

        click = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        if buttonLevel1.collidepoint((mx,my)):
            if click:
                level1()
        elif buttonLevel2.collidepoint((mx,my)):
            if click:
                level2()
        elif buttonLevel3.collidepoint((mx,my)):
            if click:
                level3()
        elif buttonLevel4.collidepoint((mx,my)):
            if click:
                level4()
        elif buttonLevel5.collidepoint((mx,my)):
            if click:
                level5()
        elif buttonLevel6.collidepoint((mx,my)):
            if click:
                level6()
        elif buttonLevel7.collidepoint((mx,my)):
            if click:
                level7()
        elif buttonLevel8.collidepoint((mx,my)):
            if click:
                level8()
        elif buttonLevel9.collidepoint((mx,my)):
            if click:
                level9()
        elif buttonLevel10.collidepoint((mx,my)):
            if click:
                level10()

        pygame.draw.rect(win, l1.colour, buttonLevel1)
        pygame.draw.rect(win, l2.colour, buttonLevel2)
        pygame.draw.rect(win, l3.colour, buttonLevel3)
        pygame.draw.rect(win, l4.colour, buttonLevel4)
        pygame.draw.rect(win, l5.colour, buttonLevel5)
        pygame.draw.rect(win, l6.colour, buttonLevel6)
        pygame.draw.rect(win, l7.colour, buttonLevel7)
        pygame.draw.rect(win, l8.colour, buttonLevel8)
        pygame.draw.rect(win, l9.colour, buttonLevel9)
        pygame.draw.rect(win, l10.colour, buttonLevel10)

        drawText("level 1", (255,255,255), font1, win, l1.x+20, l1.y+15)
        drawText("level 2", (255,255,255), font1, win, l2.x+20, l2.y+15)
        drawText("level 3", (255,255,255), font1, win, l3.x+20, l3.y+15)
        drawText("level 4", (255,255,255), font1, win, l4.x+20, l4.y+15)
        drawText("level 5", (255,255,255), font1, win, l5.x+20, l5.y+15)
        drawText("level 6", (255,255,255), font1, win, l6.x+20, l6.y+15)
        drawText("level 7", (255,255,255), font1, win, l7.x+20, l7.y+15)
        drawText("level 8", (255,255,255), font1, win, l8.x+20, l8.y+15)
        drawText("level 9", (255,255,255), font1, win, l9.x+20, l9.y+15)
        drawText("level 10", (255,255,255), font1, win, l10.x+20, l10.y+15)

        pygame.display.update()            

def howTo():

    buttonB= player((0,255,0), 400, 420, 50, 200)

    while True:
        win.fill((255,255,255))

        mx, my = pygame.mouse.get_pos()

        buttonBack = pygame.Rect(buttonB.x, buttonB.y, buttonB.width, buttonB.height)

        click = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True        
        
        if buttonBack.collidepoint((mx, my)):
            if click:
                menu()

        pygame.draw.rect(win, buttonB.colour, buttonBack)

        drawText("Bloker is a game where you control a box with your mouse and protect", (0,0,0), pygame.font.SysFont(None, 40), win, 10, 100)
        drawText("it from obsticles .There are ten levels, the difficulty increases as you ", (0,0,0), pygame.font.SysFont(None, 40), win, 10, 130)
        drawText("go further in the game.", (0,0,0), pygame.font.SysFont(None, 40), win, 10, 160)
        drawText("But I don't think you can finish it. The 5th level will demolish you.", (0,0,0), pygame.font.SysFont(None, 40), win, 10, 190)
        drawText("Anyways good luck, you will need it.", (0,0,0), pygame.font.SysFont(None, 40), win, 10, 250)

        drawText("back to menu", (255,255,255), font1, win, buttonB.x + 20, buttonB.y +15)

        pygame.display.update()

def finalScreen():
    buttonQ = player((0,255,0), 400, 300, 50, 200)
    buttonM = player((0,255,0), 400, 360, 50, 200)
    buttonL = player((0,255,0), 400, 420, 50, 200)

    while True:
        win.fill((255,255,255))

        click = False

        mx,my = pygame.mouse.get_pos()

        buttonQuit = pygame.Rect(buttonQ.x, buttonQ.y, buttonQ.width, buttonQ.height)
        buttonMenu = pygame.Rect(buttonM.x, buttonM.y, buttonM.width, buttonM.height)
        buttonLevels = pygame.Rect(buttonL.x, buttonL.y, buttonL.width, buttonL.height)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True
        
        if buttonQuit.collidepoint((mx, my)):
            if click:
                sys.exit()
        elif buttonMenu.collidepoint((mx, my)):
            if click:
                menu()
        elif buttonLevels.collidepoint((mx, my)):
            if click:
                AllLevels()

        pygame.draw.rect(win, buttonQ.colour, buttonQuit)
        pygame.draw.rect(win, buttonM.colour, buttonMenu)
        pygame.draw.rect(win, buttonL.colour, buttonLevels)

        drawText("Conratulations you have completed this game", (0,0,0), pygame.font.SysFont(None, 60), win, 50, 50)
        drawText("quit game", (255,255,255), font1, win, 420, 315)
        drawText("menu", (255,255,255), font1, win, 420, 375)
        drawText("all levels", (255,255,255), font1, win, 420, 435)

        pygame.display.update()

menu()