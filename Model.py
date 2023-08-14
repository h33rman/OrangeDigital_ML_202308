import pandas as pd
import warnings
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle  # Using pickle instead of joblib

# Suppress warnings
warnings.filterwarnings("ignore")

# Load the dataset
data = pd.read_csv("data/2healthcare_stroke_dataset.csv")
df = data.drop(columns=['id']).dropna(axis=0)

# Define features and target
X = df.drop('stroke', axis=1)
y = df['stroke']

# Use ColumnTransformer to handle both encoding and normalization
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['age', 'avg_glucose_level', 'bmi']),
        ('cat', OneHotEncoder(drop='first'), ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'])
    ])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Preprocess the data
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# Train a Random Forest model
clf = RandomForestClassifier(n_estimators=50, max_depth=None, min_samples_leaf=1, min_samples_split=2, random_state=1)
clf.fit(X_train_processed, y_train)

# Evaluate the model (optional)
accuracy = clf.score(X_test_processed, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model and preprocessor for future use using pickle
with open('random_forest_model.pkl', 'wb') as model_file:
    pickle.dump(clf, model_file)

with open('preprocessor.pkl', 'wb') as preprocessor_file:
    pickle.dump(preprocessor, preprocessor_file)
