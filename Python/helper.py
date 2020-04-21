import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import sys
from matplotlib import gridspec

# Plot some details about the dataset and show some example points
def showDatasetExamples(xTrain, yTrain, xTest, yTest):
    fig = plt.figure(figsize=(6, 6))
    fig.canvas.set_window_title('MINIST Dataset Examples')
    gs = gridspec.GridSpec(3, 1, height_ratios=[1, 1, 6])
    # Subplot "Summary"
    ax_summary = plt.subplot(gs[0])
    ax_summary.set_xticks([])
    ax_summary.set_yticks([])
    ax_summary.set_title('Dataset Summary', fontsize=20, fontweight='bold')
    ax_summary.axis('off')
    ax_summary.axhline(1.0, color='black')
    ax_summary_text_size = 12
    ax_summary_mono = {'family' : 'monospace'}
    ax_summary.text(0.14, 0.6, "Each image size:         28*28*1", fontsize=ax_summary_text_size, fontdict=ax_summary_mono)
    ax_summary.text(0.14, 0.3, "Train set image numbers: {}".format(xTrain.shape[0]), fontsize=ax_summary_text_size, fontdict=ax_summary_mono)
    ax_summary.text(0.14, 0.0, "Test set image numbers:  {}".format(xTest.shape[0]), fontsize=ax_summary_text_size, fontdict=ax_summary_mono)
    # Subplot "Examples"
    ax_examples = plt.subplot(gs[2])
    ax_examples.set_xticks([])
    ax_examples.set_yticks([])
    ax_examples.set_title('Dataset Examples', fontsize=20, fontweight='bold')
    ax_examples.axis('off')
    ax_examples.axhline(1.0, color='black')
    ax_examples_inners = gridspec.GridSpecFromSubplotSpec(3, 5, gs[2], wspace=0.1, hspace=0.1)
    for i in range(ax_examples_inners.nrows):
        for j in range(ax_examples_inners.ncols):
            ax = fig.add_subplot(ax_examples_inners[i, j])
            ax.set_xticks([])
            ax.set_yticks([])
            index = i * ax_examples_inners.nrows + j
            ax.imshow(xTrain[index], cmap='binary', interpolation='nearest')
            ax.text(0.05, 0.05, str(yTrain[index]), transform=ax.transAxes, color='green')

    plt.show()

# Load minst data from tensorflow database and return data with wanted size
def load_data(train_count=sys.maxsize, test_count=sys.maxsize, categorical=True):
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
    
    if categorical == True:
        train_labels = tf.keras.utils.to_categorical(train_labels, 10)
        test_labels = tf.keras.utils.to_categorical(test_labels, 10)
    
    return (train_images[:train_count], train_labels[:train_count]), (test_images[:test_count], test_labels[:test_count])

# Download MINST test/train set from tensorflow database to local files
def download_data(rootDir='MINST', subset_type='test'):
    from PIL import Image
    import os
    import glob

    target_dir_prefix = ''
    if subset_type == 'test':
        target_dir_prefix = rootDir+'/test/label_'
    elif subset_type == 'train':
        target_dir_prefix = rootDir+'/train/label_'
    
    # Clear folders at first
    for i in range(10):
        filePath = target_dir_prefix + str(i) + '/*'
        files = glob.glob(filePath)
        for f in files:
            os.remove(f)
    print('Clean done')

    # Load all test data
    (images, labels) = load_data()[1]
    counter = np.zeros(10, 'int32')
    for i in range(images.shape[0]):
        label = labels[i]
        counter[label] = counter[label] + 1
        target_dir = target_dir_prefix + str(label) + '/'
        img = Image.fromarray(images[i], 'L')
        img.save(target_dir + str(counter[label]) +'.png')
    print('Download done')

# download_data(subset_type='train')
# (xTrain, yTrain),(xTest,yTest) = load_data(categorical=False)
# showDatasetExamples(xTrain, yTrain, xTest, yTest)
