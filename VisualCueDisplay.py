import pygame

def main():
	pygame.init()
	screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # Fullscreen mode
	screen.fill((255, 0, 0)) # red screen
	pygame.display.flip()
	
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				running = False
				
	pygame.quit()
	
if __name__ == "__main__":
	main()
