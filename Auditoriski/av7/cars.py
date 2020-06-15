import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
import math

if __name__ == '__main__':
    with open("car.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)[1:]

        # Init encoder and train it
        encoder = OrdinalEncoder()
        encoder.fit([dataset[i][:-1] for i in range(0, len(dataset))])

        # Dividing the data into train set and test set
        train_set = dataset[0:math.ceil(0.7 * len(dataset))]
        test_set = dataset[math.ceil(0.7 * len(dataset)):]

        # Encoding the characteristic of the train set
        X = encoder.transform([train_set[i][:-1] for i in range(0, len(train_set))])
        Y = [train_set[i][-1] for i in range(0, len(train_set))]

        # Init Categorical Naive Bayes Classifier and train it with the train data
        clf = CategoricalNB()
        clf.fit(X, Y)

        # Testing the accuracy of the model
        test_set_x = encoder.transform([test_set[i][:-1] for i in range(0, len(test_set))])
        accuracy = 0
        for i in range(0, len(test_set)):
            prediction = clf.predict([test_set_x[i]])
            if prediction[0] == test_set[i][-1]:
                accuracy += 1

        print("ACCURACY = {}".format(accuracy / len(test_set)))

        # Testing the model with custom input data
        entry = [el for el in input("Enter your data:").split(' ')]
        entry = encoder.transform([entry])
        print(clf.predict(entry))
