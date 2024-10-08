import pygame

class PhysicsEntity:
  def __init__(self, game, entity_type, position, size):
    self.game = game
    self.entity_type = entity_type
    self.position = list(position) # convert any iterable to a list
    self.size = size
    self.velocity = [0, 0]

  def update(self, movement=(0, 0)):
    frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

    self.pos[0] += frame_movement[0]
    self.pos[1] += frame_movement[1]

  def render(self, surf):
    surf.blit(self.game.assets['player'], self.position)