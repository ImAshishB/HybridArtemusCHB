# import pygame
# import time
# import random
#
# # Initialize pygame
# pygame.init()
#
# # Define colors
# black = (0, 0, 0)
# red = (255, 0, 0)
# grey = (169, 169, 169)
#
# # Set display dimensions
# dis_width = 800
# dis_height = 600
#
# # Set display
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Snake Game')
#
# # Define the snake
# snake_block = 20
# snake_speed = 15
#
# # Set clock
# clock = pygame.time.Clock()
#
# # Define font
# font_style = pygame.font.SysFont(None, 50)
# score_font = pygame.font.SysFont(None, 35)
#
# # Function to display score
# def Your_score(score):
#     value = score_font.render("Your Score: " + str(score), True, black)
#     dis.blit(value, [0, 0])
#
# # Function to draw the snake
# def our_snake(snake_block, snake_List):
#     for x in snake_List:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
#
# # Function to display message
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])
#
# # Main game loop
# def gameLoop():
#     game_over = False
#     game_close = False
#
#     x1 = dis_width / 2
#     y1 = dis_height / 2
#
#     x1_change = 0
#     y1_change = 0
#
#     snake_List = []
#     Length_of_snake = 1
#
#     # Generate food position
#     foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
#     foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
#
#     while not game_over:
#
#         while game_close:
#             dis.fill(grey)
#             message("You Lost! Press Q-Quit or C-Play Again", red)
#             Your_score(Length_of_snake - 1)
#             pygame.display.update()
#
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
#
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(grey)
#         pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
#         snake_Head = []
#         snake_Head.append(x1)
#         snake_Head.append(y1)
#         snake_List.append(snake_Head)
#         if len(snake_List) > Length_of_snake:
#             del snake_List[0]
#
#         for x in snake_List[:-1]:
#             if x == snake_Head:
#                 game_close = True
#
#         our_snake(snake_block, snake_List)
#         Your_score(Length_of_snake - 1)
#
#         pygame.display.update()
#
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
#             foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
#             Length_of_snake += 1
#
#         clock.tick(snake_speed)
#
#     pygame.quit()
#     quit()
#
# # Run the game
# gameLoop()






















































import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set display dimensions
dis_width = 800
dis_height = 600

# Set display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Car Racing Game')

# Load car image
car_width = 50
car_height = 100

# Set car speed
car_speed = 15

# Set clock
clock = pygame.time.Clock()

# Load car image
car_img = pygame.Surface((car_width, car_height))
car_img.fill(red)

# Function to display obstacles
def draw_obstacle(obst_x, obst_y, obst_w, obst_h, color):
    pygame.draw.rect(dis, color, [obst_x, obst_y, obst_w, obst_h])

# Function to display car
def car(x, y):
    dis.blit(car_img, (x, y))

# Function to display message
def message(msg, color):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial car position
    x = dis_width * 0.45
    y = dis_height * 0.8

    x_change = 0

    # Obstacle properties
    obst_x = random.randrange(200, dis_width - 200)
    obst_y = -600
    obst_speed = 7
    obst_width = 100
    obst_height = 100

    while not game_over:

        while game_close:
            dis.fill(green)
            message("You Crashed! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -car_speed
                if event.key == pygame.K_RIGHT:
                    x_change = car_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        dis.fill(green)

        # Draw the road
        pygame.draw.rect(dis, black, [150, 0, dis_width - 300, dis_height])

        # Draw the obstacle
        draw_obstacle(obst_x, obst_y, obst_width, obst_height, black)
        obst_y += obst_speed

        # Draw the car
        car(x, y)

        if x > dis_width - 150 - car_width or x < 150:
            game_close = True

        if obst_y > dis_height:
            obst_y = 0 - obst_height
            obst_x = random.randrange(200, dis_width - 200)

        if y < obst_y + obst_height:
            if x > obst_x and x < obst_x + obst_width or x + car_width > obst_x and x + car_width < obst_x + obst_width:
                game_close = True

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

# Run the game
gameLoop()
