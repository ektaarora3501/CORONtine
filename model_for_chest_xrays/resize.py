#resizing all the images in the directory


'''Copyright notice..
The work, code and algorithm belongs to team Dev.ino .The team must be acknowledged for use of any portion of the project/code . The team Dev.ino reserves all rights on the code and the dataset .
We would be happy to mention https://github.com/ieee8023/covid-chestxray-dataset for their dataset for Chest X-Ray model creation

Team Dev.ino
Developers
Krishna Ojha
Ekta Arora
'''



#!/usr/bin/python
from PIL import Image
import os, sys

path = "/home/ekta3501/opensource/Dev.ino_HackCovid19/chest/train/non_covid_xrays/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            # print(f,e)
            if(e=='.png'):
                # print(f)
                imResize = im.resize((200,200), Image.ANTIALIAS)
                imResize.save(f +'.png','PNG', quality=90)
                # print("faltu")

            elif(e=='.jpg'):
                # print('.jpg')
                imResize = im.resize((200,200), Image.ANTIALIAS)
                imResize.save(f +'.jpg','JPEG', quality=90)

            elif(e=='.jpeg'):
                # print('.jpeg')
                imResize = im.resize((200,200), Image.ANTIALIAS)
                imResize.save(f +'.jpeg','JPEG', quality=90)
                print("done")


            # imResize = im.resize((200,200), Image.ANTIALIAS)
            # imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()
