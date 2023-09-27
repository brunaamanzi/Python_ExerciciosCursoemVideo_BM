# Desafio 21: Faça um programa em Python que abra e reproduza um áudio de um arquivo MP3.
# biblioteca utilizada pygame. para iniciar: pygame.init()
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

