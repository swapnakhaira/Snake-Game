# import pygame
#
# def draw_block():
#     surface.fill((52, 235, 195))
#     surface.blit(block, (block_x, block_y))
#     pygame.display.flip()
#
#
# if __name__ == "__main__":
#     pygame.init()
#
#     surface = pygame.display.set_mode((1000,500))
#     surface.fill((96, 245, 66))
#
#     block = pygame.image.load("resources/block.png").convert()
#     block_x = 100
#     block_y = 100
#     surface.blit(block, (block_x,block_y))
#
#     pygame.display.flip()
#
#     running = True
#
#     while running:
#         for event in pygame.event.get():
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     running = False
#
#                 if event.key == K_UP:
#                     block_y = block_y - 10
#                     draw_block()
#                 if event.key == K_DOWN:
#                     block_y = block_y + 10
#                     draw_block()
#                 if event.key == K_LEFT:
#                     block_x = block_x - 10
#                     draw_block()
#                 if event.key == K_RIGHT:
#                     block_x == block_x + 10
#                     draw_block()
#
#             elif event.type == QUIT:
#                 running = False


import pygame
pygame.init()

# Creating a window
gameWindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("My Firt Game")

# Game Specific Variables
exit_game = False
game_over = False

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.K_DOWN:
            if event.type == pygame.K_RIGHT:
                print("you have pressed the right key")


pygame.quit()
quit()