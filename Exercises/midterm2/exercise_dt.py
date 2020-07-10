from Exercises.midterm2.exercise_nb import split_subset, split_dataset, calculate_accuracy, read_dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
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
    dt_clf = DecisionTreeClassifier(criterion='entropy', random_state=0)
    dt_clf.fit(train_x, train_y)

    rf_clf = RandomForestClassifier(criterion='entropy', n_estimators=50)
    rf_clf.fit(train_x, train_y)

    # Make predictions on the test set
    predictions_dt = dt_clf.predict(test_x)
    predictions_rf = rf_clf.predict(test_x)

    # Calculate accuracy on the test set
    accuracy_dt = calculate_accuracy(predictions_dt, test_y)

    # Feature importances
    feature_importances = list(dt_clf.feature_importances_)
    most_important_feature = feature_importances.index(max(feature_importances))
    least_important_feature = feature_importances.index(min(feature_importances))

    # Print
    print("Accuracy with DecisionTree: {}".format(accuracy_dt))
    print("Recall with DecisionTree: {}".format(recall_score(test_y, predictions_dt, pos_label="good")))
    print("Precision with DecisionTree: {}".format(precision_score(test_y, predictions_dt, pos_label="good")))
    print("Most important feature is: {}".format(most_important_feature))
    print("Least important feature is: {}".format(least_important_feature))

    print("Accuracy with RandomForest (50 trees): {}".format(accuracy_score(test_y, predictions_rf)))
    print("Recall with RandomForest (50 trees): {}".format(recall_score(test_y, predictions_rf, pos_label="good")))
    print("Precision with RandomForest (50 trees): {}".format(precision_score(test_y, predictions_rf, pos_label="good")))

    print("Most important feature is: {}".format(most_important_feature))
    print("Least important feature is: {}".format(least_important_feature))



