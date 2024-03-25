import pygame

class Watermelon:
  def __init__(self, x, y):
      self.x = x
      self.y = y
      self.image_list = ["watermelon.png"]
      self.image = pygame.image.load(self.image_list[0])
      self.rescale_image(self.image)
      self.image_size = self.image.get_size()
      self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
      self.delta = 2
      self.image_idx = 0
      self.mask = pygame.mask.from_surface(self.image)


  def rescale_image(self, image):
      self.image_size = self.image.get_size()
      scale_size = (self.image_size[0] * .2, self.image_size[1] * .2)
      self.image = pygame.transform.scale(self.image, scale_size)


  def move(self, new_x, new_y):
      self.x = new_x
      self.y = new_y
      self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
      if self.rect.left < 0:
          self.rect.left = 0
      if self.rect.right > 800:
          self.rect.right = 800
      if self.rect.top <= 0:
          self.rect.top = 0
      if self.rect.bottom >= 600:
          self.rect.bottom = 600