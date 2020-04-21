import tensorflow as tf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Load pretrained model
model = tf.keras.models.load_model('CNN/CNN.model')

# Show the model archtecture
model.summary()

# Load dataset
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# Test
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)
predict_result = model.predict(test_images)
predict_labels = [predict_result[i].argmax() for i in range(predict_result.shape[0])]
mat = confusion_matrix(test_labels, predict_labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()