#running videos in image

'''Copyright notice..
The work, code and algorithm belongs to team Dev.ino .The team must be acknowledged for use of any portion of the project/code . The team Dev.ino reserves all rights on the code and the dataset .
We would be happy to mention https://github.com/ieee8023/covid-chestxray-dataset for their dataset for Chest X-Ray model creation

Team Dev.ino
Developers
Krishna Ojha
Ekta Arora
'''




import numpy as np
import cv2 as cv
import os,shutil
from PIL import Image
from os import listdir
from os.path import join,isfile
from keras.preprocessing import image
from keras.models import load_model
import time
import tensorflow as tf
from keras import backend as K
import tensorflow as tf
import numpy as np
# K.clear_session()
import time

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())


model = load_model("model2_2_11.h5")
# model._make_predict_function()
graph1 = tf.get_default_graph()

# with tf.Session() as sess:
#       sess.run(tf.global_variables_initializer())


model.compile(loss="categorical_crossentropy",
            optimizer='adam',
            metrics=['accuracy']
)


dir = 'F:\Github\HackCovid\Dev.ino_HackCovid19\hackit\image_store'
path = 'F:\Github\HackCovid\Dev.ino_HackCovid19\hackit\predicted'

# dir = '/home/ekta3501/opensource/Dev.ino_HackCovid19/image_store/'
# path = '/home/ekta3501/opensource/Dev.ino_HackCovid19/predicted/'

def predicting_cough():
    cap = cv.VideoCapture(0)
    count=0
    i=0
    ls=[5 for i in range(0,15)]
    print(ls)
    acc_count=0

    while (1):
        ret, frame = cap.read()
        print("i is and acc_count is ",i,acc_count)
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # if(count%10==0):
        name = dir +'image' + str(i) +'.jpg'
        # print("creating image")
        cv.imwrite(name,frame)
        im = Image.open(name)
        imResize = im.resize((28,28), Image.ANTIALIAS)
        imResize.save(name,'JPEG', quality=90)
        img = image.load_img(name,target_size=(28,28))
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis=0)

        images = np.vstack([x])
            # plt.imshow(images)
        # classes = model.predict_classes(images,batch_size=3)
        with graph1.as_default():
                    classes = model.predict_classes(images,batch_size=3)


        ls[i] = classes[0]

        if(ls[i]==0):
            acc_count+=1
            if(acc_count>=20):
                shutil.copy(name,path)
                cap.release()
                cv.destroyAllWindows()


                return 1
                # try:
                #     myimage=accident_images+'image' + st(i-1) + '.jpg'

                print("alert situation")
                acc_count=0

        else:
            acc_count=0

        if i==14:
            i=0
        else:
            i+=1

        count+=1

        cv.imshow('frame', frame)
        if cv.waitKey(20) & 0xFF == ord('q'): #running video till end
            break

        if count ==500 :
            break


    print(ls)
    cap.release()
    cv.destroyAllWindows()

    return 0
