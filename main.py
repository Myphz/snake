from classes import *
pygame.init()
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
run = True
snake = snake(900, 480, 1, "w")
randomx = 60 * randint(0, 31)
randomy = 60 * randint(0, 16)
apple = apple(randomx, randomy)
hit = False
muori = False
font = pygame.font.SysFont("handmade memories", 30)
font2 = pygame.font.SysFont("impact", 100)
text = font2.render("Hai perso", 0, (255,255,255))
music = pygame.mixer.music.load("music.mp3")
eat = pygame.mixer.Sound("eat.wav")
pygame.mixer.music.play(-1)


def draw():
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 1920, 1080))
    score = font.render("Score: " + str(snake.long-1), 0, (255,255,255))
    win.blit(score, (1800, 0))
    snake.draw(win)
    apple.draw(win)
    if snake.die(hit, muori):
        pygame.time.delay(500)
        pygame.draw.rect(win, (0,0,0), (0,0,1920,1080))
        win.blit(text, (700, 480))
    pygame.display.update()

while run:
    hit = False
    tick = 200-(snake.long-1)*10
    if tick < 50:
        tick = 50

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                run = False
            elif event.key == pygame.K_w:
                if snake.long > 1 and snake.facing == "s":
                    muori = True
                snake.facing = "w"
            elif event.key == pygame.K_a:
                if snake.long > 1 and snake.facing == "d":
                    muori = True
                snake.facing = "a"
            elif event.key == pygame.K_s:
                if snake.long > 1 and snake.facing == "w":
                    muori = True
                snake.facing = "s"
            elif event.key == pygame.K_d:
                if snake.long > 1 and snake.facing == "a":
                    muori = True
                snake.facing = "d"

    pygame.time.delay(tick)

    if apple.hit(snake.x, snake.y):
        hit = True
        eat.play()
        apple.random(snake)
        snake.long+=1
        snake.getfacing()
        snake.pos.append((snake.x, snake.y, 60, 60))

    draw()

pygame.quit()