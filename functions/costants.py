import pygame
from functions.snake import *


FRUITS = []
def list_fruit(fname, img):
    global FRUITS

    fruit = pygame.image.load(img).convert_alpha()
    fruit.set_colorkey((255, 255, 255))
    FRUITS.append((fname, fruit))

class Costants:
        
        clock = pygame.time.Clock()
        # Define Constants
        BOARD_SIZE = 20  # Size of the board, in block
        BLOCK_SIZE = 20  # Size of 1 block, in pixel
        GAME_SPEED = 8  # Game speed (Normal = 10), The bigger, the faster
        screen = pygame.display.set_mode((BOARD_SIZE * BLOCK_SIZE * 2, BOARD_SIZE * BLOCK_SIZE * 2))
        window = pygame.Surface((BOARD_SIZE * BLOCK_SIZE, BOARD_SIZE * BLOCK_SIZE))
        pygame.display.set_caption("Snake 1.9.0")
        score = 0
        music = 0
        w, h = window.get_size()
        w2 = w // 2
        h2 = h // 2

        # this are blitted with blit_all function
        # make a tuple tup_fly(fly, (0, 0)) and go
        head = pygame.image.load("imgs/head20.png").convert_alpha()
        body = pygame.image.load("imgs/skin20.png").convert_alpha()
        blacktail = pygame.image.load("imgs/tail.png").convert_alpha()
        clean = pygame.Surface((300, 20))
        clean.fill((0,0,0))
        # Create list of different fruits to choose with choice
        for f in "apple2", "pear", "cherry", "apple", "apple3", "peachoch", "orange", "banana":
            list_fruit(f, f"imgs/{f}.png")
        FRUITS = FRUITS
        fly = pygame.image.load("imgs/fly.png").convert_alpha()

        # Obscure score and maxscore text
        bscore1 = pygame.Surface((80, 15))
        bscore1.fill((0, 0, 0))
        bscore2 = pygame.Surface((80, 15))
        bscore2.fill((0, 0, 0))


def save_image(screen: pygame.Surface, name: str="screenshot.png"):
    "Saves an image of the screen;\
    arg 1 screen surface, arg 2 name to save"
    pygame.image.save(screen, name)

def replace_Costants(filename):
    w = "screen,window,score,music,head,body,blacktail,fruit,bscore2"
    w = w.split(",")
    print(w)

    with open(filename, "r") as file:
        testo = file.read()
#    print(testo)
    for eachword in w:
        testo = testo.replace(eachword, "Costants." + eachword)
    print(testo)
    # with open(filename, "w") as file:
    #     file.write(testo)

if __name__ == "__main__":
    replace_Costants("../snake189.py")
