import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet50_preprocess

from tensorflow.keras.applications.efficientnet import EfficientNetB7
from tensorflow.keras.applications.efficientnet import preprocess_input as eff_preprocess

from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input as incept_preprocess

from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense


class Predict:
    """
    This class uses the trained models to classify if an image can be classified as ec or nec
    ec means eczema while nec means not eczema
    Only the get_result method is public, it expects an image path and returns the result
    """
    def __init__(self):
        self.height = 300
        self.width = 300
        self.resnet_model = keras.models.load_model('models/res50_model.h5')
        self.eff_model = keras.models.load_model('models/eff11_model.h5')
        self.inception_model = keras.models.load_model('models/inception_model.h5')

    def __resnet(self, x):
        x = resnet50_preprocess(x)
        preds = self.resnet_model.predict(x)
        return self.format_res(preds)

    def __efficient(self, x):
        x = eff_preprocess(x)
        preds = self.eff_model.predict(x)
        return self.format_res(preds)

    def __inception(self, x):
        x = incept_preprocess(x)
        preds = self.inception_model.predict(x)
        return self.format_res(preds)

    @staticmethod
    def format_res(pred):  # formats output result to percentage
        pred = list((pred*100)[0])
        pred = [float(round(i, 2)) for i in pred]
        return pred

    def __get_x(self, image_path, case=None):
        if case == 'inception':
            img = load_img(image_path, target_size=(224, 224))
            x = img_to_array(img)
            x = np.expand_dims(x, axis=0)
            return x
        else:
            img = load_img(image_path, target_size=(self.height, self.width))
            x = img_to_array(img)
            x = np.expand_dims(x, axis=0)
            return x

    def get_result(self, image_path):
        x = self.__get_x(image_path=image_path)
        xx = self.__get_x(case='inception', image_path=image_path)
        return {'resnet': self.__resnet(x),
                'efficient': self.__efficient(x),
                'inception': self.__inception(xx)}






