from pygame import*


class GameSprite(sprite.Sprite):
    def __init__(self, image_pl,x,y,speed):
        super().__init__()

        self.image = transform.scale(image.load(image_pl),(50,50))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def onScreen(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_LEFT]:
            self.rect.x-=speed
        elif key_pressed[K_RIGHT]:
            self.rect.x+=speed
        elif key_pressed[K_UP]:
            self.rect.y-=speed
        elif key_pressed[K_DOWN]:
            self.rect.y+=speed

class Enemy(GameSprite):
    direction="left"
    def update(self):
        if self.rect.x<win_width - 230:
            self.direction="right"
        if self.rect.x>win_width-85:
            self.direction="left"
        if self.direction=="left":
            self.rect.x-=self.speed
        else:
            self.rect.x+=self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x,wall_y, wall_width, wall_height):
        super().__init__()
        self.color1=color1
        self.color2=color2
        self.color3=color3
        self.width=wall_width
        self.height=wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1,color2,color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))

display.set_caption("Ghost Maze")
#background = transform.scale(image.load("somePicture.png"))

hero = Player("pac.png",5,win_height-80,4)
enemy = Enemy("ghost.png",win_width-80, 280,2)
treasure = GameSprite("treasure.png", win_width-120,win_height-80,0)


wall1 = Wall(0,0,200,100,20,450,10)
wall2 = Wall(0,0,200,100,480,360,10)
wall3 = Wall(0,0,200,100,20,10,380)
wall4 = Wall(0,0,200,180,110,10,370)
wall5 = Wall(0,0,200,260,20,10,380)
wall6 = Wall(0,0,200,450,140,10,340)
wall7 = Wall(0,0,200,360,140,150,10)


font.init()
font = font.Font(None,70)
win = font.render("YOU WIN", True, (255,215,0))
lose = font.render("YOU LOSE", True, (180,0,0))

speed=1
game = True
clock = time.Clock()
frames = 60

finish = False

while game:
 
    for x in event.get():
        if x.type == QUIT:
            game = False

    if finish !=True:
        window.fill((0,0,0))
        hero.update()
        enemy.update()

        hero.onScreen()
        enemy.onScreen()
        treasure.onScreen()

        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        
        wall_list = [wall1,wall2,wall3,wall4,wall5,wall6,wall7]
        if sprite.collide_rect(hero,enemy):
            finish = True
            window.blit(lose,(200,200))
        # elif sprite.colide_rect(hero, wall1):
        #     finish = True
        for x in wall_list:
            if sprite.collide_rect(hero,x):
                finish = True
                window.blit(lose,(200,200))

        if sprite.collide_rect(hero,treasure):
            finish = True
            window.blit(win,(200,200))

    display.update()
    clock.tick(frames)

