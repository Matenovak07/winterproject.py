import pygame
import random
pygame.init()
 
WHITE = [255, 255, 255]
BLACK  = [0,0,0]
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_RADIUS = 15
BRICK_WIDTH, BRICK_HEIGHT = 80, 30
PADDLE_SPEED = 10
BALL_SPEED_X, BALL_SPEED_Y = 5, 5
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Winter Project")
hit_sound = pygame.mixer.Sound("hit-sound.wav")
hit_sound.set_volume(2)

pygame.mixer.music.load("background_music.mp3")  
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

snowFall = []
for i in range(150):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    snowFall.append([x, y])

paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = pygame.Vector2(BALL_SPEED_X, BALL_SPEED_Y)

bricks = []
for i in range(5):
    for j in range(8):
        brick = pygame.Rect(j * (BRICK_WIDTH + 5) + 50, i * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True
    screen.fill(BLACK)
    for i in range(len(snowFall)):
        pygame.draw.circle(screen, WHITE, snowFall[i], 2)
 
        snowFall[i][1] += 1
        if snowFall[i][1] > 600:
            y = random.randrange(-50, -10)
            snowFall[i][1] = y
        
            x = random.randrange(0, 800)
            snowFall[i][0] = x
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += PADDLE_SPEED

    ball.x += ball_speed.x
    ball.y += ball_speed.y

    if ball.left < 0 or ball.right > WIDTH:
        ball_speed.x = -ball_speed.x
    if ball.top < 0:
        ball_speed.y = -ball_speed.y

    if ball.colliderect(paddle) and ball_speed.y > 0:
        ball_speed.y = -ball_speed.y
        hit_sound.play()

    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed.y = -ball_speed.y
            hit_sound.play()

    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.circle(screen, WHITE, ball.center, BALL_RADIUS)

    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)

    pygame.display.flip()
    clock.tick(20)
pygame.quit()
