from random import randint, random
from time import sleep
import threading
import pygame

pygame.init()

#Variables
screen = pygame.display.set_mode((1386, 800))
running = True
QUIT_flag = False
WINNER_flag = False
is_collided = False
exit_event = threading.Event()
thread_list = []
tank_image = pygame.image.load("Sprites/tank.png").convert_alpha()
tank_image_width = tank_image.get_width()
tank_image_height = tank_image.get_height()
health = 3
#Sounds
bomb_explosion_sound = pygame.mixer.Sound("Sounds/bomb_explosion.ogg")
helicopter_hovering_sound = pygame.mixer.music.load("Sounds/Helicopter_sound.ogg")
helicopter_hovering_sound = pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()
# tank_image = pygame.transform.scale(tank_image, (tank_image_width*0.25, tank_image_height*0.25))
bomb_image = pygame.image.load("Sprites/bomb.png").convert_alpha()
bomb_image_width = bomb_image.get_width()
bomb_image_height = bomb_image.get_height()

bomb_explode = pygame.image.load("Sprites/bomb_explode.png").convert_alpha()
bombexplode_image_width = bomb_explode.get_width()
bombexplode_image_height = bomb_explode.get_height()
bomb_explode = pygame.transform.scale(bomb_explode, (bombexplode_image_width*0.1, bombexplode_image_height*0.1))

heli_image = pygame.image.load("Sprites/helicopter.png").convert_alpha()
heli_image_width = heli_image.get_width()
heli_image_height = heli_image.get_height()
heli_image = pygame.transform.scale(heli_image, (heli_image.get_width()*0.3, heli_image.get_height()*0.3))
#road_image = pygame.image.load("road.png").convert_alpha()
# bomb_image = pygame.transform.scale(bomb_image, (bomb_image_width*0.25, bomb_image_height*0.25))
tx = 0
ty = 600
screen.fill("LightSkyBlue")
pygame.draw.rect(screen, "SaddleBrown", (0,653, 1386,800), 0)
#Main
def rect_fill(coord_x, coord_y, image_width, image_height):
    pygame.draw.rect(screen, "LightSkyBlue", (coord_x, coord_y, image_width*0.25, image_height*0.25), 0)

def display_health(health):
    rect_health = pygame.draw.rect(screen, "Black", (1000, 700, 200,40))
    health_text = pygame.font.Font(None, 35)
    health_text_render = health_text.render(f'Tank Lifes: {health}', True, "red")
    screen.blit(health_text_render, (rect_health.x+26, rect_health.y+9))

display_health(health)

def result():
    if WINNER_flag and exit_event:
        msg = "YOU WON!"
        color = "Green"

    elif exit_event:
        msg = "You LOST!"
        color = "Red"

    result_text = pygame.font.Font(None, 100)
    result_text_render = result_text.render(msg, True, color)
    screen.blit(result_text_render, (1386/2 - 200, 800/2 - 100))
    pygame.display.update()
    print("Game Over!")


class Tank():
    def __init__(self, t_x:int, t_y:int, image =None, speed = None):
        self.t_x = t_x
        self.t_y = t_y
        self.image = pygame.transform.scale(image, (tank_image_width*0.25, tank_image_height*0.25))
        self.speed = speed
        self.max_left = True
        self.max_right = False      
        screen.blit(self.image, (tx, ty))
        pygame.display.update()

    def move(self, key_type):
        global tx, ty, WINNER_flag, health
        # screen.fill((0,0,0))
        if key_type == "left":
            rect_fill(self.t_x, self.t_y, tank_image_width, tank_image_height)
            tank1.max_right = False
            self.t_x -= 0.7
            if self.t_x < 0:
                self.t_x = 0
                tank1.max_left = True
        if key_type == "right":
            rect_fill(self.t_x, self.t_y, tank_image_width, tank_image_height)
            tank1.max_left = False
            self.t_x += 0.5
            if self.t_x > 1300:
                self.t_x = 1300
                WINNER_flag = True
                tank1.max_right = True
                result()
                exit_event.set()
                sleep(3)
                # globals()["exit_event"] = True
        #print(f'For tank: ({self.t_x}, {self.t_y})')
        tx = self.t_x
        ty = self.t_y
        screen.blit(self.image, (self.t_x, self.t_y))
        pygame.display.update()



class Bomb():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y 
        self.image = pygame.transform.scale(bomb_image, (bomb_image_width*0.25, bomb_image_height*0.25))

    def fall(self):
            global QUIT_flag, tx, ty, tank_image_width, tank_image_height, is_collided, running, WINNER_flag, health
            while not QUIT_flag:
                sleep(0.005)
                rect_fill(self.x, self.y, bomb_image_width, bomb_image_height)  
                self.y = self.y + 2
                screen.blit(self.image, (self.x, self.y))
                pygame.display.update()
                tank_rect = pygame.Rect(tx, ty, tank_image_width*0.25, tank_image_height*0.25)
                bomb_rect = pygame.Rect(self.x, self.y , bomb_image_width*0.25, bomb_image_height*0.25 )
                if pygame.Rect.colliderect(tank_rect, bomb_rect) and not is_collided:
                    # print("collided")
                    rect_fill(self.x, self.y, bomb_image_width, bomb_image_height)
                    pygame.display.update()
                    self.x = randint(0, 1386)
                    self.y = 0
                    health -= 1
                    display_health(health)
                    bomb_explosion_sound.play()
                    #print("You have",health, "out of 3 lifes of tank left!")
                    if health == 0:
                        bomb_explosion_sound.play()
                        result()
                        exit_event.set()
                        screen.blit(bomb_explode, (tank_rect.x, tank_rect.y-20))
                        pygame.display.update()
                        sleep(3)
                    # print("-----------------")
                    # print("Bomb rect", self.x, self.y)
                    # print("Tank rect", tank_rect.x, tank_rect.y )
                    # print("-----------------")

                if self.y >= ty+10:
                    rect_fill(self.x, self.y, bomb_image_width, bomb_image_height)
                    pygame.display.update()
                    self.x = randint(60, 1250)
                    self.y = 60
                if exit_event.is_set():
                    break


class Helicopter(threading.Thread):
    def __init__(self, x, y, h_img):
        self.x = x
        self.y = y
        self.h_img = h_img
    def move(self):
        forward = True
        while running:
            sleep(0.005)
            pygame.draw.rect(screen, "LightSkyBlue", (self.x, self.y, self.h_img.get_width(), self.h_img.get_height()), 0)
            if forward:    
                self.x += 2
            else:
                self.x -=2
            screen.blit(self.h_img, (self.x, self.y))
            if self.x == 1050:
                forward = False
                rect_heli_fill = pygame.draw.rect(screen, "lightblue3", (self.x, self.y, self.h_img.get_width(), self.h_img.get_height()), 0)
                self.h_img = pygame.transform.flip(self.h_img, True, False)
                screen.blit(self.h_img, (self.x, self.y))
            
            if self.x == 0:
                forward = True
                rect_heli_fill = pygame.draw.rect(screen, "lightblue3", (self.x, self.y, self.h_img.get_width(), self.h_img.get_height()), 0)
                self.h_img = pygame.transform.flip(self.h_img, True, False)
                screen.blit(self.h_img, (self.x, self.y))

            pygame.display.update()





#Loop events 
class tank_anim(threading.Thread, Bomb):

    def run(self):

        global running 
        # running = True
        while running:
            sleep(0.005)
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and not tank1.max_right :
                tank1.move("right")
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and not tank1.max_left:
                tank1.move("left")
            if exit_event.is_set():
                running = False
                break

class bomb_anim_1(threading.Thread):
    def run(self):
        bomb1.fall()
        

class bomb_anim_2(threading.Thread):
    def run(self):
        bomb2.fall()

class bomb_anim_3(threading.Thread):
    def run(self):
        bomb3.fall()

class bomb_anim_4(threading.Thread):     
    def run(self):    
        bomb4.fall()     
     
class bomb_anim_5(threading.Thread):     
    def run(self):     
        bomb5.fall()     

class bomb_anim_6(threading.Thread):     
    def run(self):     
        bomb6.fall()

class heli_anim(threading.Thread):
    def run(self):
        helicopter.move()



tank1 = Tank(tx, ty, tank_image)
bomb1 = Bomb(randint(60,1250), 60, bomb_image)
bomb2 = Bomb(randint(60,1250), 60, bomb_image)
bomb3 = Bomb(randint(60,1250), 60, bomb_image)
bomb4 = Bomb(randint(60,1250), 60, bomb_image)
bomb5 = Bomb(randint(60,1250), 60, bomb_image)
bomb6 = Bomb(randint(60,1250), 60, bomb_image)
helicopter = Helicopter(0,0, heli_image)

tank_anim1 = tank_anim()
bomb_anim1 = bomb_anim_1()
bomb_anim2 = bomb_anim_2()
bomb_anim3 = bomb_anim_3()
bomb_anim4 = bomb_anim_4()
bomb_anim5 = bomb_anim_5()
bomb_anim6 = bomb_anim_6()
heli_anim_move = heli_anim()


thread_list = [tank_anim1,
              bomb_anim1,
              bomb_anim2,
              bomb_anim3,
              bomb_anim4,
              bomb_anim5,
              bomb_anim6,
              heli_anim_move]

def Start_game():
    for thread_event in thread_list:
        thread_event.start()

if __name__ == "__main__":
    Start_game()

while running:
    pygame.draw.line(screen, "Green", (1300, 0), (1300, 652), 4)
    # pygame.draw.rect(screen, "SaddleBrown", (0,652, 1386,800), 0)
    if health == 0:
        QUIT_flag = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT_flag = True
            running = False