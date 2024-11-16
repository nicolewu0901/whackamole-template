import pygame
import random

def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (32, 32))

        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_position = (0, 0)

        def draw_mole(position):
            x, y = position
            screen.blit(mole_image, mole_image.get_rect(topleft=(x * 32, y * 32)))

        def get_random_position():
            return random.randint(0, 19), random.randint(0, 15)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = event.pos
                    clicked_col = mouse_x // 32
                    clicked_row = mouse_y // 32

                    if (clicked_col, clicked_row) == mole_position:
                        mole_position = get_random_position()

            screen.fill("pink")

            for x in range(0, 640, 32):
                pygame.draw.line(screen, "black", (x, 0), (x, 512))
            for y in range(0, 512, 32):
                pygame.draw.line(screen, "black", (0, y), (640, y))

            draw_mole(mole_position)

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
