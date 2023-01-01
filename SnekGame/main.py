
import pygame
import random
from time import sleep

pygame.init()
WIDTH , HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
border = pygame.image.load("Graphics/snakegameborder.jpg")
snake_head_up = pygame.image.load("Graphics/snake_head_up.png")
snake_head_up = pygame.transform.scale(snake_head_up, (30,30))
snake_head_down = pygame.image.load("Graphics/snake_head_down.png")
snake_head_down = pygame.transform.scale(snake_head_down, (30,30))
snake_head_left = pygame.image.load("Graphics/snake_head_left.png")
snake_head_left = pygame.transform.scale(snake_head_left, (30,30))
snake_head_right = pygame.image.load("Graphics/snake_head_right.png")
snake_head_right = pygame.transform.scale(snake_head_right, (30,30))
snake_body = pygame.image.load("Graphics/snake_body.png")
snake_body = pygame.transform.scale(snake_body, (30,30))
snack_apple = pygame.image.load("Graphics/snack.png").convert_alpha()
snack_coords_x = [i for i in range(0, 571, 30)]
snack_coords_y = [i for i in range(0, 571, 30)]
snack_x = 360
snack_y = 360
snake_eat_sound = pygame.mixer.Sound("Sound/snakesoundcollect.ogg")
score_sound = pygame.mixer.Sound("Sound/scoresound.ogg")
lose_sound = pygame.mixer.Sound("Sound/lose_sound.ogg")
running = True
apple_Ate = False
s_direction = ''
tx, ty = 300,300
score = 0
snake_coords = []

class Snake():
    def __init__(self, x, y, head, body) -> None:
        global snake_coords
        self.can_up = True
        self.can_down = False
        self.can_left = True
        self.can_right = True
        self.x = x
        self.y = y
        self.head = head
        self.body = body
        self.x, self.y = tx, ty
        snake_coords = [[self.x, self.y]]
    
    def move_up(self):
        self.y -= 30
        self.head = snake_head_up
        snake_coords.pop()
        snake_coords.insert(0, [self.x, self.y ])

    def move_down(self):
        self.y +=30
        self.head = snake_head_down
        snake_coords.pop()
        snake_coords.insert(0, [self.x, self.y])

    def move_right(self):
        self.x +=30
        self.head = snake_head_right
        snake_coords.pop()
        snake_coords.insert(0, [self.x, self.y])
        

    def move_left(self):
        self.x -= 30
        self.head = snake_head_left
        snake_coords.pop()
        snake_coords.insert(0, [self.x, self.y])
        

    def loop_move(self, key:str):
        if key == '':
            return
        self.display(False)
        if key == "up" and self.can_down == False:
            self.move_up()
            self.can_left, self.can_right = True, True
        if key == "down" and self.can_up == False:
            self.move_down()
            self.can_left, self.can_right = True, True
        if key == "right" and self.can_left == False:
            self.move_right()
            self.can_up, self.can_down = True, True
        if key == "left" and self.can_right == False:
            self.move_left()
            self.can_up, self.can_down = True, True
        self.display(True)
        self.eat_Snack()
        self.check_Game_over()

    def grow(self):
        head_x, head_y = snake_coords[0][0], snake_coords[0][1]
        if s_direction == "up":
            snake_coords.insert(0,[head_x, head_y] )
        if s_direction == "down":
            snake_coords.insert(0,[head_x, head_y] )
        if s_direction == "left":
            snake_coords.insert(0,[head_x, head_y] )
        if s_direction == "right":
            snake_coords.insert(0,[head_x, head_y] )
        else:
            return

    def spawn_Snack(self):
        global apple_Ate, snack_x, snack_y
        if apple_Ate:
            globals()["snack_x"] = random.choice(snack_coords_x)
            globals()["snack_y"] = random.choice(snack_coords_y)
            apple_Ate = False
        else:
            return

    def eat_Snack(self):
        global snake_coords
        apple_rect = pygame.Rect(snack_x, snack_y, 30,30)
        head_rect = pygame.Rect(snake_coords[0][0], snake_coords[0][1], 30,30)
        if head_rect.colliderect(apple_rect):
            self.grow()
            globals()["score"] +=1
            if score % 10 == 0 and score != 0:
                score_sound.play()
            else:
                snake_eat_sound.play()
            globals()["apple_Ate"] = True 
            self.spawn_Snack()
            print(score)


    def coord_append(self, x1, y1):
        global snake_coords
        self.x1 = x1
        self.y1 = y1
        snake_coords = snake_coords[:] + [[self.x1, self.y1]]

    def display(self, color:bool):
        global snake_coords, border, snack_apple, snack_x, snack_y
        screen.fill((0,0,0))
        screen.blit(border, (0,0))
        screen.blit(snack_apple, (snack_x, snack_y))
        self.display_Score(score)
        for i in range(len(snake_coords)):
            if i == 0:
                screen.blit(self.head, (snake_coords[i][0], snake_coords[i][1]))
            else:
                screen.blit(self.body, (snake_coords[i][0], snake_coords[i][1]))
        pygame.display.update()

    def check_Game_over(self):
        global snake_coords
        head_rect = pygame.Rect(snake_coords[0][0], snake_coords[0][1], 30,30)
        for i in range(3, len(snake_coords)):
            body_rect = pygame.Rect(snake_coords[i][0], snake_coords[i][1], 30,30)
            if head_rect.colliderect(body_rect):
                self.display_Lost()

        if not border.get_rect().contains(head_rect):
            self.display_Lost()

    def display_Score(self, score):
        self.score = score
        score_font = pygame.font.Font("Fonts/Symtext.ttf", 20)
        score_text = score_font.render(f'Score: {str(self.score)}', True, "White")
        screen.blit(score_text, (460, 570))

    def display_Lost(self): 
        lose_sound.play()
        lost_score_font = pygame.font.Font("Fonts/Symtext.ttf", 50)
        lost_score_text = lost_score_font.render(f'Your score: {score}', True, "Red")
        screen.blit(lost_score_text, (90,300))
        pygame.display.update()
        pygame.time.wait(1500)
        globals()["running"] = False


snake = Snake(tx, ty, snake_head_up, snake_body)
snake.coord_append(tx, ty+30)
snake.coord_append(tx, ty+60)
snake.display(True)
snake.display_Score(score)

while running:     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        start = False
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and snake.can_up:
            s_direction = "up"
            snake.can_down = False
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and snake.can_down:
            s_direction = "down"
            snake.can_up = False
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and snake.can_right:
            s_direction = "right"
            snake.can_left = False
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and snake.can_left:
            s_direction = "left"
            snake.can_right = False
        if (keys[pygame.K_p]):
            s_direction = ''
    snake.loop_move(s_direction)
    clock.tick(7)