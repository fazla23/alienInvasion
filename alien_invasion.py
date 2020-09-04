import pygame

from settings import Settings
from ship import Ship
import game_function as gf #giving a name to function is called aliasing
from pygame.sprite import Group
from bullet import Bullet
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	# initialize game, settings and create screen object.
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#Make the play button
	play_button = Button(ai_settings,screen,"Play")
	
	#Create an instance to store Game statistics and create a scorecard
	stats = GameStats(ai_settings)
	sb=Scoreboard(ai_settings,screen,stats)
	
	#Make a ship , a group of bullets and a group of alien
	ship=Ship(ai_settings,screen)
	aliens=Group()
	bullets=Group()
	
	#Create the fleet of alien
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	#Start the main loop for the game
	while True:
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:	
			ship.update()
			gf.update_bullets(ai_settings,screen,sb,ship,stats,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
			play_button)		
		# Make the most recently drawn visible.
		pygame.display.flip()
		
run_game()
