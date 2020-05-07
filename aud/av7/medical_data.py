import csv
import math
from sklearn.naive_bayes import GaussianNB

if __name__ == '__main__':
    with open("medical_data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)[1:]
        dataset = [[int(el) for el in row] for row in dataset]  # Converting features from string to integers

        # Dividing the data into train set and test set
        train_set = dataset[0:math.ceil(0.8 * len(dataset))]
        test_set = dataset[math.ceil(0.8 * len(dataset)):]

        # Dividing into X and Y, data - features and belonging class
        X = [train_set[i][:-1] for i in range(0, len(train_set))]
        Y = [train_set[i][-1] for i in range(0, len(train_set))]

        # Init Gaussian Naive Bayes Classifier because of the continuity of the data, and train it
        clf = GaussianNB()
        clf.fit(X, Y)

        # Testing the accuracy of the model
        accuracy = 0
        for row in test_set:
            prediction = clf.predict([row[:-1]])
            if prediction[0] == row[-1]:
                accuracy += 1

        print("ACCURACY = {}".format((accuracy / len(test_set))))
