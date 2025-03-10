import pygame
import sys


# Инициализация Pygame
pygame.init()

# Размеры окна
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Создание окна
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Крестики-Нолики")

# Размеры клеток
CELL_SIZE = WINDOW_WIDTH // 3

# Состояние игрового поля
FIELD = [[" " for _ in range(3)] for _ in range(3)]

# Текущий игрок
CURRENT_PLAYER = "X"


# Функция отрисовки игрового поля
def draw_field():
    WINDOW.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(WINDOW, BLACK, (0, i * CELL_SIZE), (WINDOW_WIDTH, i * CELL_SIZE), 5)
        pygame.draw.line(WINDOW, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_HEIGHT), 5)
    for i in range(3):
        for j in range(3):
            if FIELD[i][j] == "X":
                pygame.draw.line(WINDOW, RED, (j * CELL_SIZE + 20, i * CELL_SIZE + 20), ((j + 1) * CELL_SIZE - 20, (i + 1) * CELL_SIZE - 20), 5)
                pygame.draw.line(WINDOW, RED, (j * CELL_SIZE + 20, (i + 1) * CELL_SIZE - 20), ((j + 1) * CELL_SIZE - 20, i * CELL_SIZE + 20), 5)
            elif FIELD[i][j] == "O":
                pygame.draw.circle(WINDOW, GREEN, (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 20, 5)


# Функция проверки победы
def check_win():
    for i in range(3):
        if FIELD[i][0] == FIELD[i][1] == FIELD[i][2] != " ":
            return True
        if FIELD[0][i] == FIELD[1][i] == FIELD[2][i] != " ":
            return True
    if FIELD[0][0] == FIELD[1][1] == FIELD[2][2] != " ":
        return True
    if FIELD[0][2] == FIELD[1][1] == FIELD[2][0] != " ":
        return True
    return False


# Функция проверки ничьей
def check_draw():
    for i in range(3):
        for j in range(3):
            if FIELD[i][j] == " ":
                return False
    return True


# Стартовое окно
def start_window():
    WINDOW.fill(WHITE)
    font = pygame.font.Font(None, 36)
    text = font.render("Крестики-Нолики", True, BLACK)
    WINDOW.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2 - 100))
    pygame.draw.rect(WINDOW, BLACK, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 50, 200, 50), 2)
    text = font.render("Крестик", True, BLACK)
    WINDOW.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - 25))
    pygame.draw.rect(WINDOW, BLACK, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 50, 200, 50), 2)
    text = font.render("Нолик", True, BLACK)
    WINDOW.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 + 75))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if WINDOW_WIDTH // 2 - 100 < x < WINDOW_WIDTH // 2 + 100 and WINDOW_HEIGHT // 2 - 50 < y < WINDOW_HEIGHT // 2:
                    return "X"
                elif WINDOW_WIDTH // 2 - 100 < x < WINDOW_WIDTH // 2 + 100 and WINDOW_HEIGHT // 2 + 50 < y < WINDOW_HEIGHT // 2 + 100:
                    return "O"


# Финальное окно
def end_window(score):
    WINDOW.fill(WHITE)
    font = pygame.font.Font(None, 36)
    text = font.render("Игра окончена!", True, BLACK)
    WINDOW.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2 - 100))
    text = font.render(f"Счёт (X - O): {score['X']} - {score['O']}", True, BLACK)
    WINDOW.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False


# Основной цикл игры
score = {"X": 0, "O": 0}
CURRENT_PLAYER = start_window()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            i, j = y // CELL_SIZE, x // CELL_SIZE
            if FIELD[i][j] == " ":
                FIELD[i][j] = CURRENT_PLAYER
                draw_field()
                pygame.display.update()
                if check_win():
                    print(f"Игрок {CURRENT_PLAYER} выиграл!")
                    score[CURRENT_PLAYER] += 1
                    pygame.time.delay(2000)  # пауза на 2 секунды
                    end_window(score)
                    FIELD = [[" " for _ in range(3)] for _ in range(3)]
                    CURRENT_PLAYER = start_window()
                elif check_draw():
                    print("Ничья!")
                    pygame.time.delay(2000)  # пауза на 2 секунды
                    end_window(score)
                    FIELD = [[" " for _ in range(3)] for _ in range(3)]
                    CURRENT_PLAYER = start_window()
                else:
                    CURRENT_PLAYER = "O" if CURRENT_PLAYER == "X" else "X"
    draw_field()
    pygame.display.update()