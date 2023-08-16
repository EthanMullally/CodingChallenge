import pgzrun
import random

WIDTH = 600
HEIGHT = 400
score = 0
lives = 10

fox = Actor("player")
fox.pos= 400,200

coin = Actor("coin")
coin.pos = 500,100 
def draw():
  global game_over
  global score
  if not game_over:
    screen.fill("green")
    screen.draw.text("Score:" + str(score), topleft=(20,20))
    player.draw()
    coin.draw()
  else:
    screen.draw.text("Game Over! Press R to restart", color="white", topleft=(20,20))
def place_coin():
  global coin
  global WIDTH
  global HEIGHT
  coin.pos = random.randint((WIDTH, HEIGHT))
  
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
  if lives == 0:
    game_over = True
  if not game_over:
    fox_speed = 20
    if keyboard.a:
      player.y = player.y+fox_speed
    if keyboard.d:
      player.x = player.x-fox_speed
  else:
    if keyboard.r:
      game_over = False
      fox.pos = random.randint((WIDTH, HEIGHT))
