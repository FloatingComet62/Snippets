import pygame
import time

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW_COLOR = (0, 0, 0)
FPS = 60

def updateWindow(*items):
    WINDOW.fill(WINDOW_COLOR)
    for item in items:
        if item[0] == "rect":
            pygame.draw.rect(WINDOW, item[1], item[2])
        elif item[0] == "circle":
            pygame.draw.circle(WINDOW, item[1], item[2], item[3])
    pygame.display.update()

if __name__  == "__main__":

    run = True
    clock = pygame.time.Clock()
    pygame.display.set_caption("Title")
    frames = 0
    
    # sprite making
    # player = ["rect", (255, 0, 0), [0, HEIGHT/2-50, 25, 100]]
    # ball = ["circle", (255, 0, 0), [400, 300], 10]


    while run:
        frames+=1
        clock.tick(FPS)
        updateWindow(player, ai, ball)

            # collision checking
            # collide = pygame.rect.Rect(player[2][0], player[2][1], player[2][2], player[2][3]).collidepoint(ball[2][0]-10, ball[2][1])

        # edge bounce
        # if ball[2][1] > HEIGHT-ball[3]:
            # yVelocity = -yVelocity
        # elif ball[2][1] < 0:
            # yVelocity = -yVelocity
        # if ball[2][0] > WIDTH-ball[3]-ai[2][2]:
            # xVelocity = -xVelocity
        # elif ball[2][0] < 0+player[2][2]:
            # xVelocity = -xVelocity

        # key presses
        # keys_pressed = pygame.key.get_pressed()
        # if keys_pressed[pygame.K_UP]:
            # player[2][1] -= 10
        # if keys_pressed[pygame.K_DOWN]:
            # player[2][1] += 10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()