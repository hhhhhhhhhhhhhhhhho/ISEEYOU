import pygame
import ctypes

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

radius = 40


def writeText(screen, x, y):
    font = pygame.font.SysFont("arial", 30, True, False)
    text_title = font.render("Look at the circle and click on it", True, WHITE)
    text_rect = text_title.get_rect()
    text_rect.centerx = x
    text_rect.y = y

    screen.blit(text_title, text_rect)



def insideCircle(x_p, y_p, x, y):
    if ((x_p - x) * (x_p - x) + (y_p - y) * (y_p - y)) < radius * radius:
        return True
    else:
        return False

def GazePointGUI():

    # Initialize the game engine
    pygame.init()

    # Set the height and width of the screen
    user32 = ctypes.windll.user32
    size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    pygame.display.set_caption("Eye Tracking")

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    x_left = radius
    x_right = user32.GetSystemMetrics(0) - radius
    y_top = radius
    y_bottom = user32.GetSystemMetrics(1) - radius

    x = user32.GetSystemMetrics(0)/2
    y = user32.GetSystemMetrics(1)/2
    flag = 0

    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                if flag == 0:

                    x = x_left
                    y = y_top
                    flag = 1
                elif flag == 1:
                    x = x_right
                    y = y_top
                    flag = 2
                elif flag == 2:
                    x = x_left
                    y = y_bottom
                    flag = 3
                elif flag == 3:
                    x = x_right
                    y = y_bottom
                    flag = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if insideCircle(mouse[0], mouse[1], x, y):
                    if flag == 0:
                        x = x_left
                        y = y_top
                        flag = 1
                    elif flag == 1:
                        x = x_right
                        y = y_top
                        flag = 2
                    elif flag == 2:
                        x = x_left
                        y = y_bottom
                        flag = 3
                    elif flag == 3:
                        x = x_right
                        y = y_bottom
                        flag = 4
                    elif flag == 4:
                        done = True



        # All drawing code happens after the for loop and but
        # inside the main while done==False loop.

        # Clear the screen and set the screen background
        screen.fill(BLACK)

        writeText(screen, user32.GetSystemMetrics(0)/2, 50)
        # Draw a solid circle
        pygame.draw.circle(screen, GREEN, [x, y], radius)

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

    # Be IDLE friendly
    pygame.quit()