import csv
from sklearn.neural_network import MLPClassifier


def read_dataset():
    with open('winequality.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        data = list(csv_reader)[1:]
    data = [[float(row[i]) if i != (len(row) - 1) else row[i] for i in range(0, len(row))] for row in data]
    return data


def divide_sets(data):
    good_classes = [row for row in data if row[-1] == 'good']
    bad_classes = [row for row in data if row[-1] == 'bad']

    train_set = good_classes[:int(len(good_classes) * 0.7)] + bad_classes[:int(len(bad_classes) * 0.7)]
    val_set = good_classes[int(len(good_classes) * 0.7):int(len(good_classes) * 0.8)] \
              + bad_classes[int(len(bad_classes) * 0.7):int(len(bad_classes) * 0.8)]
    test_set = good_classes[int(len(good_classes) * 0.8):] + bad_classes[int(len(bad_classes) * 0.8):]

    return train_set, val_set, test_set


def split_set(set):
    set_x = [row[:-1] for row in set]
    set_y = [row[-1] for row in set]

    return set_x, set_y


if __name__ == '__main__':
    dataset = read_dataset()  # Read the99 dataset
    train_set, val_set, test_set = divide_sets(dataset)  # Split the dataset into train, validation and test sets

    train_set_x, train_set_y = split_set(train_set)  # Split into X and Y
    val_set_x, val_set_y = split_set(val_set)  # Split into X and Y
    test_set_x, test_set_y = split_set(test_set)  # Split into X and Y

    # Init neural networks
    clf1 = MLPClassifier(5, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    clf2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    clf3 = MLPClassifier(100, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    # Train neural networks
    clf1.fit(train_set_x, train_set_y)
    clf2.fit(train_set_x, train_set_y)
    clf3.fit(train_set_x, train_set_y)

    # Find the classifier with best performance on the validation set
    final_classifier = None
    max_acc = 0

    for i, c in enumerate([clf1, clf2, clf3]):
        val_predictions = c.predict(val_set_x)
        val_acc = 0

        for true, pred in zip(val_set_y, val_predictions):
            if true == pred:
                val_acc += 1

        val_acc = val_acc / len(val_set)

        print(f'Classifier {i} has accuracy of {val_acc} on the validation set')

        if val_acc > max_acc:
            max_acc = val_acc
            final_classifier = c

    # Evaluate the classifier performing best on the validation set on the test set
    acc = 0
    test_prediction = final_classifier.predict(test_set_x)

    for true, pred in zip(test_set_y, test_prediction):
        if true == pred:
            acc += 1

    acc = acc / len(test_set)
    print(f'The accuracy with the final classifier on the test set is {acc}')