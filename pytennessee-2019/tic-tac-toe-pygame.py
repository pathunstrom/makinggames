from itertools import product
from random import choice

import pygame

ALPHA_KEY = 255, 64, 222
AI_MOVED = pygame.USEREVENT
GAME_WON = pygame.USEREVENT + 1


def load_image(file) -> pygame.Surface:
    surf = pygame.image.load(file).convert()
    surf.set_colorkey(ALPHA_KEY)
    return surf


class Board(pygame.sprite.LayeredDirty):

    def __init__(self):
        super().__init__()
        self.winner = None

    def check_win(self):
        for x in range(3):
            self.check_row(x)
            self.check_column(x)
            self.check_diagonal(x)
        if self.winner:
            winners = {NAUGHT_IMG: "O", CROSS_IMG: "X"}
            pygame.event.post(pygame.event.Event(GAME_WON, {"winner": winners[self.winner]}))

    def check_row(self, row):
        squares = list(s for s in self if s.row == row)
        check = squares[0].image
        if check is EMPTY_IMG:
            return
        result = all(s.image == squares[0].image for s in squares)
        if result:
            self.winner = squares[0].image

    def check_column(self, column):
        squares = list(s for s in self if s.column == column)
        check = squares[0].image
        if check is EMPTY_IMG:
            return
        result = all(s.image == squares[0].image for s in squares)
        if result:
            self.winner = squares[0].image

    def check_diagonal(self, diagonal):
        if diagonal >= 2:
            return
        squares = list(s for s in self if diagonal in s.diagonals)
        if not squares:
            return
        check = squares[0].image
        if check is EMPTY_IMG:
            return
        result = all(s.image == squares[0].image for s in squares)
        if result:
            self.winner = squares[0].image


class Square(pygame.sprite.DirtySprite):

    def __init__(self, image, position, board, column, row, diagonals):
        super().__init__(board)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.column = column
        self.row = row
        self.diagonals = diagonals

    def selected(self, symbol):
        self.image = symbol
        self.dirty = True


class Mouse(pygame.sprite.DirtySprite):

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 1, 1)

    def move(self, position):
        self.rect.topleft = position


class AI:

    def __init__(self, wait_time, symbol):
        self.wait_time = wait_time
        self.counter = 0
        self.symbol = symbol

    def update(self, time_delta, board):
        self.counter += time_delta
        if self.counter >= self.wait_time:
            self.make_move(board)
            self.counter = 0

    def make_move(self, board):
        empty_spaces = list(square for square in board if square.image == EMPTY_IMG)
        if empty_spaces:
            choice(empty_spaces).selected(self.symbol)
        pygame.event.post(pygame.event.Event(AI_MOVED, {}))


pygame.init()

WINDOW = pygame.display.set_mode((384, 384))
WINDOW.set_colorkey(ALPHA_KEY)

NAUGHT_IMG = load_image("./naught.png")
CROSS_IMG = load_image("./cross.png")
EMPTY_IMG = load_image("./empty.png")
BOARD_IMG = load_image("./board.png")

running = True
WINDOW.blit(BOARD_IMG, (0, 0))
pygame.display.update()

board = Board()

for x, y in product(range(3), range(3)):
    diagonals = []
    if x == 0:
        if y == 0:
            diagonals= [0]
        elif y == 2:
            diagonals = [1]
    elif x == 2:
        if y == 0:
            diagonals = [1]
        elif y == 2:
            diagonals = [0]
    elif x == 1 and y == 1:
        diagonals = [0, 1]

    Square(EMPTY_IMG, (x * 128, y * 128), board, x, y, diagonals)

mouse = Mouse()
clock = pygame.time.Clock()
player_input = True
ai = AI(400, NAUGHT_IMG)
winner = None

while running:
    tick = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if player_input:
                mouse.move(event.pos)
                square = pygame.sprite.spritecollide(mouse, board, False)[0]
                square.selected(CROSS_IMG)
                player_input = False
        elif event.type == AI_MOVED:
            player_input = True
        elif event.type == GAME_WON:
            running = False
            winner = event.winner

    if not player_input:
        ai.update(tick, board)

    board.check_win()
    board.draw(WINDOW, BOARD_IMG)
    pygame.display.update()

font = pygame.font.Font(None, 100)
message = font.render(f"{winner}s wins!", True, (255, 255, 255))
message_rect = message.get_rect(center=WINDOW.get_rect().center)

WINDOW.blit(message, message_rect)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()