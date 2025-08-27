import pygame, sys
from MainCharacter import MainCharacter as MC

class ChoosePlayer:

    def __init__(self):
        self.imageFile = 'none'

# Set up the Pygame window
    def choose_loop(self):
        screen_width = 1280
        screen_height = 720
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Select Your Player")

        # Load the background image
        background_img = pygame.image.load("StartMenuBackground.jpg").convert()

        # Load the character images
        character1_img = pygame.image.load("CharYellowFrontView.png").convert_alpha()
        character2_img = pygame.image.load("CharOrngFrontView.png").convert_alpha()
        character3_img = pygame.image.load("CharGreenFrontView.png").convert_alpha()

        # Set the positions of the character images
        character1_rect = character1_img.get_rect(center=(screen_width // 4, screen_height // 2))
        character2_rect = character2_img.get_rect(center=(screen_width // 2, screen_height // 2))
        character3_rect = character3_img.get_rect(center=(screen_width // 4 * 3, screen_height // 2))

        # Set up the font and text for the instructions
        font = pygame.font.Font('FORCED SQUARE.ttf', 75)
        font2 = pygame.font.Font('CoffeeHealing.ttf', 18)
        text = font.render('Select Your Player', True, (255,45,115))
        text_rect = text.get_rect(center=(screen_width // 2, 50))

        # Set up a variable to keep track of the selected character
        selected_character = None

        # Set up the list of character names and their positions
        character_attributes = [
            ("Bonus Attribute: +2 HP", (character1_rect.centerx, character1_rect.bottom + 20)),
            ("Bonus Attribute: +2 Attack", (character2_rect.centerx, character2_rect.bottom + 20)),
            ("Bonus Attribute: +2 Elemental Attack", (character3_rect.centerx, character3_rect.bottom + 20))
        ]

        # Function to render the character attributes text
        def render_character_attributes(name, pos):
            attribute_text = font2.render(name, True, (255, 255, 255))
            attribute_rect = attribute_text.get_rect(center=pos)
            screen.blit(attribute_text, attribute_rect)

        # Set up the main game loop
        running = True
        while running:

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and selected_character is not None:
                    # Move to level 1 if a character has been selected
                    running = False

            # Blit the background image onto the screen
            screen.blit(background_img, (0, 0))

            # Draw the character images
            screen.blit(character1_img, character1_rect)
            screen.blit(character2_img, character2_rect)
            screen.blit(character3_img, character3_rect)

            # Draw the selected character with a bigger size
            if selected_character == character1_rect:
                pygame.draw.rect(screen, (255, 255, 255), character1_rect, 4)
                screen.blit(pygame.transform.scale(character1_img, (120, 120)), (character1_rect.centerx - 60, character1_rect.centery - 60))
                render_character_attributes(character_attributes[0][0], character_attributes[0][1])
            elif selected_character == character2_rect:
                pygame.draw.rect(screen, (255, 255, 255), character2_rect, 4)
                screen.blit(pygame.transform.scale(character2_img, (120, 120)), (character2_rect.centerx - 60, character2_rect.centery - 60))
                render_character_attributes(character_attributes[1][0], character_attributes[1][1])
            elif selected_character == character3_rect:
                pygame.draw.rect(screen, (255, 255, 255), character3_rect, 4)
                screen.blit(pygame.transform.scale(character3_img, (120, 120)), (character3_rect.centerx - 60, character3_rect.centery - 60))
                render_character_attributes(character_attributes[2][0], character_attributes[2][1])

            # Draw the instructions text
            screen.blit(text, text_rect)

            # Check if the mouse is hovering over a character image
            mouse_pos = pygame.mouse.get_pos()
            if character1_rect.collidepoint(mouse_pos):
                selected_character = character1_rect
                self.imageFile = 'CharYellowFrontView.png'

            elif character2_rect.collidepoint(mouse_pos):
                selected_character = character2_rect
                self.imageFile = 'CharOrngFrontView.png'
            elif character3_rect.collidepoint(mouse_pos):
                selected_character = character3_rect
                self.imageFile = 'CharGreenFrontView.png'
            else:
                selected_character = None
                

            # Draw the highlighted image for the selected character
            if selected_character is not None:
                highlighted_rect = pygame.Rect(selected_character)
                highlighted_rect.inflate_ip(20, 20)
                pygame.draw.rect(screen, (255, 255, 255), highlighted_rect, 2)

            # Update the screen
            pygame.display.update()

