'''Copyright notice..
The work, code and algorithm belongs to team Dev.ino .The team must be acknowledged for use of any portion of the project/code . The team Dev.ino reserves all rights on the code and the dataset .
We would be happy to mention https://github.com/ieee8023/covid-chestxray-dataset for their dataset for Chest X-Ray model creation

Team Dev.ino
Developers
Krishna Ojha
Ekta Arora
'''



from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import os
import serial
from gtts import gTTS
import pygame
import time
import random
# from video_image import front
from live_test import predicting_cough
# arduino = serial.Serial('COM9', 9600)
from audio_positioning import arduino_call
from test import test_chest
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt




def Index(request):

    return render(request,'index.html')


def Detect(request):
    global flag_dis
    # arduino_call()

    return HttpResponseRedirect(reverse('images'))


    # return render(request,'index.html')




def take_images(request):
      v=str(random.randrange(1000,9999))
      data = predicting_cough()

      return render(request,"index.html",{'data':data})



def chest_scan(request):
    data = test_chest()  #if data == 1 => non covid person

    img = mpimg.imread('/home/ekta3501/opensource/Dev.ino_HackCovid19/chest/test/covid-19-caso-70-1-PA.jpg')
    plt.imshow(img)
    plt.show()

    if data:
        val = 0
    else:
        val = 1  # => patient has covid 19
    return render(request,"index.html",{"val":val})
