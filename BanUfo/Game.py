import pygame
import random
import pickle
import sys

pygame.init()

# Kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Bắn UFO")

clock = pygame.time.Clock()

if len(sys.argv) > 1:
    player_name = sys.argv[1]

enemy_lives = True
boss_lives = False
game_over = False
moreBullet = False
running = True

# Tải hình ảnh
playerImg = pygame.image.load('img/player.png')
playerImg = pygame.transform.scale(playerImg, (50, 50))

enemyImg = pygame.image.load('img/enemy.png')
enemyImg = pygame.transform.scale(enemyImg, (64, 64))

bulletImg = pygame.image.load('img/bullets_enemy.png')
bulletImg = pygame.transform.scale(bulletImg, (16, 16))

OnebulletImg = pygame.image.load('img/OneBullet.png')
OnebulletImg = pygame.transform.scale(OnebulletImg, (16, 16))

boss1Img = pygame.image.load('img/boss2.png')
boss1Img = pygame.transform.scale(boss1Img, (180, 150))

enemy_bulletImg = pygame.image.load('img/bullet.png')
enemy_bulletImg = pygame.transform.scale(enemy_bulletImg, (16, 16))

heartImg = pygame.image.load('img/heart.png')
heartImg = pygame.transform.scale(heartImg, (25, 25))



# hinh nen
background = pygame.image.load('img/bg.jpeg')
background = pygame.transform.scale(background, (800, 800))

# Lấy kích thước hình nền
background_width, background_height = background.get_size()

# Thiết lập vị trí ban đầu của hình nền
bg_y1 = 0
bg_y2 = -background_height + 200

# Thiết lập tốc độ di chuyển
scroll_speed = 2

# Tải âm thanh
soundBG = pygame.mixer.Sound("sound/may-tinh-song.mp3")
soundBulletHit = pygame.mixer.Sound("sound/laser-zap-90575.mp3")
soundBossKill = pygame.mixer.Sound("sound/Video-10-diem-tiktok-www_tiengdong_com.mp3")
soundAppearBoss = pygame.mixer.Sound("sound/nani_-meme-sound-effect-su0k4q3yrfw-mp3cut.mp3")

soundTakeBuff = pygame.mixer.Sound("sound/take-buff-buy_1.mp3")

soundGameOver = pygame.mixer.Sound("sound/game-over-galaxy-brain-meme.mp3")

soundBG.set_volume(0.1)         # 50% volume
soundBulletHit.set_volume(0.1)  # 50% volume
soundBossKill.set_volume(0.4)   # 50% volume
soundAppearBoss.set_volume(0.4) # 50% volume
soundTakeBuff.set_volume(0.4)   # 50% volume
soundGameOver.set_volume(0.4)   # 50% volume

# Định nghĩa màu
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (100, 100, 100)

cooldown = 0
cooldowned = 100

# Exp1 = pygame.image.load("img/enemy.png")
# Exp1 = pygame.transform.scale(Exp1, (64, 64))
# Exp2 = pygame.image.load("img/enemy1.png")
# Exp2 = pygame.transform.scale(Exp2, (64, 64))
# Exp3= pygame.image.load("img/enemy2.png")
# Exp3 = pygame.transform.scale(Exp3, (64, 64))
# imageArray = [
#     Exp1,
#     Exp2,
#     Exp3
# ]
# (pygame.sprite.Sprite)
class Character:
    def __init__(self, hp, speed, width, height, image):

        # super().__init__()
        # self.index_image = 0
        # self.images = image
        # self.image = self.images[self.index_image]
        # self.rect = self.image.get_rect()
        # self.rect.topleft = (x,y)

        self.hp = hp
        self.speed = speed
        self.width = width
        self.height = height
        self.image = image
        self.direction_x = 1  # Hướng mặc định là sang phải
        self.direction_y = 1

        self.x = screen_width // 2 - self.width // 2  # Căn giữa người chơi theo chiều ngang
        self.y = screen_height // 2 - self.height // 2  # Căn giữa người chơi theo chiều dọc
    
    # def update(self):
    #     self.index_image += self.speed
    #     if int(self.index_image) >= len(self.images):
    #         self.index_image = 0
    #     self.image = self.images[int(self.index_image)]
    # Cập nhật di chuyển của nhân vật
    def move(self):
        global cooldown
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= 2 * self.speed
        if keys[pygame.K_d]:
            self.x += 2 * self.speed
        if keys[pygame.K_w]:
            self.y -= 2 * self.speed
        if keys[pygame.K_s]:
            self.y += 2 * self.speed
        # thực hiện dash
        if keys[pygame.K_SPACE] and cooldown == 0:
            if keys[pygame.K_a]:
                self.x -= 100 * self.speed
            if keys[pygame.K_d]:
                self.x += 100 * self.speed
            if keys[pygame.K_w]:
                self.y -= 100 * self.speed
            if keys[pygame.K_s]:
                self.y += 100 * self.speed
            cooldown = cooldowned
            
        if cooldown > 0:
            cooldown -= 1

        if cooldown == 0:
            self.speed = self.speed

        # Giới hạn trái phải trên dưới
        self.x = max(0, min(self.x, screen_width - self.width))
        self.y = max(0, min(self.y, screen_height - self.height))

    def ngang(self):
        # Di chuyển theo chiều ngang và kiểm tra nếu nhân vật đã chạm đến biên
        self.x += self.direction_x * self.speed
        if self.x <= 0 or self.x >= screen_width - 200:
            # Thay đổi hướng ngang nếu chạm biên
            self.direction_x *= -1
        # Đảm bảo nhân vật ở trong giới hạn màn hình
        self.x = max(0, min(self.x, screen_width - 200))

    def cheo(self):
        # Di chuyển theo chiều dọc và kiểm tra nếu nhân vật đã chạm đến biên
        self.y += self.direction_y * self.speed

        # Thay đổi hướng dọc nếu chạm biên
        if self.y <= 50 or self.y >= screen_height - 500:
            self.direction_y *= -1

        # Di chuyển theo chiều ngang và kiểm tra nếu nhân vật đã chạm đến biên
        self.x += self.direction_x * self.speed
        if self.x <= 50 or self.x >= screen_width - 50:
            # Thay đổi hướng ngang nếu chạm biên
            self.direction_x *= -1

        # Đảm bảo nhân vật ở trong giới hạn màn hình
        self.x = max(0, min(self.x, screen_width - 50))
        self.y = max(0, min(self.y, screen_height - 50))



# NGƯỜI CHƠI
player = Character(3, 1, 50, 50, playerImg)
# player_sprites = pygame.sprite.Group()
# player_sprites.add(player)
player_lives = 3

# Vị trí người chơi
player.x = 380
player.y = 500

# Hàm bắn đạn của người chơi
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+2, y + 5))

# Đạn
bullet_y_change = 15
enemy_bullet_y_change = 1.5
bullet_cooldown = 0
enemy_bullet_cooldown = 0
bullet_x = 0
bullet_state = "ready"
bullet_speed = 2

class Bullet:
    def __init__(self, x, y, x_change, y_change, width, height, image):
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change
        self.width = width
        self.height = height
        self.image = image

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def fire_multiple_bullets(player, bullets, bullet_image):
    global bullet_state
    bullet_state = "fire"
    bullet_x = player.x + player.width // 2 - bullet_image.get_width() // 2
    bullet_y = player.y
    new_bullet1 = Bullet(bullet_x, bullet_y, 1, -2, bullet_image.get_width(), bullet_image.get_height(), bullet_image)
    new_bullet2 = Bullet(bullet_x, bullet_y, 0, -2, bullet_image.get_width(), bullet_image.get_height(), bullet_image)
    new_bullet3 = Bullet(bullet_x, bullet_y, -1, -2, bullet_image.get_width(), bullet_image.get_height(), bullet_image)
    bullets.append(new_bullet1)
    bullets.append(new_bullet2)
    bullets.append(new_bullet3)

player_bullets = []

# KẺ ĐỊCH
enemy = Character(1, 1, 64, 64, enemyImg)
# enemy_sprites = pygame.sprite.Group()
# enemy_sprites.add(enemy)

# BOSS
boss = Character(5, 0.5, 180, 150, boss1Img)

# Vị trí kẻ địch
enemy.x = 400
enemy.y = 50
boss.x = 400
boss.y = 50
# danh sách đạn của kẻ địch
enemy_bullets = []

# Hàm bắn đạn của kẻ địch
def enemy_fire_bullet(x, y):
    enemy_bullets.append([x + 3, y + 50])

# Hàm bắn đạn của Boss
def boss_fire_bullet(x, y):
    enemy_bullets.append([x + 40, y + 100])
    enemy_bullets.append([x + 85, y + 100])
    enemy_bullets.append([x + 130, y + 100])

# Hàm kiểm tra va chạm giữa người chơi và đạn của kẻ địch
def is_player_hit(player_x, player_y, enemy_bullet_x, enemy_bullet_y):
    distance = ((player_x - enemy_bullet_x)**2 + (player_y - enemy_bullet_y)**2) ** 0.5
    return distance < 27

# Hàm kiểm tra va chạm giữa đạn của người chơi và kẻ địch
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)**0.5
    return distance < 27

# Hàm kiểm tra va chạm giữa đạn của người chơi và boss
def is_boss_hit(boss_x, boss_y, bullet_x, bullet_y):
    # Kiểm tra xem đạn có nằm trong hình chữ nhật bao quanh phần thân của boss không
    boss_rect = pygame.Rect(boss_x, boss_y, boss.width, boss.height)
    bullet_rect = pygame.Rect(bullet_x, bullet_y, bulletImg.get_width(), bulletImg.get_height())
    return boss_rect.colliderect(bullet_rect)

# Hàm kiểm tra va chạm giữa người chơi và kẻ địch
def player_hit(enemy_x, enemy_y, player_x, player_y):
    distance = ((enemy_x - player_x)**2 + (enemy_y - player_y)**2) ** 0.5
    return distance < 27

buffArray = ['moreSpeed', 'moreBullet', 'moreLife']

class Buff:
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.image = pygame.image.load(f'img/{type}.png')  # Đảm bảo có hình ảnh cho mỗi loại buff
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.speed = 0.5

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def drop(self):
        self.y += self.speed

def dropBuff(x, y):
    # if(buffArray.count > 0):
    buff_type = random.choice(buffArray)
    new_buff = Buff(buff_type, random.randint(100, screen_width - 100), y)
    # buffArray.remove(buff_type)
    return new_buff

# Danh sách để lưu các buff hiện tại
active_buffs = []

# Hàm vẽ số mạng của người chơi
def draw_lives(x, y, lives):
    for i in range(lives):
        heart_x = x + i * (heartImg.get_width() + 5)
        screen.blit(heartImg, (heart_x, y))

def draw_hp_boss(bossHP):
    font = pygame.font.SysFont(None, 20)
    text = font.render("BOSS", True, red)
    screen.blit(text, (screen_width / 2 - text.get_width() / 2, 0))
    for i in range(bossHP):
        heart_x = 330 + i * (heartImg.get_width() + 5)
        screen.blit(heartImg, (heart_x, 10))

# Hàm vẽ tính điểm
score = 4
def draw_score(x, y, score):
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Scores: {score}", True, white)
    screen.blit(text, (x - 20, y))

def draw_dash(x, y, cooldown):
    # Trong phần khai báo
    font = pygame.font.SysFont(None, 24)  # Chọn font và kích thước văn bản
    cooldown_text = font.render(f"Dash: {cooldown}", True, white)  # Cập nhật văn bản với giá trị cooldown hiện tại
    screen.blit(cooldown_text, (x, y))

# Nhac nen
soundBG.play()

# Hàm lưu game
def save_game(state):
    with open('inforPlayer/' + player_name + '.pkl', 'wb') as f:
        pickle.dump(state, f)

# Hàm tải game
def load_game(player_name):
    try:
        with open('inforPlayer/' + player_name + '.pkl', 'rb') as f:
            while True:
                try:
                    game_state = pickle.load(f)
                    if game_state.get('player_name') == player_name:
                        return game_state
                except EOFError:
                    break
    except FileNotFoundError:
        return None
    return None

# Hàm khởi tạo lại trò chơi với trạng thái đã lưu
def reset_game(state):
    global player, player_lives, enemy, boss, enemy_bullets, bullet_y, bullet_state, score, game_over, enemy_lives, boss_lives
    player.x, player.y = state['player_x'], state['player_y']
    player_lives = state['player_lives']
    enemy.x, enemy.y = state['enemy_x'], state['enemy_y']
    boss.x, boss.y = state['boss_x'], state['boss_y']
    enemy_bullets = state['enemy_bullets']
    bullet_y = state['bullet_y']
    bullet_state = state['bullet_state']
    score = state['score']
    game_over = state['game_over']
    enemy_lives = state['enemy_lives']
    boss_lives = state['boss_lives']
    enemy.hp = state['enemy_hp']
    boss.hp = state['boss_hp']

last_bullet_time = pygame.time.get_ticks()
bullet_interval = 1000  # Thời gian giữa các lần bắn (mili giây)

# Tải trạng thái trò chơi đã lưu nếu có
saved_state = load_game(player_name)
if saved_state:
    reset_game(saved_state)

while running:
    screen.fill(black)

    # Di chuyển hình nền
    bg_y1 += scroll_speed
    bg_y2 += scroll_speed

    # Reset vị trí khi hình nền đi ra khỏi màn hình
    if bg_y1 >= screen_height:
        bg_y1 = -background_height
    if bg_y2 >= screen_height:
        bg_y2 = -background_height

    # Vẽ hình nền
    screen.blit(background, (0, bg_y1))
    screen.blit(background, (0, bg_y2))

    # draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                # Lưu trạng thái trò chơi
                state = {
                    'player_x': player.x,
                    'player_y': player.y,
                    'player_lives': player_lives,
                    'enemy_x': enemy.x,
                    'enemy_y': enemy.y,
                    'boss_x': boss.x,
                    'boss_y': boss.y,
                    'enemy_bullets': enemy_bullets,
                    'bullet_y': bullet_y,
                    'bullet_state': bullet_state,
                    'score': score,
                    'game_over': game_over,
                    'enemy_lives': enemy_lives,
                    'boss_lives': boss_lives,
                    'enemy_hp': enemy.hp,
                    'boss_hp': boss.hp,
                    'player_name': player_name
                }
                save_game(state)
                print("Game saved!")
                
    # chonam
    if moreBullet == True:
    # Tự động bắn đạn của người chơi
        current_time = pygame.time.get_ticks()
        if current_time - last_bullet_time > bullet_interval:
            fire_multiple_bullets(player, player_bullets, OnebulletImg)
            last_bullet_time = current_time

        for bullet in player_bullets:
            bullet.y += bullet.y_change
            screen.blit(bullet.image, (bullet.x-15, bullet.y))
            if bullet.y < 0:
                player_bullets.remove(bullet)
    
    if player.hp <= 0:
        game_over = True

    # bắn đạn tự động của người chơi
    if moreBullet == False:
        bullet_cooldown -= 1
        if bullet_cooldown <= 0 and bullet_state == "ready":
            soundBulletHit.play()
            bullet_x = player.x
            bullet_y = player.y
            fire_bullet(bullet_x, bullet_y)
            bullet_cooldown = 60

        # Di chuyển đạn của người chơi
        if bullet_y <= 0:
            bullet_y = player.y
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bullet_x, bullet_y)
            bullet_y -= bullet_y_change

    # Bắn đạn của kẻ địch
    enemy_bullet_cooldown -= 1
    if enemy_bullet_cooldown <= 0 and enemy_lives:
        enemy_fire_bullet(enemy.x, enemy.y)
        enemy_bullet_cooldown = 60
    
    if enemy_bullet_cooldown <= 0 and boss_lives:
        boss_fire_bullet(boss.x, boss.y)
        enemy_bullet_cooldown = 60
    
    for bullet in enemy_bullets:
        screen.blit(enemy_bulletImg, (bullet[0], bullet[1]))
        bullet[1] += enemy_bullet_y_change
        if bullet[1] >= screen_height:
            enemy_bullets.remove(bullet)
        if is_player_hit(player.x, player.y, bullet[0], bullet[1]):
            player_lives -= 1
            enemy_bullets.remove(bullet)
            if player_lives <= 0:
                game_over = True
            else:
                player.x = 370
                player.y = 480

    player.move()

    for buff in active_buffs:
        buff.drop()  # Cập nhật vị trí của buff (rơi xuống)
        buff.draw()
        if is_collision(buff.x, buff.y, player.x, player.y):
            soundTakeBuff.play()
            if buff.type == 'moreSpeed':
                player.speed += 0.5
            elif buff.type == 'moreBullet':
                moreBullet = True
            elif buff.type == 'moreLife':
                player_lives +=1
            active_buffs.remove(buff)
        elif buff.y > screen_height:  # Xóa buff nếu rơi khỏi màn hình
            active_buffs.remove(buff)

    # nghia
    if moreBullet == False:
        if is_collision(enemy.x, enemy.y, bullet_x, bullet_y) and not boss_lives:
            bullet_y = player.y
            bullet_state = "ready"
            enemy.hp -= 1
            if enemy.hp <= 0:

                buff = dropBuff(enemy.x, enemy.y)
                if buff:
                    active_buffs.append(buff)

                score += 1
                if score == 5:
                    soundAppearBoss.play()
                    boss.hp = 5
                    boss_lives = True
                    enemy_lives = False
                else:
                    enemy.x = random.randint(100, screen_width - 100)
                    enemy.y = random.randint(60, 100)
                    enemy.hp = 1

        if is_boss_hit(boss.x, boss.y, bullet_x, bullet_y) and boss_lives:
            soundBulletHit.play()
            bullet_y = player.y
            bullet_state = "ready"
            boss.hp -= 1
            if boss.hp <= 0:
                soundBossKill.play()
                score += 5
                boss_lives = False
                enemy_lives = True
                enemy.x = random.randint(100, screen_width - 100)
                enemy.y = random.randint(60, 100)
                enemy.hp = 1
            
    # chonam
    if moreBullet == True:
        for bullet in player_bullets:
            bullet.y += bullet.y_change
            bullet.x += bullet.x_change
            # screen.blit(bullet.image, (bullet.x, bullet.y))

            if is_collision(enemy.x, enemy.y, bullet.x, bullet.y) and not boss_lives:
                bullet.y = player.y
                bullet_state = "ready"
                enemy.hp -= 1
                if enemy.hp <= 0:

                    buff = dropBuff(enemy.x, enemy.y)
                    if buff:
                        active_buffs.append(buff)

                    score += 1
                    if score == 5:
                        # soundAppearBoss.play()
                        boss.hp = 5
                        boss_lives = True
                        enemy_lives = False
                    else:
                        enemy.x = random.randint(100, screen_width - 100)
                        enemy.y = random.randint(60, 100)
                        enemy.hp = 1
                    player_bullets.remove(bullet)

            if is_boss_hit(boss.x, boss.y, bullet.x, bullet.y) and boss_lives:
                soundBulletHit.play()
                bullet.y = player.y
                bullet_state = "ready"
                boss.hp -= 1
                if boss.hp <= 0:
                    # soundBossKill.play()
                    score += 5
                    boss_lives = False
                    enemy_lives = True
                    enemy.x = random.randint(100, screen_width - 100)
                    enemy.y = random.randint(60, 100)
                    enemy.hp = 1
                player_bullets.remove(bullet)

        # Kiểm tra va chạm giữa đạn của người chơi và kẻ địch
        # if is_collision(enemy.x, enemy.y, bullet.x, bullet.y) and not boss_lives:
        #     bullet_state = "ready"
        #     enemy.hp -= 1
        #     player_bullets.remove(bullet)
        #     if enemy.hp <= 0:
        #         score += 1
        #         if score == 5:
        #             soundAppearBoss.play()
        #             boss.hp = 5
        #             boss_lives = True
        #             enemy_lives = False
        #         else:
        #             enemy.x = random.randint(100, screen_width - 100)
        #             enemy.y = random.randint(60, 100)
        #             enemy.hp = 1

        # # Kiểm tra va chạm giữa đạn của người chơi và boss
        # if is_boss_hit(boss.x, boss.y, bullet.x, bullet.y) and boss_lives:
        #     soundBulletHit.play()
        #     bullet_state = "ready"
        #     boss.hp -= 1
        #     if boss.hp <= 0:
        #         buff = dropBuff(enemy.x, enemy.y)
        #         if buff:
        #             active_buffs.append(buff)
        #         soundBossKill.play()
        #         score += 5
        #         boss_lives = False
        #         enemy_lives = True
        #         enemy.x = random.randint(100, screen_width - 100)
        #         enemy.y = random.randint(60, 100)
        #         enemy.hp = 1

    if player_hit(enemy.x, enemy.y, player.x, player.y):
        player_lives -= 1
        if player_lives <= 0:
            game_over = True
            enemy_lives = False
        else:
            player.x = 370
            player.y = 480

    if player_hit(boss.x, boss.y, player.x, player.y):
        player_lives -= 1
        if player_lives <= 0:
            game_over = True
            boss_lives = False
        else:
            player.x = 370
            player.y = 480

    if score == 5 and boss_lives:
        screen.blit(boss.image, (boss.x, boss.y), (0, 0, boss.width, boss.height))
        draw_hp_boss(boss.hp)
        boss.ngang()
    else:
        enemy.cheo()
        screen.blit(enemy.image, (enemy.x-20, enemy.y), (0, 0, enemy.width, enemy.height))
        # enemy_sprites.draw(screen)
        # enemy_sprites.update()

    # Vẽ player
    screen.blit(player.image, (player.x-15, player.y-10), (0, 0, player.width, player.height))

    draw_lives(10, 10, player_lives)
    draw_score(700, 10, score)
    draw_dash(10, 40, cooldown)
    scoreNow = score
    
    if game_over:
        # screen.fill(black)
        soundGameOver.play()
        font = pygame.font.SysFont(None, 64)
        text = font.render("Game Over", True, red)
        screen.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.wait(5000)
        break

    # Update the display
    pygame.display.update()
    clock.tick(60)
pygame.quit()