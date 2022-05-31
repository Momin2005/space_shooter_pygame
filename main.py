import pygame

from data import game_manager


class main:
    def __init__(self):
        pygame.init()

        # ---- window setup ---- #
        self.resolution = (960, 540)
        self.bg = pygame.image.load("data/res/bg/bg.png")
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()

        # ---- run ---- #
        self.running = True

        # ----objects---- #
        self.game_manager = game_manager.gameManager(self.screen)

        self.game_loop()

    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def game_loop(self):
        while self.running:
            self.screen.blit(self.bg, (0, 0))

            mousePos = pygame.mouse.get_pos()

            self.event_manager()

            # ----objects----#
            self.game_manager.update()
            if self.game_manager.isPlayerDead == True:
                self.running = False

            # ---- end ---- #
            self.clock.tick(10)
            pygame.display.update()


if __name__ == '__main__':
    main()
