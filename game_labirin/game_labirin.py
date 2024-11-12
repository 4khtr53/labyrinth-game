from pygame import *
from random import *
import math
import pygame

font.init()
init() #instal penting2

#step 2 buat font
font1 = font.Font(None, 80) 
win = font1.render('YOU ESCAPED!', True, (255, 255, 255))
lose = font1.render('YOU GOT CAUGHT', True, (255, 51, 0))

font2 = font.Font(None, 36)


#step 3: buat variable untuk simpen gambar
img_back = "background.jpg"  
img_cop = "cop2.png"  
img_prisoner = "prisoner.png" 
img_finish = "locked_door.png" 
img_key = "key.png"


#step 4: buat karakter game -> buat kelas (object)
# parent class for other sprites
class character(sprite.Sprite):
    # class constructor
        def __init__(self, player_image, player_x, player_y, width, height, player_speed):
            # Call for the class (Sprite) constructor:
            sprite.Sprite.__init__(self)

            # every sprite must store the image property
            self.image = transform.scale(image.load(player_image), (width, height))
            self.speed = player_speed

            # every sprite must have the rect property – the rectangle it is fitted in
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
            self.kena_kunci = False
            self.velocity = pygame.math.Vector2(5, 5)

        # method drawing the character on the window
        def draw(self): #upload karakter in screen
            screen.blit(self.image, (self.rect.x,self.rect.y))
        def tabrakan(self, karakter_lain):
            return self.rect.colliderect(karakter_lain)



class main_player(character):
        def moving(self):
            keys = key.get_pressed()
            if keys[K_left]:
                self.rect.x -= self.velocity.x
            if keys[K_right]:
                self.rect.x += self.velocity.x
            if keys[K_up]:
                self.rect.y -= self.velocity.y
            if keys[K_down]:
                self.rect.y += self.velocity.y

            # Check for wall collisions and bounce
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    # Horizontal collision
                    if self.velocity.x > 0 and self.rect.right >= wall.rect.left:
                        #self.rect.right = wall.rect.left
                        self.velocity.x *= -1
                    elif self.velocity.x < 0 and self.rect.left <= wall.rect.right:
                        #self.rect.left = wall.rect.right
                        self.velocity.x *= -1

                    # Vertical collision
                    if self.velocity.y > 0 and self.rect.bottom >= wall.rect.top:
                        #self.rect.bottom = wall.rect.top
                        self.velocity.y *= -1
                    elif self.velocity.y < 0 and self.rect.top <= wall.rect.bottom:
                        #self.rect.top = wall.rect.bottom
                        self.velocity.y *= -1


class enemy(character):
        def automatic_move_updown(self):
            #cek apakah enemy di batasan atas

            if self.rect.y > 5:
                #jika enemy di atas nanti kebawah
                self.gerak = "down"

            if self.rect.y < height:
                #jika enemy di bawah nanti keatas
                self.gerak = "up"

            #cek jika betul gerakan = atas/bawah
            if self.gerak == 'down':
                self.rect.y += self.speed
            else: 
                self.rect.y -= self.speed
        
        def automatic_move_side(self):
            #cek apakah enemy di batasan atas

            if self.rect.x > 5:
                #jika enemy di atas nanti kebawah
                self.gerak = "right"

            if self.rect.x < width:
                #jika enemy di bawah nanti keatas
                self.gerak = "left"

            #cek jika betul gerakan = atas/bawah
            if self.gerak == 'right':
                self.rect.x += self.speed
            else: 
                self.rect.x -= self.speed


class wall(pygame.sprite.Sprite):
        def __init__(self, x, y, width, height,color):
            super().__init__()
            self.image = pygame.Surface((width, height))
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.color = color
        def draw(self):
            draw.rect(screen,self.color,self.rect)
        def collide_character(self,other_character):
            return self.rect.colliderect(other_character)

#step 5: buat screen
width = 900
height = 750

screen = display.set_mode((width,height))
display.set_caption("Prison Escape Game")
background = transform.scale(image.load(img_back),(width,height))


mc_width = 50
mc_height = 50
mc_speed = 3
mc = main_player(img_prisoner, 130, 0, mc_width, mc_height, mc_speed)


cop_width = 50
cop_height = 50
cop_speed = 4
cop = enemy(img_cop, 130, 0, cop_width, cop_height, mc_speed)


finish_width = 60
finish_height = 60
finish_speed = 0
finish = character(img_finish, 130, 0, finish_width, finish_height, mc_speed)


key_width = 25
key_height = 25
key_speed = 0
key = character(img_key, 130, 0, key_width, key_height, mc_speed)


wall_color = (25, 25, 25)
wall1 = wall(0,0,30,750,wall_color)
wall2 = wall(0,0,750,30,wall_color)
wall3 = wall(0,720,750,30,wall_color)
wall4 = wall(720,0,30,750,wall_color)
wall5 = wall(100,0,10,380,wall_color)
wall6 = wall(100,575,10,380,wall_color)
wall7 = wall(100,575,100,10,wall_color)
wall8 = wall(200,100,10,485,wall_color)
wall9 = wall(200,100,450,10,wall_color)
wall10 = wall(300,200,450,10,wall_color)
wall11 = wall(200,300,450,10,wall_color)
wall12 = wall(300,300,10,285,wall_color)
wall13 = wall(300,575,100,10,wall_color)
wall14 = wall(400,400,10,185,wall_color)
wall15 = wall(200,650,300,10,wall_color)
wall16 = wall(500,400,10,260,wall_color)
wall17 = wall(500,400,260,10,wall_color)
wall18 = wall(620,500,10,260,wall_color)

game_start = True

fps = time.Clock()

while game_start:
    screen.blit(background, (0,0))
    mc.draw()
    cop.draw()
    key.draw()
    finish.draw()
    wall1.draw()
    wall2.draw()
    wall3.draw()
    wall4.draw()
    wall5.draw()
    wall6.draw()
    wall7.draw()
    wall8.draw()
    wall9.draw()
    wall10.draw()
    wall11.draw()
    wall12.draw()
    wall13.draw()
    wall14.draw()
    wall15.draw()
    wall16.draw()
    wall17.draw()
    wall18.draw()
    for e in event.get():
        if e.type == QUIT:
            quit()
    display.update()
    fps.tick(60)











