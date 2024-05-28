# Import dependencies
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import tensorflow as tf

# Load the data
application_df = pd.read_csv("https://static.bc-edx.com/data/dl-1-2/m21/lms/starter/charity_data.csv")

# Drop the non-beneficial ID columns, 'EIN' and 'NAME'.
application_df = application_df.drop(columns=['EIN', 'NAME'])

# Determine the number of unique values in each column.
unique_counts = application_df.nunique()

# Look at APPLICATION_TYPE value counts for binning
application_type_counts = application_df.APPLICATION_TYPE.value_counts()

# Replace rare application types with "Other"
application_types_to_replace = application_type_counts[application_type_counts < 500].index.tolist()
application_df.APPLICATION_TYPE = application_df.APPLICATION_TYPE.replace(application_types_to_replace, 'Other')

# Look at CLASSIFICATION value counts for binning
classification_counts = application_df.CLASSIFICATION.value_counts()

# Replace rare classifications with "Other"
classifications_to_replace = classification_counts[classification_counts < 1000].index.tolist()
application_df.CLASSIFICATION = application_df.CLASSIFICATION.replace(classifications_to_replace, 'Other')

# Convert categorical data to numeric with `pd.get_dummies`
application_df = pd.get_dummies(application_df)

# Split our preprocessed data into our features and target arrays
X = application_df.drop(columns=['IS_SUCCESSFUL'])
y = application_df.IS_SUCCESSFUL

# Split the preprocessed data into a training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Create a StandardScaler instance
scaler = StandardScaler()

# Fit the StandardScaler
X_scaler = scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train_scaled.shape[1],)),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train_scaled, y_train, epochs=100)

# Evaluate the model
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f'Loss: {loss}, Accuracy: {accuracy}')

# Save the model
model.save('AlphabetSoupCharity.h5')
