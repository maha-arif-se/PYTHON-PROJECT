import pygame
import random

# Initialize pygame
pygame.init()
pygame.mixer.init()
catch_sound = pygame.mixer.Sound("catch.wav.wav")
font = pygame.font.SysFont("Arial", 25)

# Window size
width, height = 1000, 700
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Catch The Ball Game")

# Load images
circle_img = pygame.image.load("ball.jpg")
circle_img = pygame.transform.scale(circle_img, (30, 30))


rect_img = pygame.image.load("rectangle.png")
rect_img = pygame.transform.scale(rect_img, (70, 70))

background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (width, height))
# Load sound
catch_sound = pygame.mixer.Sound("catch.wav.wav")

# Circle (Ball) variables
circle_x = random.randint(0, width - 30)
circle_y = 0
circle_r = 15

# Rectangle (Paddle) variables
rect_w = 70
rect_h = 70
rect_x = width // 2
rect_y = height - rect_h

# Score variables
score = 0
missed = 0

# Level selection screen
level_selected = False
ball_speed = 5

while not level_selected:
    screen.fill((0, 0, 0))

    title = font.render("Select Level", True, (255,255,255))
    basic = font.render("Press 1 - Basic", True, (255,255,255))
    inter = font.render("Press 2 - Intermediate", True, (255,255,255))
    adv = font.render("Press 3 - Advanced", True, (255,255,255))

    screen.blit(title, (220, 120))
    screen.blit(basic, (220, 170))
    screen.blit(inter, (220, 210))
    screen.blit(adv, (220, 250))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                ball_speed = 5
                level_selected = True
            elif event.key == pygame.K_2:
                ball_speed = 8
                level_selected = True
            elif event.key == pygame.K_3:
                ball_speed = 12
                level_selected = True

# Game loop flag
running = True

# Game Loop
while running:
    pygame.time.delay(30)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        rect_x += 5
        if rect_x > width - rect_w:
            rect_x = width - rect_w

    if keys[pygame.K_LEFT]:
        rect_x -= 5
        if rect_x < 0:
            rect_x = 0

    # Move ball downward
    circle_y += ball_speed

    # Collision detection (Catch)
    if (rect_y <= circle_y + circle_r <= rect_y + rect_h) and \
            (rect_x <= circle_x <= rect_x + rect_w):
        score += 1 
        catch_sound.stop()
        catch_sound.play()
        circle_x = random.randint(0, width - 30)
        circle_y = 0

    # Miss condition
    elif circle_y + circle_r >= height:
        missed += 1
        circle_x = random.randint(0, width - 30)
        circle_y = 0

    # Stop game after 5 misses
    if missed >= 5:
        running = False
    # Draw everything
    screen.blit(background_img, (0, 0))
    screen.blit(circle_img, (circle_x, circle_y))
    screen.blit(rect_img, (rect_x, rect_y))
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    miss_text = font.render("Missed: " + str(missed), True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(miss_text, (10, 40))
    pygame.display.update()

# Game end
print("You missed =", missed)
print("Your score =", score)

# Game Over Screen
screen.fill((0, 0, 0))

game_over_text = font.render("GAME OVER!", True, (255, 0, 0))
final_score_text = font.render("Final Score: " + str(score), True, (255, 255, 255))

screen.blit(game_over_text, (width//2 - 100, height//2 - 40))
screen.blit(final_score_text, (width//2 - 100, height//2))

pygame.display.update()
pygame.time.delay(3000)

pygame.quit()



