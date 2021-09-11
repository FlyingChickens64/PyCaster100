import math
import pygame
worldMap = [
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	[1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
def main():
	screenWidth = 1000
	screenHeight = 500
	screen = pygame.display.set_mode((screenWidth, screenHeight))
	pygame.display.set_caption("PyCaster100")
	posX = 2
	posY = 2
	dirX = 1
	dirY = 0
	planeX = 0
	planeY = 1
	zde = 0.00000001
	movSpeed = 16
	rotSpeed = 6
	while True:
		clock = pygame.time.Clock()
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP]:
			if (worldMap[int(posX + dirX / movSpeed)][int(posY + dirY / movSpeed)] == 0):
				posX += dirX / movSpeed
				posY += dirY / movSpeed
		if pressed[pygame.K_DOWN]:
			if (worldMap[int(posX - dirX / movSpeed)][int(posY - dirY / movSpeed)] == 0):
				posX -= dirX / movSpeed
				posY -= dirY / movSpeed
		if pressed[pygame.K_LEFT]:
			oldDirX = dirX
			dirX = dirX * math.cos(rotSpeed) - dirY * math.sin(rotSpeed)
			dirY = oldDirX * math.sin(rotSpeed) + dirY * math.cos(rotSpeed)
			oldPlaneX = planeX
			planeX = planeX * math.cos(rotSpeed) - planeY * math.sin(rotSpeed)
			planeY = oldPlaneX * math.sin(rotSpeed) + planeY * math.cos(rotSpeed)
		if pressed[pygame.K_RIGHT]:
			oldDirX = dirX
			dirX = dirX * math.cos(-rotSpeed) - dirY * math.sin(-rotSpeed)
			dirY = oldDirX * math.sin(-rotSpeed) + dirY * math.cos(-rotSpeed)
			oldPlaneX = planeX
			planeX = planeX * math.cos(-rotSpeed) - planeY * math.sin(-rotSpeed)
			planeY = oldPlaneX * math.sin(-rotSpeed) + planeY * math.cos(-rotSpeed)
		screen.fill((0,0,0))
		x = 0
		while x != screenWidth:
			cameraX = 2 * x / screenWidth - 1
			rayPosX = int(posX)
			rayPosY = int(posY)
			rayDirX = dirX + planeX * cameraX
			rayDirY = dirY + planeY * cameraX
			deltaDistX = abs(1 / rayDirX)
			deltaDistY = abs(1 / (rayDirY + zde))
			if (rayDirX < 0):
				stepX = -1
				sideDistX = (posX - rayPosX) * deltaDistX
			else:
				stepX = 1
				sideDistX = (rayPosX + 1 - posX) * deltaDistX
			if (rayDirY < 0):
				stepY = -1
				sideDistY = (posY - rayPosY) * deltaDistY
			else:
				stepY = 1
				sideDistY = (rayPosY + 1 - posY) * deltaDistY
			hit = 0
			while (hit == 0):
				if (sideDistX < sideDistY):
					sideDistX += deltaDistX
					rayPosX += stepX
					side = 0
				else:
					sideDistY += deltaDistY;
					rayPosY += stepY;
					side = 1
				if (worldMap[rayPosX][rayPosY] == 1):
					hit = 1
			if (side == 0):
				perpWallDist = (rayPosX - posX + (1 - stepX) / 2) / rayDirX
			else:
				perpWallDist = (rayPosY - posY + ( 1 - stepY ) / 2) / rayDirY
			lineHeight = int(screenHeight / (perpWallDist + zde))
			drawStart = -lineHeight / 2 + screenHeight / 2
			drawEnd = lineHeight / 2 + screenHeight / 2
			if side == 1:
				pygame.draw.line(screen, (100, 100, 100), (x, drawStart), (x, drawEnd), 1)
			else:
				pygame.draw.line(screen, (150, 150, 150), (x, drawStart), (x, drawEnd), 1)
			x += 1
		pygame.display.update()
main()
