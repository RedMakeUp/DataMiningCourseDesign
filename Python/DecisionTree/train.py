import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pickle as pk
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import sys
sys.path.append('')
import helper

# Plot pca curve
def plot_pca_cumulativa_variance(images):
    plt.xlim(-10, 800)
    plt.ylim(-0.2, 1.2)

    pca = PCA().fit(images)
    points = np.cumsum(pca.explained_variance_ratio_)
    marker_x = 100
    marker_y = points[100]

    plt.plot(points)
    plt.scatter([marker_x], [marker_y], marker='o', color='r')
    plt.text(marker_x + 0.2, marker_y - 0.1, s='(' + str(marker_x) + ', ' + str(round(marker_y, 2)) + ')')
    plt.plot([marker_x, marker_x], [-0.2, marker_y], linestyle='--', color='orange')
    plt.plot([-10, marker_x], [marker_y, marker_y], linestyle='--', color='orange')
    
    plt.xlabel('number of components')
    plt.ylabel('cumulative explained variance')
    plt.show()


# Load the dataset
(train_images, train_labels), (test_images, test_labels) = helper.load_data(categorical=False)

# Flat
train_images = train_images.reshape(-1, 28*28) / 255
# test_images = test_images.reshape(-1, 28*28) / 255

# # Show PCA result
# plot_pca_cumulativa_variance(train_images)
# plt.show()

# 100 dims can reach about 90% explained variance
pca = PCA(100)
# Create a decision tree(CART)
dtc = tree.DecisionTreeClassifier()
# Create a model that first performs PCA, then CART decision tree classifer
model = make_pipeline(pca, dtc)
# Begin training
model.fit(train_images, train_labels)
# Save the model
pk.dump(model, open("DecisionTree/decisionTree.pkl","wb"))

# Show results
predict_labels = model.predict(test_images)
print(metrics.classification_report(test_labels, predict_labels))