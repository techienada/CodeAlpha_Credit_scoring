import csv

# Define a function to load the dataset from a CSV file
def load_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        
        # Print headers for debugging
        headers = reader.fieldnames
        print("Headers:", headers)
        
        for row in reader:
            # Print each row for debugging
            print("Row:", row)
            row['Symptoms 1'] = int(row['Symptoms 1'])
            row['Symptoms 2'] = int(row['Symptoms 2'])
            row['Symptoms 3'] = int(row['Symptoms 3'])
            row['disease'] = int(row['disease'])
            dataset.append({
                'symptom1': row['Symptoms 1'],
                'symptom2': row['Symptoms 2'],
                'symptom3': row['Symptoms 3'],
                'disease': row['disease']
            })
    return dataset

# Define a function to train the model
def train_model(dataset):
    model = {}
    total_samples = len(dataset)
    num_disease = sum(1 for data in dataset if data['disease'] == 1)
    prior_disease = num_disease / total_samples
    model['prior_disease'] = prior_disease
    symptom_counts = {'symptom1': {}, 'symptom2': {}, 'symptom3': {}}
    for data in dataset:
        for symptom in symptom_counts:
            if data['disease'] == 1:
                symptom_counts[symptom][data[symptom]] = symptom_counts[symptom].get(data[symptom], 0) + 1
    model['symptom_counts'] = symptom_counts
    return model

# Define a function to predict disease likelihood
def predict(model, new_data):
    likelihood_disease = model['prior_disease']
    for symptom in model['symptom_counts']:
        likelihood_disease *= model['symptom_counts'][symptom].get(new_data[symptom], 0) / sum(model['symptom_counts'][symptom].values())
    return likelihood_disease

# Example usage
file_path = r"C:\Users\AD\OneDrive\Desktop\CodeAlpha_project\task2.csv"
dataset = load_dataset(file_path)
new_patient = {'symptom1': 1, 'symptom2': 0, 'symptom3': 1}
trained_model = train_model(dataset)
likelihood = predict(trained_model, new_patient)
likelihood_percentage = likelihood * 100
print("Likelihood of disease: {:.2f}%".format(likelihood_percentage))
