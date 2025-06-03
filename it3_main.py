import pygame
from sys import exit
from it2_button import Button
from it3_game import Game

pygame.init()

master_volume = 0.3
test_music_playing = False
test_music_position = 0

canvas = pygame.display.set_mode((800, 800))
pygame.display.set_caption("StarGuard")

clock = pygame.time.Clock()

def get_font(size):
    return pygame.font.Font("assets/fonts/font.ttf", size)

def play():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets/music/greensleeves-8bit.ogg")
    pygame.mixer.music.set_volume(master_volume)
    pygame.mixer.music.play(loops=-1)
    
    game = Game()
    
    running = True
    while running:
        canvas.fill("darkblue")
        mouse_pos = pygame.mouse.get_pos()
        
        game.draw_grid(canvas)
        
        grid_pos = game.get_grid_pos(mouse_pos)
        if grid_pos and game.can_place_tower(grid_pos):
            x, y = grid_pos
            pygame.draw.rect(canvas, (0, 255, 0, 100), 
                           (x * game.grid_size, y * game.grid_size, 
                            game.grid_size, game.grid_size), 2)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if grid_pos and game.can_place_tower(grid_pos):
                    print("notihng happens yet")
                    # code to place a tower would go here
        
        pygame.display.update()
        clock.tick(60)
    
    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets/music/debussy-arabesque-1.ogg")
    pygame.mixer.music.set_volume(master_volume)
    pygame.mixer.music.play(loops=1, fade_ms=3000)

def options():
    pygame.mixer.music.stop()
    global master_volume, test_music_playing, test_music_position

    volume_label = get_font(30).render("VOLUME", True, "white")
    vol_up_btn = Button(None, (540, 200), "+", get_font(40), "green", "darkgreen")
    vol_down_btn = Button(None, (260, 200), "-", get_font(40), "red", "darkred")
    test_music_btn = Button(None, (400, 300), "TEST MUSIC", get_font(30), "white", "gray")

    running = True
    while running:
        canvas.fill("indigo")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if test_music_playing:
                    pygame.mixer.music.stop()
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if vol_up_btn.checkForInput(pygame.mouse.get_pos()):
                    master_volume = min(1.0, master_volume + 0.1)
                    pygame.mixer.music.set_volume(master_volume)

                if vol_down_btn.checkForInput(pygame.mouse.get_pos()):
                    master_volume = max(0.0, master_volume - 0.1)
                    pygame.mixer.music.set_volume(master_volume)

                if test_music_btn.checkForInput(pygame.mouse.get_pos()):
                    if test_music_playing:
                        test_music_position = pygame.mixer.music.get_pos()
                        pygame.mixer.music.stop()
                        test_music_playing = False
                    else:
                        pygame.mixer.music.load("assets/music/mozart-vc3-mov1-8bit.ogg")
                        pygame.mixer.music.set_volume(master_volume)
                        pygame.mixer.music.play(-1, start=test_music_position / 1000.0)
                        test_music_playing = True

        heading = get_font(18).render("Options Menu (ESC to return)", True, "white")
        canvas.blit(heading, heading.get_rect(center=(400, 120)))

        canvas.blit(volume_label, volume_label.get_rect(center=(400, 200)))

        volume_value = get_font(20).render(f"{int(master_volume * 100)}%", True, "white")
        canvas.blit(volume_value, volume_value.get_rect(center=(400, 240)))

        test_music_btn.base_color = "green" if test_music_playing else "red"

        for button in [vol_up_btn, vol_down_btn, test_music_btn]:
            button.changeColor(pygame.mouse.get_pos())
            button.update(canvas)

        pygame.display.update()
        clock.tick(60)

    pygame.mixer.music.load("assets/music/debussy-arabesque-1.ogg")
    pygame.mixer.music.set_volume(master_volume)
    pygame.mixer.music.play(loops=1, fade_ms=3000)

def menu():
    pygame.mixer.music.load("assets/music/debussy-arabesque-1.ogg")
    pygame.mixer.music.set_volume(master_volume)
    pygame.mixer.music.play(loops=1, fade_ms=3000)

    while True:
        canvas.fill("black")
        mouse_pos = pygame.mouse.get_pos()

        title_text = get_font(50).render("StarGuard", True, "gold")
        title_rect = title_text.get_rect(center=(canvas.get_width() // 2, canvas.get_height() // 2 - 160))
        canvas.blit(title_text, title_rect)

        center_x = canvas.get_width() // 2
        center_y = canvas.get_height() // 2
        spacing = 80

        play_button = Button(None, (center_x, center_y - spacing), "PLAY", get_font(36), "white", "purple")
        options_button = Button(None, (center_x, center_y), "OPTIONS", get_font(36), "white", "purple")
        quit_button = Button(None, (center_x, center_y + spacing), "QUIT", get_font(36), "white", "purple")

        for button in [play_button, options_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(canvas)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    play()
                if options_button.checkForInput(mouse_pos):
                    options()
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    menu()