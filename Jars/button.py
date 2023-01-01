import pygame
screen = pygame.display.set_mode((1386, 800))
running = True
pygame.init()
#Images
AB = pygame.image.load("Sprites/AB.png").convert_alpha()
AC = pygame.image.load("Sprites/AC.png").convert_alpha()
BA = pygame.image.load("Sprites/BA.png").convert_alpha()
BC = pygame.image.load("Sprites/BC.png").convert_alpha()
CA = pygame.image.load("Sprites/CA.png").convert_alpha()
CB = pygame.image.load("Sprites/CB.png").convert_alpha()
reset = pygame.image.load("Sprites/reset.png").convert_alpha()

#music
pop = pygame.mixer.Sound("Sounds/pop.ogg")

class Button():
  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.clicked = False

  def draw(self):
    action = False
    pos = pygame.mouse.get_pos()
    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
        pop.play()
        action = True

    if pygame.mouse.get_pressed()[0] == 0:
      self.clicked = False


    screen.blit(self.image, (self.rect.x, self.rect.y))
    pygame.display.update()
    return action

button_AB = Button(540, 600, AB, 1)
button_AC = Button(540, 700, AC, 1)
button_BA = Button(640, 600, BA, 1)
button_BC = Button(640, 700, BC, 1)
button_CB = Button(740, 600, CB, 1)
button_CA = Button(740, 700, CA, 1)
reset_button = Button(840, 650, reset, 1)



# while running:
#   if button_AB.draw():
#     print("AB")
#   if button_AC.draw():
#     print("AC")
#   if button_BA.draw():
#     print("BA")
#   if button_BC.draw():
#     print("BC")
#   if button_CB.draw():
#     print("CB")
#   if button_CA.draw():
#     print("CA")
#   pygame.display.update()
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       running = False


