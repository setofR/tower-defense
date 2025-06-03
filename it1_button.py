class Button:
    """
    A class representing a button in a graphical user interface.

    Args:
            x (int): The x-coordinate of the button.
            y (int): The y-coordinate of the button.
            init_text (str): The initial text displayed on the button.
            font (pygame.font.Font): The font used for rendering the text.
            color (tuple): The color of the button.

    Attributes:
            x (int): The x-coordinate of the button.
            y (int): The y-coordinate of the button.
            init_text (str): The initial text displayed on the button.
            font (pygame.font.Font): The font used for rendering the text.
            color (tuple): The color of the button.
            text (pygame.Surface): The rendered text on the button.
            image (pygame.Surface): The image of the button.
            rect (pygame.Rect): The rectangle representing the button's position and size.
            text_rect (pygame.Rect): The rectangle representing the position and size of the text.

    Methods:
            update(screen): Updates the button's appearance on the screen.
            checkForInput(position): Checks if the given position is within the button's boundaries.
            changeColor(position): Changes the color of the button based on the given position.
    """

    # Constructor method
    def __init__(self, x, y, init_text, font, color):
        self.x = x
        self.y = y
        self.init_text = init_text
        self.font = font
        self.color = color
        self.text = self.font.render(self.text_input, True, self.color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1
        ] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1
        ] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
