#Importa o arquivo de áudio antes

import pygame
pygame.inti()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
