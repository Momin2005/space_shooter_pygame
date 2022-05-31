import pygame
from data.wave_manager import waveManager
import data.player.player as player


class gameManager:
    def __init__(self, surface):
        self.screen = surface
        self.player = player.Player(self.screen, self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.particles = []
        self.waveManager = waveManager(self, self.screen)
        self.isPlayerDead = False
        self.score = 0

    def update(self):
        self.waveManager.update()

        for p in self.all_players:
            p.update()
            p.update_bars(self.screen)

        self.all_players.draw(self.screen)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False)

    def score_management(self, points):
        self.score += points
        print(self.score)
        
