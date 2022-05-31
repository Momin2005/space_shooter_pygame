import pygame


# bullet class
class Bullet(pygame.sprite.Sprite):

    def __init__(self, img, player, game, x, y, velocity, target, damage, rotate=-90):
        super().__init__()
        pygame.init()

        self.game = game

        self.velocity = velocity
        self.player = player
        self.damage = damage
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.image = pygame.transform.rotate(self.image, rotate)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.target = target

    def remove(self):
        self.player.all_bullets.remove(self)

    def get_damage(self):
        return self.damage

    def update(self):
        self.rect.x += self.velocity

        for e in self.game.check_collision(self, self.target):
            self.remove()

            e.damage(self.damage)

