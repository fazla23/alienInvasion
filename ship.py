import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai_settings,screen): #screen parameter is for the screen where the ship will be drawn
		"""Initialize ship & set starting position."""
		super(Ship,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		
		#loading image and getting rect.
		#rect() means rectangle python takes everyyhing as rectangle as it is easy to control
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect() 
		self.screen_rect=screen.get_rect()
		
		
		#start new ship at the bottom center of the screen
		self.rect.centerx=self.screen_rect.centerx 
		self.rect.bottom=self.screen_rect.bottom
		
		#store a decimal value for the center of the ship
		self.center=float(self.rect.centerx)
		
		#movement flag
		self.moving_right=False
		self.moving_left=False
		
	def update(self):
		"""Update the ship's position depending on the movement flag"""
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center+=self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			self.center-=self.ai_settings.ship_speed_factor
		
		#Update the rect object from self.center
		self.rect.centerx=self.center
		
	def blitme(self):
		"""Draw the ship in current location"""
		self.screen.blit(self.image,self.rect)
	
	def center_ship(self):
		""" Center the ship on the screen."""
		self.center = self.screen_rect.centerx
	