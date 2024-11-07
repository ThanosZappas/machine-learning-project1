import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from logistic_regression import LogisticRegressionEP34
import time

# Load the dataset
dataset = datasets.load_breast_cancer()

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(dataset.data)

# Initialize variables to store accuracies
accuracies = []

# Start the timer
start_time = time.time()

# Perform 20 iterations
for _ in range(20):
    print(f"Iteration {_ + 1}")
    # Split the scaled dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(scaled_data, dataset.target, train_size=0.70)

    # Initialize the LogisticRegressionEP34 model
    model = LogisticRegressionEP34(lr=0.01)

    # Train the model
    model.fit(X_train, y_train, show_line=False, batch_size=64, iterations=10000)

    # Calculate accuracy on the test set
    predictions = model.predict(X_test) >= 0.5
    accuracy = np.mean(predictions == y_test)
    accuracies.append(accuracy)
    print(f"Model accuracy: {accuracy * 100:.2f}%")
    print()

# End the timer
end_time = time.time()

# Calculate mean and standard deviation of accuracies
mean_accuracy = np.mean(accuracies)
std_accuracy = np.std(accuracies)

# Calculate total execution time
execution_time = end_time - start_time

# Print results
print(f"Mean accuracy: {mean_accuracy * 100:.2f}%")
print(f"Standard deviation of accuracy: {std_accuracy * 100:.2f}%")
print(f"Total execution time: {execution_time:.2f} seconds")

# Print system specifications
print(f"Processor: 11th Gen Intel(R) Core(TM) i3-1115G4 @ 3.00GHz") #11th Gen Intel(R) Core(TM) i3-1115G4 @ 3.00GHz
print(f"Memory: 12 GB")