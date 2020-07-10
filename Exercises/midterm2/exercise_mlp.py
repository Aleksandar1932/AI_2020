from Exercises.midterm2.exercise_nb import split_subset, split_dataset, calculate_accuracy, read_dataset
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import recall_score, precision_score, accuracy_score

if __name__ == '__main__':
    # Read the dataset
    dataset = read_dataset()

    # Split the dataset into train and test subsets
    train, test = split_dataset(dataset)

    # Split each subset into x and y
    train_x, train_y = split_subset(train)
    test_x, test_y = split_subset(test)

    # Init classifier and train it
    mlp_clf = MLPClassifier(hidden_layer_sizes=(15,), activation='relu', learning_rate_init=0.009, max_iter=500,
                            random_state=0)
    mlp_clf.fit(train_x, train_y)

    # Make predictions on the test set
    predictions_mlp = mlp_clf.predict(test_x)

    # Calculate metrics
    accuracy_mlp = accuracy_score(test_y, predictions_mlp)
    recall_mlp = recall_score(test_y, predictions_mlp, pos_label="good")
    precision_mlp = precision_score(test_y, predictions_mlp, pos_label="good")

    # Print metrics
    print(f"MLP Accuracy = {accuracy_mlp}")
    print(f"MLP Recall = {recall_mlp}")
    print(f"MLP Precision = {precision_mlp}")