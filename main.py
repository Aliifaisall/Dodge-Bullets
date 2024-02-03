#
# Author : Ali Maskari
# Date : 3/02/2024
# Refrecne :https://devdocs.io/pygame/
#
# ----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
import pygame
import time
import random
pygame.font.init()
# width and height of the game window
width, height = 900, 700
# the window variable
window = pygame.display.set_mode((width, height))
# name at top of the window
pygame.display.set_caption("Space Game")

backgtound = pygame.transform.scale(pygame.image.load("Space_game_BG.jpeg"), (width, height))

# player charecter
player_width = 40
player_height = 60
player_vel = 5
# bullet charecter
bullet_width = 10
bullet_height = 50
bullet_vel = 2

# time font
font = pygame.font.SysFont("bold", 30)


def draw(player, elapsed_time, bullets):
    window.blit(backgtound, (0, 0))
    time_text = font.render(f"Time: {round(elapsed_time)}s", 1, "white")
    window.blit(time_text, (10, 10))
    pygame.draw.rect(window, "blue", player)
    for bullet in bullets:
        pygame.draw.rect(window, "red", bullet)

    pygame.display.update()


# main game loop
def main():
    run = True
    player = pygame.Rect(200, height - player_height, player_width, player_height)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    # shooting bullets object
    bullet_add_increment = 2000
    bullet_count = 0
    bullets = []
    hit = False

    while run:
        # This method should be called once per frame. It will compute how many milliseconds have passed since the previous call.
        bullet_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if bullet_count > bullet_add_increment:
            for _ in range(3):
                bullet_x = random.randint(0, width - bullet_width)
                bullet = pygame.Rect(bullet_x, -bullet_height, bullet_width, bullet_height)
                bullets.append(bullet)
            bullet_add_increment = max(200, bullet_add_increment - 50)
            bullet_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # moving player logic
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x - player_vel >= 0:
            player.x -= player_vel
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x + player_vel + player.width <= width:
            player.x += player_vel

        # shooting bullets logic
        for bullet in bullets[:]:
            bullet.y += bullet_vel
            if bullet.y > height:
                bullets.remove(bullet)
            elif bullet.y + bullet.height >= player.y and bullet.colliderect(player):
                bullets.remove(bullet)
                hit = True
                break

        if hit:
            lost_text = font.render("YOU LOST BITCH 00100", 1, "white")
            window.blit(lost_text, (width/2 - lost_text.get_width()/2, height/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(5000)
            break

        draw(player, elapsed_time, bullets)
    pygame.quit()


if __name__ == "__main__":
    main()
