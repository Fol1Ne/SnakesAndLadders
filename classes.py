import pygame

class PlayerPiece(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image_path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
    def update(self, pos_x, pos_y):
        self.rect.center = [pos_x, pos_y]

class Ladder(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, rotation):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/ladder.png"), (width, height))
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

class Snake(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, rotation):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/snake.png"), (width, height))
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

class Dice(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, rotation):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/dice.png"), (width, height))
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
    def update(self, rotation):
        self.image = pygame.transform.rotate(self.image, rotation)


        





