import pygame
from random import randint
class snake:
    def __init__(self, x, y, long, facing):
        self.x = x
        self.y = y
        self.long = long
        self.facing = facing
        self.pos = [(self.x, self.y, 60, 60)]
        self.isDead = False

    def draw(self, win):
        self.getfacing()
        self.pos.append((self.x, self.y, 60, 60))
        for i, index in enumerate(range(self.long)):
            pygame.draw.rect(win, (0, 255, 0), (self.pos[index+1]))
            pygame.draw.rect(win, (0, 100, 0), (self.pos[index+1]), 1)
        pygame.draw.rect(win, (0, 100, 0), self.pos[len(self.pos)-1])
        pygame.draw.circle(win, (0, 0, 255), (self.pos[len(self.pos) - 1][0] + 20, self.pos[len(self.pos) - 1][1] + 30),6)
        pygame.draw.circle(win, (0, 0, 255), (self.pos[len(self.pos) - 1][0] + 40, self.pos[len(self.pos) - 1][1] + 30),6)
        pygame.draw.rect(win, (255, 0, 0), (self.pos[len(self.pos)-1][0]+40, self.pos[len(self.pos)-1][1]+50, 20, 5))
        pygame.draw.rect(win, (0, 0, 0), self.pos[0])
        self.pos.remove(self.pos[0])

    def getfacing(self):
        if self.facing == "w":
            self.y = self.y - 60
        if self.facing == "a":
            self.x = self.x - 60
        if self.facing == "s":
            self.y = self.y + 60
        if self.facing == "d":
            self.x = self.x + 60

    def die(self, hitapple, morte):
        if not hitapple:
            for i, index in enumerate(range(self.long)):
                if self.pos.count(self.pos[index]) > 1:
                    self.isDead = True
                    return True
        if self.x == 1920 or self.y == 1080 or self.x<0 or self.y<0:
            self.isDead = True
            return True
        if morte:
            self.isDead = True
            return True
        if self.isDead:
            return True
        return False

class apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 60, 60))

    def hit(self, snakex, snakey):
        if snakex == self.x and snakey == self.y:
            return True
        else:
            return False

    def random(self, snake):
        self.x = 60 * randint(0, 31)
        self.y = 60 * randint(0, 16)
        apple.inSnake(self, snake)

    def inSnake(self, snake):
        for i, index in enumerate(range(snake.long)):
            if self.x == snake.pos[index][0] and self.y == snake.pos[index][1]:
                apple.random(self, snake)
