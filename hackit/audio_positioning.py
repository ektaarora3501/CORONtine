'''Copyright notice..
The work, code and algorithm belongs to team Dev.ino .The team must be acknowledged for use of any portion of the project/code . The team Dev.ino reserves all rights on the code and the dataset .
We would be happy to mention https://github.com/ieee8023/covid-chestxray-dataset for their dataset for Chest X-Ray model creation

Team Dev.ino
Developers
Krishna Ojha
Ekta Arora
'''






import serial
import pygame
import time

def play(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(10)
    pygame.mixer.music.load("../hardware/audio-files/beep.mp3")


def arduino_call():
    arduino = serial.Serial('COM9', 9600)

    while 1:
        print(int(arduino.readline()))

        if abs(int(arduino.readline()) - 40) >= 8:
            while abs(int(arduino.readline()) - 40) >= 8:
                if int(arduino.readline()) > 80:
                    print(int(arduino.readline()))
                    play('../hardware/audio-files/guide1.mp3')
                elif int(arduino.readline()) < 80:
                    print(int(arduino.readline()))
                    play('../hardware/audio-files/guide2.mp3')
        else:
            print(int(arduino.readline()))
            play('../hardware/audio-files/guide4.mp3')
            break
