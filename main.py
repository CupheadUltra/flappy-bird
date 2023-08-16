import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WIDTH, HEIGHT = 400, 600

# Колір
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Створення вікна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Параметри пташки
bird_x = 50
bird_y = HEIGHT // 2
bird_speed = 0
bird_accel = 0.5

# Параметри труб
tube_width = 50
tube_gap = 150
tube_speed = 3
tubes = []

# Оновлення труб
def update_tubes():
    if len(tubes) == 0 or tubes[-1][0] < WIDTH - 200:
        tube_height = random.randint(100, 400)
        tubes.append([WIDTH, tube_height])

# Головний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_speed = -10

    # Оновлення позиції пташки
    bird_speed += bird_accel
    bird_y += bird_speed

    # Оновлення позицій труб
    for i, tube in enumerate(tubes):
        tube[0] -= tube_speed
        if tube[0] + tube_width < 0:
            tubes.pop(i)

    # Перевірка на зіткнення пташки з трубою або межею вікна
    for tube in tubes:
        if (
            bird_x + 30 > tube[0]
            and bird_x < tube[0] + tube_width
            and (bird_y < tube[1] or bird_y + 30 > tube[1] + tube_gap)
        ):
            running = False

    if bird_y > HEIGHT or bird_y < 0:
        running = False

    # Оновлення списку труб
    update_tubes()

    # Відображення гри
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (bird_x, bird_y, 30, 30))
    for tube in tubes:
        pygame.draw.rect(screen, BLUE, (tube[0], 0, tube_width, tube[1]))
        pygame.draw.rect(
            screen, BLUE, (tube[0], tube[1] + tube_gap, tube_width, HEIGHT)
        )
    pygame.display.flip()

    # Таймер
    pygame.time.Clock().tick(30)

# Завершення гри
pygame.quit()