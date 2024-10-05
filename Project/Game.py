import pygame
import random

pygame.init()

# Kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Bắn UFO")

# khai báo biến màu sắc
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()

# Tải hình ảnh
playerImg = pygame.image.load('img/player.png')
playerImg = pygame.transform.scale(playerImg, (64, 64))

enemyImg = pygame.image.load('img/enemy.png')
enemyImg = pygame.transform.scale(enemyImg, (64, 64))

bulletImg = pygame.image.load('img/bullets_enemy.png')
bulletImg = pygame.transform.scale(bulletImg, (16, 16))

enemy_bulletImg = pygame.image.load('img/bullet.png')
enemy_bulletImg = pygame.transform.scale(enemy_bulletImg, (16, 16))

foodImg = pygame.image.load('img/food.png')
foodImg = pygame.transform.scale(foodImg, (16, 16))

# Vị trí ban đầu của người chơi
player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0

# khai báo biến tính điểm
core = 0

# Vị trí ban đầu của kẻ địch
enemy_x = random.randint(0, screen_width - 64)
enemy_y = random.randint(50, 150)
enemy_x_change = 0.3
enemy_y_change = 40
enemy_hp = 3

# Vị trí của food
food_x = random.randint(0, screen_width - 16)
food_y = random.randint(50, 150)
food_x_change = 0
food_y_change = 1

# Vị trí ban đầu của đạn
bullet_x = player_x
bullet_y = player_y
bullet_x_change = 0
bullet_y_change = -4
bullet_state = "ready"

# danh sách đạn của kẻ địch
enemy_bullets = []

# Hàm kiểm tra va chạm giữa đạn của kẻ địch và người chơi được tính theo cong thức Euclid 
def is_enemy_collision(player_x, player_y, enemy_bullet_x, enemy_bullet_y):
    distance = ((player_x - enemy_bullet_x)**2 + (player_y - enemy_bullet_y)**2) ** 0.5
    return distance < 27

# Hàm bắn đạn của kẻ địch
def enemy_fire_bullet(x, y):
    enemy_bullets.append([x + 16, y + 10])

# tốc độ đạn
bullet_y_change = 15
enemy_bullet_y_change = 0.5
enemy_bullet_cooldown = 0
bullet_cooldown = 0

game_over = False

# Số mạng của người chơi
player_lives = 3

# Hàm vẽ số mạng của người chơi
def draw_lives(x, y, lives):
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Mang: {lives}", True, red)
    screen.blit(text, (x, y))

# Hàm vẽ tính điểm
def draw_core(x, y, core):
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Core: {core}", True, white)
    screen.blit(text, (x, y))

# Hàm kiểm tra va chạm giữa người chơi và UFO
def player_hit(enemy_x, enemy_y, player_x, player_y):
    distance = ((enemy_x - player_x)**2 + (enemy_y - player_y)**2) ** 0.5
    return distance < 27

# Hàm bắn đạn của người chơi
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Hàm kiểm tra va chạm
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2) ** 0.5
    return distance < 27

# Hàm vẽ người chơi
def player(x, y):
    screen.blit(playerImg, (x, y))

# Hàm vẽ kẻ địch
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def food(x, y):
    screen.blit(foodImg, (x, y))

# Hàm kiểm tra va chạm giữa người chơi và food
def is_food_collision(player_x, player_y, food_x, food_y):
    distance = ((player_x - food_x)**2 + (player_y - food_y)**2) ** 0.5
    return distance < 27

# Hàm kiểm tra va chạm giữa người chơi và đạn của kẻ địch
def is_player_hit(player_x, player_y, enemy_bullet_x, enemy_bullet_y):
    distance = ((player_x - enemy_bullet_x)**2 + (player_y - enemy_bullet_y)**2) ** 0.5
    return distance < 27

running = True

# Xử lý game
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Điều khiển người chơi
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_x_change = -2
            if event.key == pygame.K_d:
                player_x_change = 2
            if event.key == pygame.K_w:
                player_y_change = -2
            if event.key == pygame.K_s:
                player_y_change = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player_x_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player_y_change = 0

    # bắn đạn tự động của người chơi
    bullet_cooldown -= 1
    if bullet_cooldown <= 0:
        bullet_x = player_x
        fire_bullet(bullet_x, bullet_y)
        bullet_y = player_y
        bullet_state = "fire"
        bullet_cooldown = 60

    # Cập nhật vị trí người chơi
    player_x += player_x_change
    player_y += player_y_change

    # Giới hạn người chơi trong màn hình
    if player_x <= 0:
        player_x = 0
    elif player_x >= screen_width - 64:
        player_x = screen_width - 64
    if player_y <= 0:
        player_y = 0
    elif player_y >= screen_height - 64:
        player_y = screen_height - 64

    # Di chuyển kẻ địch
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 0.3
        enemy_y += enemy_y_change
    elif enemy_x >= screen_width - 64:
        enemy_x_change = -0.3
        enemy_y += enemy_y_change
        
    # Di chuyển food nếu điểm là 2
    if core == 5:
        food_x += food_x_change
        food_y += food_y_change
        if food_y > screen_height:
            food_x = random.randint(0, screen_width - 16)
            food_y = random.randint(50, 150)

    # Di chuyển đạn của người chơi
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Bắn đạn của kẻ địch tự động
    enemy_bullet_cooldown -= 1
    if enemy_bullet_cooldown <= 0:
        enemy_fire_bullet(enemy_x, enemy_y)
        enemy_bullet_cooldown = 60 

    # Cập nhật vị trí đạn của kẻ địch và kiểm tra va chạm
    for bullet in enemy_bullets:
        screen.blit(enemy_bulletImg, (bullet[0], bullet[1]))
        bullet[1] += enemy_bullet_y_change
        if bullet[1] >= screen_height:
            enemy_bullets.remove(bullet)
        if is_player_hit(player_x, player_y, bullet[0], bullet[1]):
            player_lives -= 1
            enemy_bullets.remove(bullet)
            if player_lives <= 0:
                game_over = True
            else:
                player_x = 370
                player_y = 480

    # Kiểm tra va chạm giữa đạn người chơi và kẻ địch
    collision = is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = player_y
        bullet_state = "ready"
        enemy_hp -= 1
        if enemy_hp <= 0:
            enemy_x = random.randint(0, screen_width - 64)
            enemy_y = random.randint(50, 150)
            enemy_hp = 3
            enemy_x_change = enemy_x_change + 0.5
            core = core + 1

    # Kiểm tra va chạm giữa người chơi và kẻ địch
    if player_hit(enemy_x, enemy_y, player_x, player_y):
        player_lives -= 1
        if player_lives <= 0:
            game_over = True
        else:
            player_x = 370
            player_y = 480

    # Kiểm tra va chạm giữa người chơi và food
    if core == 5 and is_food_collision(player_x, player_y, food_x, food_y):
        bullet_y_change += 5  # Increase bullet speed

    # Vẽ các phần tử
    screen.blit(playerImg, (player_x, player_y))
    screen.blit(enemyImg, (enemy_x, enemy_y))
    
    if core == 5:
        food(food_x, food_y)
    
    draw_lives(10, 10, player_lives)
    draw_core(700, 10, core)

    if game_over:
        font = pygame.font.SysFont(None, 64)
        text = font.render("Bạn Đã Thua", True, red)
        screen.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.wait(4000)
        break

    pygame.display.update()
    clock.tick(60)

pygame.quit()
