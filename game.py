import sys
import pygame
from scripts.entities import PhysicsEntity

class Game:
  def __init__(self):
    pygame.init()

    pygame.display.set_caption("Ninja Game")

    self.screen = pygame.display.set_mode((640, 480)) # Creates window and sets size

    self.clock = pygame.time.Clock() # instatiate clock obj

    self.img_pos = [160, 260]
    self.movement = [False, False]


    self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

  def run(self):
    while True:
      self.screen.fill((14, 219, 248))

      self.player.update((self.movement[1] - self.movement[0], 0))
      self.player.render(self.screen)

      for event in pygame.event.get():

        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        
        if event.type == pygame.KEYDOWN:

          if event.key == pygame.K_a:
            self.movement[0] = True
          if event.key == pygame.K_d:
            self.movement[1] = True

        if event.type == pygame.KEYUP:

          if event.key == pygame.K_a:
            self.movement[0] = False
          if event.key == pygame.K_d:
            self.movement[1] = False


      pygame.display.update()
      self.clock.tick(60) # fps

Game().run()