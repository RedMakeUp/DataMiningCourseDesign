import matplotlib.pyplot as plt
import numpy as np
import pickle as pk
import os
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import confusion_matrix

import sys
sys.path.append(0, '')
import helper

# Load the dataset
(train_images, train_labels), (test_images, test_labels) = helper.load_data(categorical=False)
print("Load dataset")

# Flat
test_images = test_images.reshape(-1, 28*28) / 255.0

# Load SVM model
model = pk.load(open("SVM/SVM.pkl","rb"))         

# Predict
predict_labels = model.predict(test_images)

# Show the result
print(metrics.classification_report(test_labels, predict_labels))
mat = confusion_matrix(test_labels, predict_labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()