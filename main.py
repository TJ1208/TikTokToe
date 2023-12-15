import os
import pygame

# Sets Width / Height / Title of game window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)


# Contains code for updating window display
def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()


# Main function containing events to be looped
# Collision, Movement, etc.
def main():
    # Controls speed of while loop
    # Creates consistency amongst other systems
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


# Checks to make sure main() is only ran if the file is selected directly
# Won't run if file is imported into another file
if __name__ == "__main__":
    main()

