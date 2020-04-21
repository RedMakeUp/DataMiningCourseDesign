import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pickle as pk
import graphviz 
from sklearn import tree
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import sys
sys.path.append('')
import helper

# Load the dataset
(train_images, train_labels), (test_images, test_labels) = helper.load_data(categorical=False)

# Flat
# train_images = train_images.reshape(-1, 28*28) / 255
test_images = test_images.reshape(-1, 28*28) / 255

# Load model
model = pk.load(open("DecisionTree/decisionTree.pkl","rb"))

# Show the result
predict_labels = model.predict(test_images)
print(metrics.classification_report(test_labels, predict_labels))
mat = confusion_matrix(test_labels, predict_labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')

# Show decision tree partialy with pdf
dot_data = tree.export_graphviz(model[-1], out_file=None,
                      max_depth=3) 
graph = graphviz.Source(dot_data)
graph.render('DecisionTree/minst')            

plt.show()