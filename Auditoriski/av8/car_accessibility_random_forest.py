import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
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

    for estims in range(10, 150, 10):
        # Init and train Random Forest Classifier
        clf = RandomForestClassifier(n_estimators=estims, criterion='entropy')
        clf.fit(train_x, train_y)

        # Measure the accuracy of the classifier using the test set
        correct_samples = 0
        for x, y in zip(test_x, test_y):
            if y == clf.predict([x])[0]:
                correct_samples += 1

        print("Accuracy ({} trees): {}%".format(estims, np.round(((correct_samples / len(test_set)) * 100), 3)))
