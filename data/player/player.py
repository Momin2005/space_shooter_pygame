import pygame
import data.entities.bullet as bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, surface, game):
        super().__init__()
        pygame.init()

        self.maxHealth = 50
        self.health = self.maxHealth

        self.screen = surface
        self.image = pygame.image.load('data\\player\\player.png')
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.image = pygame.transform.rotate(self.image, -90)
        self.game = game

        self.timeBTWBullet = 5
        self.timeCounter = self.timeBTWBullet

        self.rect = self.image.get_rect()
        self.rect.x = 25
        self.rect.y = self.screen.get_height() / 2 - self.image.get_height() / 2
        self.is_shooting = True
        self.all_bullets = pygame.sprite.Group()

    def update(self):
        mousePos = pygame.mouse.get_pos()
        self.rect.y = mousePos[1] - self.image.get_height() / 2
        self.mouse(mousePos)
        self.shoot_bullet()

    def shoot_bullet(self):
        self.all_bullets.draw(self.screen)
        self.timeCounter -= 1
        if self.timeCounter < 0:
            if pygame.mouse.get_pressed()[0]:
                self.all_bullets.add(bullet.Bullet('data/res/bullets/tile003.png', self, self.game, self.rect.x,
                                                   (pygame.mouse.get_pos()[1] - int(self.image.get_width() / 2)), 5,
                                                   self.game.waveManager.all_enemies, 3))
            self.is_shooting = False
            self.timeCounter = self.timeBTWBullet

        for b in self.all_bullets:
            b.update()

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.isPlayerDead = True

    def update_bars(self, surface):

        # healthbar
        health_bar_color = (255, 0, 0)
        health_back_bar_color = (150, 0, 0)

        bar_position = [self.screen.get_width()/2 - (self.maxHealth*3)/2, 0, self.health * 3, 15]
        back_bar_position = [self.screen.get_width()/2 - (self.maxHealth*3)/2, 0, self.maxHealth * 3, 15]

        pygame.draw.rect(surface, health_back_bar_color, back_bar_position)
        pygame.draw.rect(surface, health_bar_color, bar_position)

    def mouse(self, mousePos):
        pygame.mouse.set_visible(False)
        img = pygame.image.load('data\\res\\UI\\cursor.png')
        img = pygame.transform.scale(img, (32, 32))
        x = mousePos[0] - img.get_width() / 2
        y = mousePos[1] - img.get_height() / 2

        self.screen.blit(img, (x, y))
