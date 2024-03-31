import pygame.display
from pygame import *

#CLASSES
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def movement(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 75:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 75:
            self.rect.y += self.speed


class Enemy(GameSprite):
    direction = 'left'

    def movement(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
            if self.rect.x <= 460:
                self.direction = 'right'
        elif self.direction == 'right':
            self.rect.x += self.speed
            if self.rect.x >= win_width - 75:
                self.direction = 'left'


class Wall(sprite.Sprite):
    def __init__(self, color_r, color_g, color_b, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_r = color_r
        self.color_g = color_g
        self.color_b = color_b
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.image = Surface((self.wall_width, self.wall_height))
        self.image.fill((self.color_r, self.color_g, self.color_b))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        draw.rect(window, (self.color_r, self.color_g, self.color_b), (self.rect.x, self.rect.y, self.wall_width, self.wall_height))


#SETTINGS


win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
bg = transform.scale(image.load('background.jpg'), (win_width, win_height))
icon = image.load('maze.png')
pygame.display.set_icon(icon)

#CHARACTERS
player = Player('hero.png', 25, win_height - 500, 4)
monster = Enemy('cyborg.png', win_width - 80, 330, 3)
# final = GameSprite('treasure.png', win_width - 230, win_height - 70, 0)

#MAZE WALLS
w1 = Wall(154, 205, 50, 110, 180, 110, 10)
w2 = Wall(154, 205, 50, 100, 360, 240, 10)
w3 = Wall(154, 205, 50, 110, 0, 10, 90)
w4 = Wall(154, 205, 50, 220, 75, 10, 200)
w5 = Wall(154, 205, 50, 440, 100, 10, 140)
w6 = Wall(154, 205, 50, 330, 0, 10, 360)
w7 = Wall(154, 205, 50, 410, 100, 160, 10)
w8 = Wall(154, 205, 50, 570, 0, 10, 100)
w9 = Wall(154, 205, 50, 440, 310, 140, 10)
w10 = Wall(154, 205, 50, 90, 270, 140, 10)
w11 = Wall(154, 205, 50, 90, 270, 10, 150)
w12 = Wall(154, 205, 50, 440, 230, 140, 10)
# w13 = Wall(154, 205, 50, 0, 360, 250, 10)
w14 = Wall(154, 205, 50, 440, 320, 10, 250)
w15 = Wall(154, 205, 50, 440, 400, 140, 10)
w16 = Wall(154, 205, 50, 570, 190, 10, 40)
w17 = Wall(154, 205, 50, 540, 180, 40, 10)
w18 = Wall(154, 205, 50, 570, 100, 50, 10)
w19 = Wall(154, 205, 50, 190, 450, 10, 80)
w20 = Wall(154, 205, 50, 270, 370, 10, 50)
w21 = Wall(154, 205, 50, 360, 450, 10, 80)

#MUSIC
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
mixer.music.set_volume(0.1)

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

font.init()
font = font.Font(None, 70)
win = font.render('win', True, (255, 215, 0))
lose = font.render('lose', True, (255, 215, 0))

#GAME CYCLE
game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    window.blit(bg, (0, 0))

    for even in event.get():
        if even.type == QUIT:
            game = False

    if not finish:
        # final.show()
        player.movement()
        monster.movement()
        player.show()
        monster.show()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        w16.draw_wall()
        w17.draw_wall()
        w18.draw_wall()
        w19.draw_wall()
        w20.draw_wall()
        w21.draw_wall()

        if (sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1)
            or sprite.collide_rect(player, w2)
            or sprite.collide_rect(player, w3)
            or sprite.collide_rect(player, w4)
            or sprite.collide_rect(player, w5)
            or sprite.collide_rect(player, w6)
            or sprite.collide_rect(player, w7)
            or sprite.collide_rect(player, w8)
            or sprite.collide_rect(player, w9)
            or sprite.collide_rect(player, w10)
            or sprite.collide_rect(player, w11)
            or sprite.collide_rect(player, w12)
            or sprite.collide_rect(player, w14)
            or sprite.collide_rect(player, w15)
            or sprite.collide_rect(player, w16)
            or sprite.collide_rect(player, w17)
            or sprite.collide_rect(player, w18)
            or sprite.collide_rect(player, w19)
            or sprite.collide_rect(player, w20)
            or sprite.collide_rect(player, w21)):

            finish = True
            window.blit(lose, (200, 200))
            kick.play()

        # if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()

        display.update()
        clock.tick(FPS)
