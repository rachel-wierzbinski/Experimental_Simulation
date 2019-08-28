import pygame
from environment import Environment
import time


def main():
    pygame.init()
    clock = pygame.time.Clock()

    # Display size
    display_width = 1000
    display_height = 400

    # Grid outline color
    BLACK = (0,0,0)
    # Empty block color
    WHITE = (255,255,255)
    # Obstacle color
    RED = (184,32,37)

    # Initialize display
    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Environment_Simulation')
    display.fill(BLACK)

    # Initialize environment
    env = Environment()

    done = False

    while not done:

        # Quit when user closes window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Location of grid squares
        x = 0
        y = 100

        # Grid square dimensions
        w = 100
        h = 100

        # Get new state
        old_state, new_state, reward = env.step()
        env.print_state()

        # Draw the grid
        obstacle = 1
        for row in new_state:
            for col in row:
                square_color = WHITE

                if col == obstacle:
                    square_color = RED

                pygame.draw.rect(display, square_color, [x, y, w, h])
                x += w

            y += h
            x = 0


        # Frame rate: 60 frames per second
        clock.tick(60)

        # Update display
        pygame.display.update()

if __name__ == '__main__':
    main()