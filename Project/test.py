import pygame
import random

pygame.init()

# Kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Bắn UFO")

clock = pygame.time.Clock()

# Tải hình ảnh
playerImg = pygame.image.load('img/player.png')
playerImg = pygame.transform.scale(playerImg, (50, 50))

enemyImg = pygame.image.load('img/enemy.png')
enemyImg = pygame.transform.scale(enemyImg, (64, 64))

bulletImg = pygame.image.load('img/bullets_enemy.png')
bulletImg = pygame.transform.scale(bulletImg, (16, 16))

boss1Img = pygame.image.load('img/boss2.png')
boss1Img = pygame.transform.scale(boss1Img, (180, 150))

enemy_bulletImg = pygame.image.load('img/bullet.png')
enemy_bulletImg = pygame.transform.scale(enemy_bulletImg, (16, 16))

heartImg = pygame.image.load('img/heart.png')
heartImg = pygame.transform.scale(heartImg, (25, 25))

# Tải âm thanh
soundBG = pygame.mixer.Sound("sound/bg-battle-march-action-loop-6935.mp3")
soundBulletHit = pygame.mixer.Sound("sound/bullet-hit-080997_bullet-39735.mp3")
soundGameOver = pygame.mixer.Sound("sound/game-over-galaxy-brain-meme.mp3")

# Định nghĩa màu
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

cooldown = 0
cooldowned = 100

class Character:
    def __init__(self, hp, speed, width, height, image):
        self.hp = hp
        self.speed = speed
        self.width = width
        self.height = height
        self.image = image
        self.direction_x = 1  # Hướng mặc định là sang phải
        self.direction_y = 1

        self.x = screen_width // 2 - self.width // 2  # Căn giữa người chơi theo chiều ngang
        self.y = screen_height // 2 - self.height // 2  # Căn giữa người chơi theo chiều dọc
    
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

# KẺ ĐỊCH
enemy = Character(1, 1, 64, 64, enemyImg)

# BOSS
boss = Character(5, 1, 180, 150, boss1Img)

# Vị trí kẻ địch
enemy.x = 400
enemy.y = 50

# danh sách đạn của kẻ địch
enemy_bullets = []

# Hàm bắn đạn của kẻ địch
def enemy_fire_bullet(x, y):
    enemy_bullets.append([x + 3, y + 50])

# Hàm bắn đạn của Boss
def boss_fire_bullet(x, y):
    enemy_bullets.append([x - 80, y + 60])
    enemy_bullets.append([x - 40, y + 60])
    enemy_bullets.append([x, y + 60])

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

# Hàm vẽ số mạng của người chơi
def draw_lives(x, y, lives):
    for i in range(lives):
        heart_x = x + i * (heartImg.get_width() + 5)
        screen.blit(heartImg, (heart_x, y))

# Hàm vẽ tính điểm
score = 0
def draw_score(x, y, score):
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Scores: {score}", True, white)
    screen.blit(text, (x - 20, y))

def draw_dash(x, y, cooldown):
    # Trong phần khai báo
    font = pygame.font.SysFont(None, 24)  # Chọn font và kích thước văn bản
    cooldown_text = font.render(f"Dash: {cooldown}", True, white)  # Cập nhật văn bản với giá trị cooldown hiện tại
    screen.blit(cooldown_text, (x, y))

enemy_lives = True
boss_lives = False
game_over = False
running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # bắn đạn tự động của người chơi
    bullet_cooldown -= 1
    if bullet_cooldown <= 0 and bullet_state == "ready":
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
    
    if is_collision(enemy.x, enemy.y, bullet_x, bullet_y) and not boss_lives:
        soundBulletHit.play()
        bullet_y = player.y
        bullet_state = "ready"
        enemy.hp -= 1
        if enemy.hp <= 0:
            score += 1
            if score == 10:
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
            score += 1
            boss_lives = False
            enemy_lives = True
            enemy.x = random.randint(100, screen_width - 100)
            enemy.y = random.randint(60, 100)
            enemy.hp = 1

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

    if score == 10 and boss_lives:
        screen.blit(boss.image, (boss.x, boss.y), (0, 0, boss.width, boss.height))
        boss.cheo()
    else:
        enemy.cheo()
        screen.blit(enemy.image, (enemy.x-20, enemy.y), (0, 0, enemy.width, enemy.height))

    # Vẽ player
    screen.blit(player.image, (player.x-15, player.y-10), (0, 0, player.width, player.height))

    draw_lives(10, 10, player_lives)
    draw_score(700, 10, score)
    draw_dash(10, 40, cooldown)
    
    if game_over:
        soundGameOver.play()
        font = pygame.font.SysFont(None, 64)
        text = font.render("Game Over", True, red)
        screen.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.wait(4000)
        break

    # Update the display
    pygame.display.update()
    clock.tick(60)

pygame.quit()