import csv

# Define functions to load data and preprocess it
def load_data(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def preprocess_data(data):
    headers = data[0]
    data = data[1:]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if j == 0:  # Converting the first column (e.g., age) to integer
                data[i][j] = int(data[i][j])
            elif j == len(data[i]) - 1:  # Handling label column
                # No need to convert, keep it as string
                pass
            else:  # Converting the rest of the columns to float
                data[i][j] = float(data[i][j])
    return headers, data

# Define a function to split data into features and labels
def split_data(data):
    features = []
    labels = []
    for row in data:
        features.append(row[:-1])  # All columns except the last one are features
        labels.append(row[-1])     # The last column is the label
    return features, labels

# Define a function to train a basic classification model
def train_model(features, labels):
    # Here, you can implement any classification algorithm of your choice
    # For simplicity, let's assume a basic rule-based model for demonstration purposes
    thresholds = [600, 10000, 2]  # Example thresholds for age, income, and number of dependents
    def predict(instance):
        age, income, dependents = instance
        if age >= thresholds[0] and income >= thresholds[1] and dependents <= thresholds[2]:
            return 'Approved'
        else:
            return 'Rejected'
    return predict

# Define a function to evaluate the model's accuracy
def evaluate_model(model, features, labels):
    correct_predictions = 0
    total_instances = len(features)
    for i in range(total_instances):
        prediction = model(features[i])
        if prediction == labels[i]:
            correct_predictions += 1
    accuracy = (correct_predictions / total_instances) * 100
    return accuracy

# Load and preprocess the data
file_path = r'C:\Users\AD\OneDrive\Desktop\CodeAlpha_project\credit.csv'  # Replace 'credit_data.csv' with the path to your dataset
data = load_data(file_path)
headers, preprocessed_data = preprocess_data(data)

# Split data into features and labels
features, labels = split_data(preprocessed_data)

# Train the model
model = train_model(features, labels)

# Evaluate the model
accuracy = evaluate_model(model, features, labels)
print("Model Accuracy:", accuracy)
