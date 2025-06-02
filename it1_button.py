class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        # Set all the button's properties from the parameters
        self.image = image  # Can be a background image or None
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color  # Color of the text normally
        self.hovering_color = hovering_color  # Color when hovered over
        self.text_input = text_input  # The actual text on the button

        # Render the text using the font and base color
        self.text = self.font.render(self.text_input, True, self.base_color)

        # If no image is provided, use the rendered text as the button appearance
        if self.image is None:
            self.image = self.text

        # Create a rectangle for the image and text for positioning and collision detection
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        # Draw the button's image and text onto the screen
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        # Check if the mouse position is inside the button's rectangle
        return self.rect.collidepoint(position)

    def changeColor(self, position):
        # Change the button text color if the mouse is hovering over it
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


"""
__init__(...)

This method sets up the button with:
	•	Position (x, y) where the button will appear.
	•	Image (can be None, and it just uses text).
	•	Text to display on the button (text_input).
	•	Font, base color, and hovering color to control the look and feel.
	•	It uses pygame.Rect to handle position and size for detecting mouse clicks and hover effects.

update(screen)

Draws the button’s image and the text onto the screen.

checkForInput(position)

Checks whether the mouse is clicking inside the button’s area. Used to trigger actions (e.g. start game, quit).

changeColor(position)

Changes the text color when the mouse is hovering over the button, providing visual feedback to the user.

⸻
"""
