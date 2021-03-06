#!/usr/bin/python

import sys
import pickle
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Load the dictionary containing the dataset
data_dict = pickle.load(open("final_project_dataset.pkl", "r") )

### Task 2: Remove outliers
from data_cleaning import clean_dataset
my_dataset = clean_dataset(data_dict)
### Task 3: Create new feature(s)
from feature_engineering import feature_engineering
my_dataset, feature_names = feature_engineering(my_dataset)
### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi', 'prop_shared_with_poi', 'total_payments', 
				'restricted_stock_deferred', 'prop_rest_stock', 
				'from_messages', 'deferral_payments', 'prop_exercised_stock', 
				'shared_receipt_with_poi', 'to_messages', 
				'from_poi_to_this_person', 'total_stock_value', 
				'from_this_person_to_poi']

data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from feature_scaling import SigmoidMinMaxScaler

clf = Pipeline([('scaler', SigmoidMinMaxScaler()),
	('knn', KNeighborsClassifier(n_neighbors=1))])


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)