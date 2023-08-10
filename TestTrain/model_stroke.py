import pandas as pd
import numpy as np
import warnings

# Ignorer tous les avertissements
warnings.filterwarnings("ignore")

# take the dataset
data = pd.read_csv("data/healthcare-dataset-stroke-data.csv")

# preprocessing
df = data.copy()
df = df.dropna(axis=0)
df = df.drop(columns='id')

df_test = df.copy()

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split


X = df_test.drop('stroke', axis = 1)
y = df_test['stroke']

encode = OneHotEncoder(sparse=False, handle_unknown='ignore')
X_encoded = encode.fit_transform(X=X)

norm = StandardScaler(with_mean=False)
X_norm = norm.fit_transform(X_encoded)


# modeling
X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2, random_state=1)

"""from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC"""

from sklearn.neighbors import KNeighborsClassifier

"""from sklearn.metrics import confusion_matrix, classification_report, f1_score, recall_score
from sklearn.model_selection import learning_curve"""

def evaluation(model):

    model.fit(X_train, y_train)
    print(model.score(X_test, y_test))
    ypred = model.predict(X_test)

knn = KNeighborsClassifier(n_neighbors=100)
evaluation(knn)