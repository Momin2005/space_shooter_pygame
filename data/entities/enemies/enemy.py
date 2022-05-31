import math, pygame, random

import data.entities.bullet as bullet
import data.entities.enemies.spark as spark


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, player, name, velocity, image, health, attack, p_color, points=1, can_shoot=False, timeBTWBullet=25, bullet_image=1, bullet_rotation=90):
        super().__init__()

        self.maxHealth = health
        self.health = self.maxHealth
        self.attack = attack
        self.velocity = velocity
        self.name = name
        self.can_shoot = can_shoot
        self.bullet_image = bullet_image
        self.bullet_rotation = bullet_rotation
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.game = game
        self.player = player
        self.p_color = p_color
        self.points = points

        self.all_bullets = pygame.sprite.Group()
        self.timeBTWBullet = timeBTWBullet
        self.timeCounter = self.timeBTWBullet

        self.sparks = []

        self.rect.x = 960
        self.rect.y = random.randint(30, 510)

    def damage(self, amount):
        # [loc, velocity, timer]
        for i in range(4):
            self.sparks.append(
                spark.Spark(loc=[self.rect.centerx, self.rect.centery], angle=math.radians(random.randint(0, 360)),
                            speed=random.randint(3, 6), color=self.p_color, scale=1))

        self.health -= amount

        if self.health <= 0:
            self.remove()
            self.game.score_management(self.points)

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        back_bar_color = (60, 60, 60)

        bar_position = [self.rect.x, self.rect.y - 5, self.health * 1.5, 3]
        back_bar_position = [self.rect.x, self.rect.y - 5, self.maxHealth * 1.5, 3]

        hover_rect = pygame.Rect(pygame.mouse.get_pos()[0] - 960, pygame.mouse.get_pos()[1], 960 * 2, 32)
        if hover_rect.colliderect(self.rect):
            pygame.draw.rect(surface, back_bar_color, back_bar_position)
            pygame.draw.rect(surface, bar_color, bar_position)

    def shoot_bullet(self):
        self.all_bullets.draw(self.game.screen)
        self.timeCounter -= 1
        if self.timeCounter < 0:
            self.all_bullets.add(bullet.Bullet(self.bullet_image, self, self.game, self.rect.x - 3,
                                               self.rect.y, -5, self.game.all_players, self.attack,
                                               self.bullet_rotation))
            self.timeCounter = self.timeBTWBullet

        for b in self.all_bullets:
            b.update()

    def remove(self):
        self.game.waveManager.all_enemies.remove(self)

    def update(self):
        self.rect.x -= self.velocity

        for i, spark in sorted(enumerate(self.sparks), reverse=True):
            spark.move(1)
            spark.draw(self.game.screen)
            if not spark.alive:
                self.sparks.pop(i)

        for e in self.game.check_collision(self, self.game.all_players):
            self.remove()

            e.damage(self.attack * 2)

        if self.rect.x <= 0:
            self.remove()

        if self.can_shoot:
            self.shoot_bullet()
