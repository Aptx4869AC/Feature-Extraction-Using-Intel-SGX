# -*- coding: utf-8 -*-
# @Author  : qiaohezhe
# @github : https://github.com/fengduqianhe
# @Date    :  10/22/2023 
# version： Python 3.7.8
# @File : sgx_demo.py
# @Software: PyCharm
from __init__ import *
import os
os.environ['OMP_NUM_THREADS'] = '1'
from feature_extract_set import batch_extractor, extract_features


def run():
    images_path = 'data/card_dataset/'
    # batch_extractor(images_path)
    images = '/bin/opencv_exp/data/card_dataset/train.jpg'
    result = {}
    print('Extracting features from image %s' % images)
    name = images.split('/')[-1].lower()
    result[name] = extract_features(images)
    print(result[name])

run()
