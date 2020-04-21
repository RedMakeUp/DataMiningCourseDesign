from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pickle as pk

import sys
sys.path.append(0, '')
import helper

# Load the dataset
(train_images, train_labels), (test_images, test_labels) = helper.load_data(categorical=False)
print("Load dataset")

# Flat
train_images = train_images.reshape(-1, 28*28) / 255.0
test_images = test_images.reshape(-1, 28*28) / 255.0

# Define the model
model = SVC(kernel='rbf', class_weight='balanced', C=5, gamma=0.05)

# Begin training
model.fit(train_images, train_labels)

pk.dump(model, open("SVM/SVM.pkl","wb"))
predict_labels = model.predict(test_images)

# Show the result
print(metrics.classification_report(test_labels, predict_labels))
mat = confusion_matrix(test_labels, predict_labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()
