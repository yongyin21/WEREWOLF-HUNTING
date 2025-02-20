class Button():
    def __init__(self, image, pos, text_input=None, font=None, base_color=None, hovering_color=None):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input

        # If text is provided, create it. Otherwise, set text to None.
        if self.text_input and self.font:
            self.text = self.font.render(self.text_input, True, self.base_color)
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        else:
            self.text = None
            self.text_rect = None  # Fix for NoneType error
       
        # Set up image rect
        if self.image is not None:
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        else:
            self.rect = None


    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)  # Draw button image

        if self.text is not None and self.text_rect is not None:
            screen.blit(self.text, self.text_rect)  # Only draw text if it exists


    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if self.text_input and self.font:  # Only render if font exists
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                self.text = self.font.render(self.text_input, True, self.hovering_color)
            else:
                self.text = self.font.render(self.text_input, True, self.base_color)
