#just exported!
import pygame
import time
import random
from fruits import Apple
from watermelon import Watermelon
from orange import Orange
from bomb import Bomb


pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Arial", 20)
pygame.display.set_caption("Point and click, it's that simple!")
size = (800, 600)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("bg.png")
gun = pygame.image.load("gun.png")


start_screen = True
game_screen = False
end_screen = False
stamp = True
reload = False
ult = False
action = True
actions = True
stamper = True
stampern = False
stamperoo = False
timed = False
start = False
start_2 = False
red_rgb = (255, 0, 0)
black_rgb = (0, 0, 0)
white_rgb = (255, 255, 255)
yellow_rgb = (255,255,0)


apple = Apple(100, 100)
watermelon = Watermelon(800, 800)
orange = Orange(900, 50)
bomb = Bomb(900, 50)
current_time = time.time()

counter = 1
score = 0
bullets = 7
ab_points = 5
a_clicks = 0
w_clicks = 0
o_clicks = 0
count = 999
w_count = 999
o_count = 999
timer = 2
w_timer = 2
o_timer = 2
seconds_left = 60


reload_sound = pygame.mixer.Sound("reload.wav")
ult_sound = pygame.mixer.Sound("clear_screen.wav")
f_reload_sound = pygame.mixer.Sound("final_reload.wav")
fire_sound = pygame.mixer.Sound("fire.wav")
f_fire_sound = pygame.mixer.Sound("final_round.wav")
no_ammo_sound = pygame.mixer.Sound("no_ammo.wav")
while start_screen:
  # event loop: listen for mouse clicks
  for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:  # when mouse clicked, hide start screen and display game screen
       start_screen = False
       game_screen = True
      if event.type == pygame.QUIT:  # hide start screen if player X's out
       start_screen = False
  title_font = pygame.font.SysFont("Comic_Sans", 53)
  message_font = pygame.font.SysFont("Times_New_Roman", 20)
  message_font_two = pygame.font.SysFont("lobster", 45)
  welcome_message = title_font.render("AMERICAN FRUIT NINJA", True, red_rgb)
  message_one = message_font.render("Shoot the fruits to win", True, white_rgb)
  message_two = message_font.render("You cannot shoot if you are out of bullets", True, white_rgb)
  message_three = message_font.render("Press R to reload and E to use your ultimate", True, white_rgb)
  message_four = message_font.render("Earn points by shooting the fruits!", True, white_rgb)
  message_five = message_font_two.render("Click anywhere to begin!", True, yellow_rgb)
  life_message = message_font.render("!!Hit a Fruit before Timer Runs Out!!", True, white_rgb)
  screen.blit(bg, (0, 0))  # show background
  screen.blit(welcome_message, (60, 150))  # show welcome msg
  screen.blit(message_one, (210, 275))  # show msg 1
  screen.blit(message_two, (210, 300))  # show msg 2
  screen.blit(message_three, (210, 325))  # show msg 2
  screen.blit(message_four, (210, 350))  # show msg 4
  screen.blit(life_message, (210, 375))  # show msg 4
  screen.blit(message_five, (210, 425))  # show msg 5


  pygame.display.update()  # last line in the main run loop


while game_screen:
  # event loop: listen for mouse clicks
  for event in pygame.event.get():
      if (event.type == pygame.MOUSEBUTTONUP) and actions == True:
          mouse_x = event.pos[0]
          mouse_y = event.pos[1]
          mouse_position = (mouse_x, mouse_y)
          bullets -= 1
          if bullets < 0 and action == False:
              no_ammo_sound.play()
          else:
              if bullets == 0:
                  f_fire_sound.play()
              else:
                  fire_sound.play()
          if bullets < 0:
              bullets = 0

          if apple.rect.collidepoint(mouse_position) and action == True:
            if bullets >= 0:
                a_clicks +=1
                timer = 2 - (a_clicks * .1)
                if timer < .3:
                    timer = .3
                apple.move(random.randint(0, 600 - apple.image_size[0]), random.randint(0, 480 - apple.image_size[1]))
                score += 2
                rng = random.randint(1, 3)
                if rng == 1:
                    ab_points+=1
                    if ab_points > 5:
                        ab_points = 5
            stamper = True

          if orange.rect.collidepoint(mouse_position) and action == True:
              if bullets >= 0:
                  o_clicks += 1
                  timer2 = 2 - (o_clicks * .1)
                  if timer2 < .3:
                      timer2 = .3
                  orange.move(random.randint(0, 600 - orange.image_size[0]), random.randint(0, 480 - orange.image_size[1]))
                  score += 2
                  rng = random.randint(1, 4)
                  if rng == 1:
                      ab_points += 1
                      if ab_points > 5:
                          ab_points = 5
              stampern = True

          if watermelon.rect.collidepoint(mouse_position) and action == True and timed == True:
              if bullets >= 0:
                  w_clicks += 1
                  w_timer = 2 - (w_clicks * .1)
                  if w_timer < .3:
                      w_timer = .3
                  watermelon.move(random.randint(0, 600 - watermelon.image_size[0]), random.randint(0, 480 - watermelon.image_size[1]))
                  score += 1
                  rng = random.randint(1, 5)
                  if rng == 1:
                      ab_points += 1
                      if ab_points > 5:
                          ab_points = 5
              if real_time >= 10:
                 stamperoo = True

          elif bomb.rect.collidepoint(mouse_position) and bullets > 0:
             game_screen = False
             end_screen = True


      if event.type == pygame.KEYDOWN and event.key == pygame.K_r and ult == False:
          stamp = False
          reload = True
          action = False

      if (event.type == pygame.KEYDOWN and event.key == pygame.K_e) and ab_points == 5 and reload == False:
          stamp = False
          ult = True
          actions = False
          action = False
          stamper = False
          ult_sound.play()
          ab_points = 0
          bullets = 6

      if event.type == pygame.QUIT:  # hide game screen if player X's out
          game_screen = False

  screen.blit(bg, (0, 0))  # show background
  screen.blit(gun, (360, 400))
  actual_time = time.time()
  real_time = round(actual_time - current_time) + 1
  screen.blit(apple.image, apple.rect)
  screen.blit(bomb.image, bomb.rect)
  screen.blit(orange.image, orange.rect)
  screen.blit(watermelon.image, watermelon.rect)
  current_score = my_font.render("Score: " + str(score), True, white_rgb)  # update score label
  bullet_message = my_font.render("Bullets: " + str(bullets) + "/6", True, red_rgb)
  ap_message = my_font.render("Ability points: " + str(ab_points) + "/5", True, red_rgb)
  display_timer = my_font.render("Time Left: " + str(seconds_left), True, (255, 255, 255))
  screen.blit(display_timer, (0, 0))
  screen.blit(bullet_message, (700, 580))
  screen.blit(ap_message, (660, 550))
  screen.blit(current_score, (350, 20))  # show score  # last line in the main run loop
  if real_time >= 4 and start == False: # watermelon starts to move and becomes active
      stamperoo = True
      watermelon.move(random.randint(0, 400), random.randint(0, 480))
      timed = True
      start = True

  if real_time >= 7 and start_2 == False: #watermelon starts to move and becomes active
      stampern = True
      orange.move(random.randint(0, 400), random.randint(0, 480))
      timed = True
      start_2 = True

  if stamp == True:
      actual_time = time.time()
      realer_time = round(actual_time - current_time, 2)
      ticks = round(realer_time + .8, 2)
      tick_tick = realer_time + 6
      ticked = realer_time + 3

  if stamper == True and actions == True: #apple timestamp
      count = timer + real_time
      stamper = False

  if stamperoo == True and actions == True: #watermelon timestamp
      w_count = w_timer + real_time
      stamperoo = False

  if stampern == True and actions == True: #pineapple timestamp
      o_count = o_timer + real_time
      stampern = False

  if reload == True:
      if real_time >= ticks:
          bullets += 1
          if bullets > 6:
              bullets = 6
          if bullets == 6:
              f_reload_sound.play()
          else:
              reload_sound.play()
          stamp = True
          reload = False
          action = True


  if ult == True:
    if tick_tick <= real_time:
        score += 20
        action = True
        ult = False
        stamp = True
        actions = True
        stamper = True
        seconds_left += 6
    if ticked <= real_time:
        timer += .4
        a_clicks += 1
        apple.move(random.randint(0, 600 - apple.image_size[0]), random.randint(0, 480 - apple.image_size[1]))
        if real_time >= 4:
            watermelon.move(random.randint(0, 600 - watermelon.image_size[0]), random.randint(0, 480 - watermelon.image_size[1]))
            w_clicks += 1
            if real_time >= 7:
                orange.move(random.randint(0, 600 - orange.image_size[0]), random.randint(0, 480 - orange.image_size[1]))
                o_clicks += 1
        ticked += .5

  if seconds_left <= 0:
      game_screen = False
      end_screen = True

  if bullets == 0:
      action = False

  if count <= real_time and actions == True:
      apple.move(random.randint(0, 600 - apple.image_size[0]), random.randint(0, 480 - apple.image_size[1]))
      stamper = True

  if w_count <= real_time and actions == True:
      watermelon.move(random.randint(0, 600 - watermelon.image_size[0]), random.randint(0, 480 - watermelon.image_size[1]))
      stamperoo = True

  if o_count <= real_time and actions == True:
      orange.move(random.randint(0, 600 - orange.image_size[0]), random.randint(0, 480 - orange.image_size[1]))
      stampern = True

  if counter <= real_time:
      if ult == False:
          seconds_left -= 1
      bomb.move(random.randint(0, 600 - bomb.image_size[0]), random.randint(0, 480 - bomb.image_size[1]))
      counter += 1

  pygame.display.update()

while end_screen:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:  # hide end screen if player X's out
           end_screen = False
   color = (255, 255, 0)
   end_font = pygame.font.SysFont("Arial", 50)
   score_font = pygame.font.SysFont("Arial", 20)
   final_score = score_font.render("Final score: " + str(score), True, color)
   time_score = score_font.render("You survived for: " + str(real_time) + " seconds", True, color)
   apple_score = score_font.render("Apples shot : " + str(a_clicks), True, color)
   watermelon_score = score_font.render("Watermelons shot : " + str(w_clicks), True, color)
   orange_score = score_font.render("Oranges shot : " + str(o_clicks), True, color)
   game_over_message = end_font.render("GAME OVER", True, red_rgb)
   screen.blit(bg, (0, 0))  # show background
   screen.blit(time_score, (300, 300))
   screen.blit(apple_score, (300, 325))
   screen.blit(watermelon_score, (300, 350))
   screen.blit(orange_score, (300, 375))
   screen.blit(game_over_message, (275, 200))  # show game over msg
   screen.blit(final_score, (300, 275))  # show final score
   pygame.display.update()  # last line in the main run loop