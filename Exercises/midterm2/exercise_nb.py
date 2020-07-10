import csv

from sklearn.naive_bayes import GaussianNB


def read_dataset():
    with open('../../Auditoriski/av9/winequality.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        data = list(csv_reader)[1:]
    data = [[float(row[i]) if i != (len(row) - 1) else row[i] for i in range(0, len(row))] for row in data]
    return data


def split_dataset(data):
    # Training = 70% from each class
    # Test = the other 30% from each class
    good_class = [row for row in data if row[-1] == "good"]
    bad_class = [row for row in data if row[-1] == "bad"]

    return (good_class[:int(0.7 * len(good_class))] + bad_class[:int(0.7 * len(bad_class))],
            good_class[int(0.7 * len(good_class)):] + bad_class[int(0.7 * len(bad_class)):])


def split_subset(subset):
    return [row[:-1] for row in subset], [row[-1] for row in subset]


def calculate_accuracy(predicted, exact):
    correct_samples = 0
    for (p, e) in zip(predicted, exact):
        if p == e:
            correct_samples += 1

    return correct_samples / len(predicted)


if __name__ == '__main__':
    # Read the dataset
    dataset = read_dataset()

    # Split the dataset into train and test subsets
    train, test = split_dataset(dataset)

    # Split each subset into x and y
    train_x, train_y = split_subset(train)
    test_x, test_y = split_subset(test)

    # Init classifier and train it
    nb_clf = GaussianNB()
    nb_clf.fit(train_x, train_y)

    # Make predictions on the test set
    predictions = nb_clf.predict(test_x)

    # Calculate accuracy on the test set
    accuracy = calculate_accuracy(predictions, test_y)

    # Print
    print("Accuracy on test set is: {}".format(accuracy))
