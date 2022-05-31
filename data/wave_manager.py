import random
import pygame
import data.entities.enemies.enemy as enemy


class waveManager():
    def __init__(self, game_manager, surface):

        self.all_enemies = pygame.sprite.Group()

        self.game_manager = game_manager
        self.screen = surface

        self.num_waves = 1

        self.spawn_rate = 200
        self.counter = self.spawn_rate

    def update(self):
        self.counter -= 1
        if self.counter <= 0:
            self.enemies()
            self.counter = random.randint(self.spawn_rate, 400)
        self.spawn_system()

    def spawn_system(self):
        for e in self.all_enemies:
            e.update()
            e.update_health_bar(self.screen)

        self.all_enemies.draw(self.screen)

    def enemies(self):
        whiton = enemy.Enemy(self.game_manager,
                             self.game_manager.player,
                             name='whiton',
                             velocity=.05,
                             image='data/res/enemies/tile000.png',
                             health=35,
                             attack=2,
                             can_shoot=True,
                             timeBTWBullet=100,
                             bullet_image='data/res/bullets/tile055.png',
                             bullet_rotation=180,
                             p_color=(167, 167, 167)
                             )
        speedon = enemy.Enemy(self.game_manager,
                              self.game_manager.player,
                              name='speedon',
                              velocity=4,
                              image='data/res/enemies/tile001.png',
                              health=15,
                              attack=2,
                              p_color=(167, 167, 167)
                              )
        electro = enemy.Enemy(self.game_manager,
                              self.game_manager.player,
                              name='electro',
                              velocity=3,
                              image='data/res/enemies/tile002.png',
                              health=15,
                              attack=2,
                              p_color=(255, 255, 0)
                              )
        grento = enemy.Enemy(self.game_manager,
                             self.game_manager.player,
                             name='grento',
                             velocity=3,
                             image='data/res/enemies/tile005.png',
                             health=12,
                             attack=4,
                             p_color=(0, 100, 0)
                             )
        purps = enemy.Enemy(self.game_manager,
                            self.game_manager.player,
                            name='perps',
                            velocity=1.5,
                            image='data/res/enemies/tile003.png',
                            health=15,
                            attack=3,
                            p_color=(128, 0, 128)
                            )
        p = enemy.Enemy(self.game_manager,
                        self.game_manager.player,
                        name='electro',
                        velocity=3,
                        image='data/res/enemies/tile030.png',
                        health=15,
                        attack=2,
                        p_color=(255, 255, 0)
                        )
        electro = enemy.Enemy(self.game_manager,
                              self.game_manager.player,
                              name='electro',
                              velocity=3,
                              image='data/res/enemies/tile002.png',
                              health=15,
                              attack=2,
                              p_color=(255, 255, 0)
                              )

        enemyTypes = [whiton,
                      speedon,
                      electro,
                      grento,
                      purps,
                      p]

        random_enemies = random.sample(enemyTypes, random.randint(3, len(enemyTypes)))

        for e in random_enemies:
            self.all_enemies.add(e)
