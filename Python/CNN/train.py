import os
import tensorflow as tf
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from datetime import datetime

import sys
sys.path.append('')
import helper

# Load the dataset
(train_images, train_labels), (test_images, test_labels) = helper.load_data()

# Reshape
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)
# Normalize
train_images.astype('float32')
test_images.astype('float32')
train_images = train_images / 255.0
test_images = test_images / 255.0

# Define a model
def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (5, 5), kernel_initializer='he_uniform', input_shape=input_shape, activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Conv2D(32, (3, 3), kernel_initializer='he_uniform', activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model

# Create a model
model = create_model()
# Display the model's archtecture
model.summary()

# Train
logdir="CNN/logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)
model.fit(train_images,
          train_labels,
          epochs=10,
          batch_size=32,
          validation_data=(test_images, test_labels),
          callbacks=[tensorboard_callback])

# Evaluate the model
loss, acc = model.evaluate(test_images,  test_labels, verbose=2)
print("Accuracy: {:5.2f}%".format(100*acc))

# Save the model
model.save('CNN/CNN.model')