import pandas as pd
import warnings
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import joblib

# Ignore all warnings for cleaner output
warnings.filterwarnings("ignore")

# Load the dataset
data = pd.read_csv("data/healthcare-dataset-stroke-data.csv")

# Preprocess the dataset
df = data.drop(columns=['id']).dropna(axis=0)

X = df.drop('stroke', axis=1)
y = df['stroke']

# One-hot encode categorical variables
encode = OneHotEncoder(sparse=False, handle_unknown='ignore')
X_encoded = encode.fit_transform(X)

# Normalize the data
norm = StandardScaler(with_mean=False)
X_norm = norm.fit_transform(X_encoded)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2, random_state=1)

def evaluation(model):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Model Performance:\n")
    print(classification_report(y_test, y_pred))

    # Optionally save the model, encoder, and normalizer for future use
    joblib.dump(model, 'knn_model.pkl')
    joblib.dump(encode, 'encoder.pkl')
    joblib.dump(norm, 'normalizer.pkl')

knn = KNeighborsClassifier(n_neighbors=100)
evaluation(knn)
