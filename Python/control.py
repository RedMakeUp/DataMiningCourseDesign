
import tensorflow as tf
import logging, os
import numpy as np
import pickle as pk
from matplotlib.image import imread

models = {}
def init():
    logging.disable(logging.WARNING)
    logging.disable(logging.INFO)
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

    models['cnn'] = tf.keras.models.load_model('../../../Python/CNN/CNN.model')
    models['simple_ann'] = tf.keras.models.load_model('../../../Python/SimpleANN/simple_ann_model.model')
    models['decision_tree'] = pk.load(open("../../../Python/DecisionTree/decisionTree.pkl","rb"))
    models['svm'] = pk.load(open("../../../Python/SVM/SVM.pkl","rb"))
    # print('Initialize successfully')


def predict(filename, classifer):
    if classifer == 'cnn':
        test_image = imread(filename)
        return predict_with_Cnn(test_image)
    elif classifer == 'simple_ann':
        test_image = imread(filename)
        return predict_with_simpleAnn(test_image)
    elif classifer == 'decision_tree':
        test_image = imread(filename)
        return predict_with_decision_tree(test_image)
    elif classifer == 'svm':
        test_image = imread(filename)
        return predict_with_svm(test_image)

    return -10

def predict_with_simpleAnn(image):
    image = image.reshape((28 * 28, ))
    scores = models['simple_ann'].predict(np.array([image]))
    return np.argmax(scores)

def predict_with_Cnn(image):
    image = image.reshape((1, 28, 28, 1))
    scores = models['cnn'].predict(image)
    return np.argmax(scores)

def predict_with_decision_tree(image):
    image = image.reshape((28 * 28, ))
    digits = models['decision_tree'].predict(np.array([image]))
    return digits[0]

def predict_with_svm(image):
    image = image.reshape((28 * 28, ))
    digits = models['svm'].predict(np.array([image]))
    return digits[0]