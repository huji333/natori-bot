import pygame

pygame.init()
def playAudio(path,n):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(n)
