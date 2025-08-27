import pygame

class Button:
    def __init__(self, screen, color_light, color_dark, x, y, width, height, text, text_color, font_name, font_size):
        self.screen = screen
        self.color_light = color_light
        self.color_dark = color_dark
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.rendered_text = self.font.render(text, True, text_color)

    def draw(self, mouse_pos):
        if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
            pygame.draw.rect(self.screen, self.color_light, [self.x, self.y, self.width, self.height])
        else:
            pygame.draw.rect(self.screen, self.color_dark, [self.x, self.y, self.width, self.height])

        text_x = self.x + (self.width - self.rendered_text.get_width()) / 2
        text_y = self.y + (self.height - self.rendered_text.get_height()) / 2
        self.screen.blit(self.rendered_text, (text_x, text_y))

    def is_clicked(self, mouse_pos):
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height
    
    def remove(self, screen):
        self.screen = screen
        self.color_light = (0,0,0,0)
        self.color_dark = (0,0,0,0)
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.text = ""
        self.text_color = (0,0,0,0)
