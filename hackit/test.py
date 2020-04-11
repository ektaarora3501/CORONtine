'''                  Copyright notice..
The work, code and algorithm belongs to team Dev.ino .The team must be acknowledged for use of any portion of the project/code . The team Dev.ino reserves all rights on the code and the dataset .
We would be happy to mention https://github.com/ieee8023/covid-chestxray-dataset for their dataset for Chest X-Ray model creation

Team Dev.ino
Developers
Krishna Ojha
Ekta Arora
'''






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

model = load_model("model1_6_15.h5")
# model._make_predict_function()
graph1 = tf.get_default_graph()

# with tf.Session() as sess:
#       sess.run(tf.global_variables_initializer())





test_dir = '/home/ekta3501/opensource/Dev.ino_HackCovid19/chest/test/'

model.compile(loss="categorical_crossentropy",
            optimizer='adam',
            metrics=['accuracy']
)

def test_chest():
    onlyfiles = [f for f in listdir(test_dir) if isfile(join(test_dir, f))]
    print(onlyfiles)

    for files in onlyfiles:
       img = image.load_img(test_dir+files,target_size=(200,200))
       x = image.img_to_array(img)
       x = np.expand_dims(x,axis=0)

       images = np.vstack([x])
       # plt.imshow(images)
       with graph1.as_default():
           classes = model.predict_classes(images,batch_size=3)
       print(classes,files)
       classes = classes[0]

       return classes

# {'covid_xrays': 0, 'non_covid_xrays': 1}
