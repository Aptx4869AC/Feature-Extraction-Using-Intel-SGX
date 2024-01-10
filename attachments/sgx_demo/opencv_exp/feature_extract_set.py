# -*- coding: utf-8 -*-
# @Author  : qiaohezhe
# @github : https://github.com/fengduqianhe
# @Date    :  9/17/2023 
# version： Python 3.7.8
# @File : feature_extract_set.py
# @Software: PyCharm

from __init__ import *
import os
import cv2
import numpy as np
import imageio


# Feature extractor
def extract_features(image_path, vector_size=32):
    image = imageio.imread(image_path)
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create()
        # alg = cv2.SIFT_create()  # SIFT
        # alg = cv2.ORB_create()  # ORB

        # Finding image keypoints
        kps = alg.detect(image)

        # Getting first 32 of them.
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]

        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)

        # Flatten all of them in one big vector - our feature vector
        dsc = dsc.flatten()

        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros
            # at the end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print("run is error!")
        print ('Error: ', e)
        return None
    print("run is ok!")
    return dsc

#
def batch_extractor(images_path, pickled_db_path="features_aug.pck"):
    images_path='/bin/opencv_exp/data/card_dataset/'
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    result = {}
    for f in files:
       print('Extracting features from image %s' % f)
       name = f.split('/')[-1].lower()
       result[name] = extract_features(f)
       print(result[name])

    # saving all our feature vectors in pickled file
    # with open(pickled_db_path, 'wb') as fp:
    #     cpickle.dump(result, fp)
