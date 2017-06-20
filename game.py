import pygame
import sys
from Settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stat import GameStats
from button import Button
from scoreboard import Scoreboard
import time

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("COMP140风云--领带怪兽抵抗战")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb,  play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb,  ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
