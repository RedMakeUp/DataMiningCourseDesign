import tensorflow as tf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import sys
sys.path.append('')
import helper


# Load pretrained model
model = tf.keras.models.load_model('SimpleANN/simple_ann_model.model')

# Show the model archtecture
model.summary()

# Load the dataset
(train_images, train_labels), (test_images, test_labels) = helper.load_data()

# Predict
predict_labels = model.predict(test_images / 255.0)
print(predict_labels.shape)
predict_labels = np.argmax(predict_labels, axis=1)
print(predict_labels.shape)

# Test
print(metrics.classification_report(test_labels, predict_labels))
mat = confusion_matrix(test_labels, predict_labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()