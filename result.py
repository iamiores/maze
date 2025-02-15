#from pygame.sprite import Group
import pygame.time
from pygame import *
'''Необхідні класи'''

# клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас-спадкоємець для спрайту-гравця (керується стрілками)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас-спадкоємець для спрайта-ворога (переміщається сам)
class Enemy(GameSprite):
    direction = "left"

    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

      
# клас для спрайтів-перешкод
class Wall(sprite.Sprite):
    def __init__(self, color_r, color_g, color_b, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_r = color_r
        self.color_g = color_g
        self.color_b = color_b
        self.width = wall_width
        self.height = wall_height
        # картинка стіни - прямокутник потрібних розмірів та кольору
        self.image = Surface((self.width, self.height))
        self.image.fill((color_r, color_g, color_b))
        # кожен спрайт повинен зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        draw.rect(window, (self.color_r, self.color_g, self.color_b), (self.rect.x, self.rect.y, self.width, self.height))


# Ігрова сцена:
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load(
    "background.jpg"), (win_width, win_height))

# Персонажі гри:
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

# стіни
w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 200, 130, 10, 350)
w5 = Wall(154, 205, 50, 450, 130, 10, 360)
w6 = Wall(154, 205, 50, 300, 20, 10, 350)
w7 = Wall(154, 205, 50, 390, 120, 130, 10)


game = True
finish = False
clock = time.Clock()
FPS = 60

# написи
font.init()
font = font.Font(None, 70)
win = font.render('ТИ ПЕРЕМІГ!', True, (255, 215, 0))
lose = font.render('СПРОБУЙ ЩЕ!', True, (180, 0, 0))

# музика
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

# Функція скидання гравця та ворога
def reset_game():
    player.rect.x = 5
    player.rect.y = win_height - 80
    monster.rect.x = win_width - 80
    monster.rect.y = 280

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()


    # Ситуація "Програш"
    if (sprite.collide_rect(player, monster)
            or sprite.collide_rect(player, w1)
            or sprite.collide_rect(player, w2)
            or sprite.collide_rect(player, w3)
            or sprite.collide_rect(player, w4)
            or sprite.collide_rect(player, w5)
            or sprite.collide_rect(player, w6)
            or sprite.collide_rect(player, w7)
    ):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()

        #додаткова умова на оновлення гри
        #дісплей встигає оновитися
        display.update()
        #затримка надпису
        pygame.time.delay(1000)
        #повертаємось до гри
        finish = False
        reset_game()

    # Ситуація "Перемога"
    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        money.play()

        #додаткова умова на оновлення гри
        display.update()
        pygame.time.delay(1000)
        finish = False
        reset_game()

    display.update()
    clock.tick(FPS)