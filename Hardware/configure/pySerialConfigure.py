import os
import serial
import pygame
import time
from gtts import gTTS

def play(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(10)
    pygame.mixer.music.load("beep.mp3")
    # os.remove("guide.mp3")


arduino = serial.Serial('COM9', 9600)

while 1:
    print(int(arduino.readline()))

    if abs(int(arduino.readline()) - 20) >= 3:
        while abs(int(arduino.readline()) - 20) >= 3:
            if int(arduino.readline()) > 20:
                print(int(arduino.readline()))
                play('guide1.mp3')
            elif int(arduino.readline()) < 20:
                print(int(arduino.readline()))
                play('guide2.mp3')
    else:
        print(int(arduino.readline()))
        play('guide3.mp3')


# while 1:
#     data = int(arduino.readline())
#     print(data)
#     if data == 1:
#         print('move a bit closer')
#         play('guide1.mp3')
#     elif data == 2:
#         print('move a bit backward')
#         play("guide2.mp3")
#     elif data == 3:
#         print('rightly placed');
#         play('guide3.mp3')
