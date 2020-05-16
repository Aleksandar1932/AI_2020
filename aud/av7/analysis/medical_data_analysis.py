# Se pravi odreden broj na shuffles' na izvornoto podatocno mnozestvo, pri sekoj shuffle se zemaat razlicni udeli
# za trening mnozestvo, minimalniot i maksimalniot udel se dadeni vo soodvetni konstanti, i e zadadena rata na
# zgolemuvanje na intervalot. Pri sekoj shuffle se zema poedinecno tocnost za sekoj udel, i potoa za sekoj udel
# imame onolku tocnosti kolku sto e brojot za shuffles, pa se pravi statistika na nivo na udel.
#
# Kako sto e zadadeno momentalno 100 pati se pravi shuffle na podatocnoto mnozestvo, i vo sekoj shuffle se zema
# najmalku 50% za trening mnozestvo, a najmnogu 80% za trening mnozestvo, i pritoa ratata na zgolemuvanje e 10, pa
# se zemaat 50%, 60%, 70%, 80% za trening mnozestva i za sekoe od niv poedinecno se presmetuva tocnost.
#
# - dMIN_MAX: absolutna razlika megju minimalnata i maksimanlnata tocnost za konkretniot udel vo razlicnite shuffles
#   (delta)

import csv
import math
from sklearn.naive_bayes import GaussianNB
from random import shuffle as shuf
import numpy as np

NUM_OF_SHUFFLES = 150  # Kolku pati da izvrsi shuffle na podatocnoto mnozestvo
TRAIN_SET_MIN_RATIO = 50  # Minimalen procent na trening mnozestvo od celoto podatocno mnozestvo
TRAIN_SET_MAX_RATIO = 90  # Maksimalen procent na trening mnozestvo od celoto podatocno mnozestvo
TRAIN_SET_RATIO_INCREMENT = 10  # Rata na inkrement na procentot za trening mnozestvoto
DECIMALS_ROUND = 2  # Na kolku decimali da se zakruzuvaat presmetkite

if __name__ == '__main__':
    total_accuracies = {}
    for iteration in range(0, NUM_OF_SHUFFLES):
        accuracies = {}
        for ratio in range(TRAIN_SET_MIN_RATIO, TRAIN_SET_MAX_RATIO, TRAIN_SET_RATIO_INCREMENT):
            TRAIN_SET_RATIO = ratio / 100
            with open("medical_data_shuff2.csv") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                dataset = list(csv_reader)
                shuf(dataset)
                dataset = [[int(el) for el in row] for row in dataset]  # Converting features from string to integers

                # Dividing the data into train set and test set
                train_set = dataset[0:math.ceil(TRAIN_SET_RATIO * len(dataset))]
                test_set = dataset[math.ceil(TRAIN_SET_RATIO * len(dataset)):]

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

                accuracies["{}%".format(TRAIN_SET_RATIO * 100)] = ((accuracy / len(test_set)) * 100)
            total_accuracies[iteration] = accuracies

    # Statistics - print
    # Za lesen copy-paste vo excel
    total_accuracies_flatten = [list(individual_acc.values()) for individual_acc in total_accuracies.values()]
    data_headers = list(total_accuracies[0].keys())
    # for stat in total_accuracies_flatten:
    #     print("{}".format(stat))

    ratio_accuracies = {}
    for i in range(0, len(total_accuracies_flatten[0])):
        ratio_accuracies[data_headers[i]] = [acc[i] for acc in total_accuracies_flatten]

    print("Data was shuffled: {} times, the test set ratio ranges from {} to {} with step of {}\n"
          .format(NUM_OF_SHUFFLES, TRAIN_SET_MIN_RATIO, TRAIN_SET_MAX_RATIO, TRAIN_SET_RATIO_INCREMENT))
    for i in range(0, len(ratio_accuracies.keys())):
        row_arr = np.array(list(ratio_accuracies.values())[i])
        print("--- TRAIN SET RATIO: {} ---\n\tMIN: {}\n\tMAX: {}\n\tAVERAGE: {}\n\tSTDEV: {}\n\tdMIN_MAX: {}"
            .format(
            list(ratio_accuracies.keys())[i],
            np.round(np.min(row_arr), DECIMALS_ROUND),
            np.round(np.max(row_arr), DECIMALS_ROUND),
            np.round(np.average(row_arr), DECIMALS_ROUND),
            np.round(np.std(row_arr), DECIMALS_ROUND),
            np.round(np.abs(np.min(row_arr) - np.max(row_arr))), DECIMALS_ROUND)
        )
