import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
import numpy as np

if __name__ == '__main__':
    # Read the data from the CSV file
    with open('cars_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)
        dataset_headers = dataset[0]
        dataset = dataset[1:]

    # Init encoder and train it
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    # Split the dataset into train and test sets
    train_set = dataset[0:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_x = encoder.transform(train_x)
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_x = encoder.transform(test_x)
    test_y = [row[-1] for row in test_set]

    # Init and train Decision Tree Classifier
    clf = DecisionTreeClassifier(criterion='entropy')
    clf.fit(train_x, train_y)

    # Print depth and number of leaves for the classifier
    print("Depth: {}".format(clf.get_depth()))
    print("Number of leaves: {}".format(clf.get_n_leaves()))

    # Measure the accuracy of the classifier using the test set
    correct_samples = 0
    for x, y in zip(test_x, test_y):
        if y == clf.predict([x])[0]:
            correct_samples += 1

    print("Accuracy: {}%".format(np.round(((correct_samples / len(test_set)) * 100), 3)))

    # Get the feature importances
    feature_importances = list(clf.feature_importances_)
    print("Feature importances: {}".format(feature_importances))

    most_important_feature = feature_importances.index(max(feature_importances))
    print("Most important feature(index): {}".format(most_important_feature))
    print("Most important feature(name): {}".format(dataset_headers[most_important_feature]))

    least_important_feature = feature_importances.index(min(feature_importances))
    print("Least important feature(index): {}".format(least_important_feature))
    print("Least important feature(name): {}".format(dataset_headers[least_important_feature]))

    # Removing the most important feature
    train_x_2 = [[row[i] for i in range(0, len(row)) if i != most_important_feature] for row in train_x]
    test_x_2 = [[row[i] for i in range(0, len(row)) if i != most_important_feature] for row in test_x]

    # Removing the least important feature
    train_x_3 = [[row[i] for i in range(0, len(row)) if i != least_important_feature] for row in train_x]
    test_x_3 = [[row[i] for i in range(0, len(row)) if i != least_important_feature] for row in test_x]

    # Classification after features removal
    clf2 = DecisionTreeClassifier(criterion='entropy')
    clf3 = DecisionTreeClassifier(criterion='entropy')

    clf2.fit(train_x_2, train_y)
    clf3.fit(train_x_3, train_y)

    print("Depth (removed most important feature): {}".format(clf2.get_depth()))
    print("Number of leaves (removed most important feature): {}".format(clf2.get_n_leaves()))

    print("Depth (removed least important feature): {}".format(clf3.get_depth()))
    print("Number of leaves (removed least important feature): {}".format(clf3.get_n_leaves()))

    # Measuring the accuracies of the new classifiers

    correct_samples = 0
    for x, y in zip(test_x_2, test_y):
        if y == clf2.predict([x])[0]:
            correct_samples += 1
    print("Accuracy (removed most important feature): {}%"
          .format(np.round(((correct_samples / len(test_set)) * 100), 3)))

    correct_samples = 0
    for x, y in zip(test_x_3, test_y):
        if y == clf3.predict([x])[0]:
            correct_samples += 1
    print("Accuracy (removed most important feature): {}%"
          .format(np.round(((correct_samples / len(test_set)) * 100), 3)))

