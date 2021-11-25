#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import plot_confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


# In[2]:


def logistic_regression(X_train, y_train, X_test, y_test):
    
    # Logistic regression: accuracy score
    classification = LogisticRegression(random_state=42, max_iter=10000)
    classification.fit(X_train, y_train)
    
    print('1) Logistic regression score:', classification.score(X_test, y_test))
    
    # Confusion metrix
    print('2) Confustion metrix:')
    predictions = classification.predict(X_test)
    print(confusion_matrix(y_test, predictions))
    
    # Plot confusion metrix
    print('3) Confustion metrix plot: see bottom plot')
    cf_matrix = confusion_matrix(y_test, predictions)
    group_names = ['True A', 'False A', 'False A',
               'False B', 'True B', 'False B',
               'False C', 'False C', 'True C']

    group_counts = ["{0:0.0f}".format(value) for value in cf_matrix.flatten()]
    group_percentages = ["{0:.2%}".format(value) for value in cf_matrix.flatten()/np.sum(cf_matrix)]
    labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(group_names,group_counts,group_percentages)]
    labels = np.asarray(labels).reshape(3,3)
    print(sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues'))
    
    print('4) Classification report:')
    print(classification_report(y_test, classification.predict(X_test)))


# In[ ]:


def knn_classifier(X_train, y_train, X_test, y_test, K_value):
    model = KNeighborsClassifier(n_neighbors= K_value)
    model.fit(X_train, y_train)
    
    print('1) KNN Classifier accuracy score:')
    y_pred = model.predict(X_test)
    print(metrics.accuracy_score(y_test, y_pred))
    
    print('2) Confusion metrix:')
    predictions_knn = model.predict(X_test)
    print(confusion_matrix(y_test, predictions_knn))

    # Plot confusion metrix
    print('3) Confustion metrix plot: see bottom plot')
    cf_matrix = confusion_matrix(y_test, predictions_knn)
    group_names = ['True A', 'False A', 'False A',
               'False B', 'True B', 'False B',
               'False C', 'False C', 'True C']

    group_counts = ["{0:0.0f}".format(value) for value in cf_matrix.flatten()]
    group_percentages = ["{0:.2%}".format(value) for value in cf_matrix.flatten()/np.sum(cf_matrix)]
    labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(group_names,group_counts,group_percentages)]
    labels = np.asarray(labels).reshape(3,3)
    print(sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues'))
    
    
    print('4) Classification report:') 
    print(classification_report(y_test, model.predict(X_test)))


# In[ ]:


def random_forest(X_train, y_train, X_test, y_test):
    clf = RandomForestClassifier(max_depth = 5, random_state = 0)
    clf.fit(X_train, y_train)
    print('1) Random forest accuracy score:', clf.score(X_test, y_test))
    

def random_forest_param(X_train, y_train, X_test, y_test, max_feat, min_sam_leaf,min_sam_split, max_dep, n_est):
    clf = RandomForestClassifier(random_state=0, 
                                 max_features = max_feat, 
                                 min_samples_leaf = min_sam_leaf,
                                 min_samples_split= min_sam_split,
                                 max_depth = max_dep,
                                 n_estimators = n_est)
    # accuracy score
    clf.fit(X_train, y_train)
    print('1) Random forest accuracy score:', clf.score(X_test, y_test))

    # cross validation score
    cross_val_scores = cross_val_score(clf, X_train, y_train, cv=10)
    print('2) Cross validation score:', np.mean(cross_val_scores))

    #Confusion metrix
    predictions = clf.predict(X_test)
    print('3) Confusion metrix:')
    print(confusion_matrix(y_test, predictions))

    # Plot confusion metrix
    print('4) Confustion metrix plot: see bottom plot')
    cf_matrix = confusion_matrix(y_test, predictions)
    group_names = ['True A', 'False A', 'False A',
               'False B', 'True B', 'False B',
               'False C', 'False C', 'True C']

    group_counts = ["{0:0.0f}".format(value) for value in cf_matrix.flatten()]
    group_percentages = ["{0:.2%}".format(value) for value in cf_matrix.flatten()/np.sum(cf_matrix)]
    labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(group_names,group_counts,group_percentages)]
    labels = np.asarray(labels).reshape(3,3)
    print(sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues'))
    
    #classification report
    print('5) Classification report:') 
    print(classification_report(y_test, predictions))


# In[ ]





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




