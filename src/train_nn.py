'''
    Train Nueral Network
    
    This file contains functions related to training neural networks using tensorflow.
    Tutorials and links that the specific functions are based off of (ie. stackoverflow, github, etc) 
    will be provided for tensorflow-specific functions used.
    
    For an overview of Tensorflow neural networks see the tutorials here: 
    https://www.tensorflow.org/get_started/get_started
'''

import tensorflow as tf
import numpy as np
from tensorflow.contrib.learn.python import SKCompat


#Constants
CLASSES = 3 #the number of possible classifications
HIDDEN_UNITS = [10, 20, 10] #the topology of the neural network

#inputs: data_size is an int describing the number of features (window width_size^2)
#       data is the features
#       labels is the correct label
#outputs: returns the trained classifier
#This file uses a basic Tensorflow classifier rather than the Tensorflow sess() feature
#tutorial for this type of model can be found at https://www.tensorflow.org/get_started/tflearn
def train_base(data_size, data, labels):
    print("training model")
    
    
    # Specify that all features have real-value data
    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=data_size)]


    #create a neural network based on constants
    classifier = SKCompat(tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                                hidden_units= HIDDEN_UNITS,
                                                n_classes= CLASSES,
                                                model_dir="/tmp/test_model"))

    # Fit model.
    classifier.fit(x=data, y=labels)

    accuracy_score = classifier.evaluate(x=X_test, y=Y_test)["accuracy"]
    print('Accuracy: {0:f}'.format(accuracy_score))
    #return classifier