import pygame
import random



def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        row = 0
        col = 0
        mole_cords = (0,0)
        mole_pos = (0,0)

        running = True
        while running:
            # Draw Grid
            screen.fill("pink")
            for i in range(1, 20):
                pygame.draw.line(screen, "dark blue", (i * 32, 0), (i * 32, 512))
            for i in range(1, 16):
                pygame.draw.line(screen, "dark blue", (0, i * 32), (640, i * 32))

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_cords)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = x // 32
                    col = y // 32
                    click_pos = row,col

                    # Check if mole is clicked
                    x, y = mole_cords
                    row = x // 32
                    col = y // 32
                    mole_pos = row, col
                    if mole_pos == click_pos:
                        #Move Mole
                        x = random.randrange(0, 640)
                        y = random.randrange(0, 512)
                        x -= x % 32
                        y -= y % 32
                        mole_cords = (x,y)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
