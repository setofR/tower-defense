import pygame
from sys import exit
from it1_button import Button

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Tower Defense")

clock = pygame.time.Clock()

def get_font(size):
    return pygame.font.Font(None, size)

def play():
    running = True
    while running:
        screen.fill("darkblue")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                
        text = get_font(40).render("Game Screen (ESC to return)", True, "white")
        screen.blit(text, text.get_rect(center=(400, 250)))
        
        pygame.display.update()
        clock.tick(60)

def menu():
    while True:
        screen.fill("black")
        mouse_pos = pygame.mouse.get_pos()
        
        title_text = get_font(50).render("Tower Defense", True, "white")
        title_rect = title_text.get_rect(center=(400, 100))
        screen.blit(title_text, title_rect)
        
        play_button = Button(None, (400, 200), "PLAY", get_font(36), "white", "green")
        options_button = Button(None, (400, 280), "OPTIONS", get_font(36), "white", "green")
        quit_button = Button(None, (400, 360), "QUIT", get_font(36), "white", "green")
        
        for button in [play_button, options_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    play()
                if options_button.checkForInput(mouse_pos):
                    print("Options not implemented yet")
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()
                    
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    menu()