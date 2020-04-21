import os
import tensorflow as tf
from datetime import datetime

import sys
sys.path.append('')
import helper


# Load the dataset
(train_images, train_labels), (test_images, test_labels) = helper.load_data()

# Flat and normalize
train_images = train_images /255.0
test_images = test_images / 255.0

# Define a model
def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(256, activation='relu'),
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
logdir="SimpleANN/logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
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
model.save('SimpleANN/simple_ann_model.model')

