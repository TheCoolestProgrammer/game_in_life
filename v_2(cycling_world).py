import pygame
import copy


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 20

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_mouse(self):
        pass

    def get_cords(self):
        pass

    def render(self, screen):
        pass


class Live(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def on_mouse(self):
        x, y = pygame.mouse.get_pos()
        if self.left <= x <= self.width * self.cell_size and self.top <= y <= self.height * board.cell_size:
            self.board[(y - self.top) // self.cell_size][(x - self.left) // self.cell_size] = ((self.board[
                (y - self.top) // self.cell_size][(x - self.left) // self.cell_size]) + 1) % 2

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] % 2 == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (
                        self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size),
                                     1)
                else:
                    pygame.draw.rect(screen, (0, 255, 0), (
                        self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size))

    def next_move(self):
        tmp_board = copy.deepcopy(self.board)
        for y in range(self.height):
            for x in range(self.width):
                s = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if x + dx < 0 or x + dx >= self.width or y + dy < 0 or y + dy >= self.height:
                            a = dy
                            b = dx
                            if y + dy < 0:
                                a = self.height - 1
                            if x + dx < 0:
                                b = self.height - 1
                            if y + dy >= self.height:
                                a = 0
                            if x + dx >= self.width:
                                b = 0
                            if a == dy:
                                a = y + dy
                            if b == dx:
                                b = x + dx
                            s += self.board[a][b]
                        else:
                            s += self.board[y + dy][x + dx]
                s -= self.board[y][x]
                if s == 3:
                    tmp_board[y][x] = 1
                elif s < 2 or s > 3:
                    tmp_board[y][x] = 0
        self.board = copy.deepcopy(tmp_board)


board = Live(40, 40)
running = True
pygame.init()
pygame.display.set_caption('game life')
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
fps = 60
clock = pygame.time.Clock()
time_on = False
ticks = 0
speed = 10
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.on_mouse()
            if event.button == 3:
                time_on = not time_on
            if event.button == 4:
                speed -= 1

            if event.button == 4:
                speed += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                time_on = not time_on
    screen.fill((0, 0, 0))
    board.render(screen)
    if time_on:
        if ticks >= speed:
            board.next_move()

            ticks = 0
    pygame.display.flip()
    clock.tick(fps)
    ticks += 1
