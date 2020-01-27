from matplotlib import pyplot as plt

import numpy as np
import os
import tensorflow as tf

from datasets import imagedata
from nets import inception
from preprocessing import inception_preprocessing

checkpoints_dir = './tmp/inception_finetuned/'
imagedata_dir = '.'
slim = tf.contrib.slim

image_size = inception.inception_v4.default_image_size    

#with tf.Graph().as_default():
def eval_image():
    user_images = [] # 복수의 원본 이미지
    user_processed_images = [] # 복수의 전처리된 이미지
    
    dataset = imagedata.get_split('train', imagedata_dir)
    image_files = os.listdir("/home/ubuntu/webpy/dir_picture")
    #image_files = os.listdir("/home/ubuntu/test4/bigdataAnalytics/restFileUpload/dir_picture")
    #image_files = os.listdir("C:\\Users\\user\\Desktop\\ttt") # 분류하고 싶은 이미지가 저장된 폴더

    for i in image_files:
        image_input = tf.read_file("/home/ubuntu/webpy/dir_picture" +'/'+ i)
        #image_input = tf.read_file("/home/ubuntu/test4/bigdataAnalytics/restFileUpload/dir_picture" +'/'+ i)
        #image_input = tf.read_file("C:\\Users\\user\\Desktop\\ttt" +'/'+ i)
        image = tf.image.decode_jpeg(image_input, channels=3)
        user_images.append(image)
        processed_image = inception_preprocessing.preprocess_image(image, image_size, image_size, is_training=False)
        user_processed_images.append(processed_image)
        
    processed_images  = tf.expand_dims(processed_image, 0)
    
    with slim.arg_scope(inception.inception_v4_arg_scope()):
        logits, _ = inception.inception_v4(user_processed_images, num_classes=3, is_training=True)
    probabilities = tf.nn.softmax(logits)

    init_fn = slim.assign_from_checkpoint_fn(
        os.path.join(checkpoints_dir, 'model.ckpt-300'),
        slim.get_model_variables('InceptionV4'))

    with tf.Session() as sess:
        init_fn(sess)
        np_images, probabilities = sess.run([user_images, probabilities])


    count = [0, 0, 0, 0, 0]
    
    for files in range(len(image_files)):
        predicted_label = np.argmax(probabilities[files, :])
        predicted_name = dataset.labels_to_names[predicted_label]
        
        plt.figure()
        plt.imshow(np_images[files].astype(np.uint8))
        plt.title('%d , Prediction [%s]' % (predicted_label, predicted_name))
        plt.axis('off')
        plt.show()
        
        if(predicted_name=='cat'):
            count[0]+=1
        elif(predicted_name=='clown'):
            count[1]+=1
        elif(predicted_name=='dog'):
            count[2]+=1
        elif(predicted_name=='frog'):
            count[3]+=1
        else: #spider
            count[4]+=1

    print(count[0], count[1], count[2], count[3], count[4])
    return count