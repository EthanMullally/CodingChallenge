import pgzrun
import random

WIDTH = 600
HEIGHT = 400
score = 0
lives = 10

fox = Actor("player")
fox.pos= 400,200

coin = Actor("coin")
coin.pos = random.randint(WIDTH, HEIGHT)

enemy = Actor("enemy")
enemy.pos = random.randint(WIDTH, HEIGHT)
def draw():
  global game_over
  global score
  if not game_over:
    screen.fill("green")
    screen.draw.text("Score: " + str(score) + "/Lives: " + str(lives), color="white", topleft=(20,20))
    player.draw()
    coin.draw()
    enemy.draw()
  else:
    screen.draw.text("Game Over! Press R to restart", color="white", topleft=(20,20))
    player.draw()
def place_coin():
  global coin
  global WIDTH
  global HEIGHT
  coin.x = random.randint(WIDTH, HEIGHT)
  
def update():
  global player_speed
  global score 
  global game_over
  global lives
  global fox
  coin_hit = player.colliderect(coin)
  if coin_hit:
    score+=1
    place_coin()
  if not game_over:
    fox_speed = 20
    if keyboard.a:
      player.y = player.y+fox_speed
    if keyboard.d:
      player.x = player.x-fox_speed
    player_hit_enemy = fox.colliderect(enemy)
    if player_hit_enemy:
      if lives > 0:
        lives = lives-1
      else:
        game_over = True
    def move_enemy():
      if random.choice([True, False]):
        random_move = random.randint(1,2)
        if random_move == 1:
          enemy.x = enemy.x+20
        else:
          enemy.x = enemy.x-20
      else:
        move_enemy()
  else:
    fox.x = fox.x-400
    if keyboard.r:
      game_over = False
      fox.pos = random.randint(WIDTH, HEIGHT)
  move_enemy()
pgzrun.go()
