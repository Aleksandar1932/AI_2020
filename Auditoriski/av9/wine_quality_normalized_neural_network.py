from Auditoriski.av9.wine_quality_neural_network import read_dataset, divide_sets, split_set
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neural_network import MLPClassifier

if __name__ == '__main__':
    dataset = read_dataset()  # Read the dataset
    train_set, val_set, test_set = divide_sets(dataset)  # Split the dataset into train, validation and test sets

    train_set_x, train_set_y = split_set(train_set)  # Split into X and Y
    val_set_x, val_set_y = split_set(val_set)  # Split into X and Y
    test_set_x, test_set_y = split_set(test_set)  # Split into X and Y

    # Init scalers and train them
    scaler1 = StandardScaler()  # Init standard scaler
    scaler1.fit(train_set_x)
    scaler2 = MinMaxScaler()   # Init min max scaler
    scaler2.fit(train_set_x)

    # Init neural networks and train them
    clf1 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    clf2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    clf3 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    clf1.fit(train_set_x, train_set_y)  # Train the neural network without any scaling
    clf2.fit(scaler1.transform(train_set_x), train_set_y)  # Train the neural network with standard scaling
    clf3.fit(scaler2.transform(train_set_x), train_set_y)  # Train the neural network with standard scaling

    # Find the performance on the validation set without scaling
    val_acc1 = 0
    val_predictions = clf1.predict(val_set_x)

    for true, pred in zip(val_set_y, val_predictions):
        if true == pred:
            val_acc1 += 1

    val_acc1 = val_acc1 / len(val_set_y)
    print(f'Without normalization the accuracy on the validation set is: {val_acc1}')

    # Find the performance on the validation set with standard scaling
    val_acc2 = 0
    val_predictions = clf2.predict(scaler1.transform(val_set_x))

    for true, pred in zip(val_set_y, val_predictions):
        if true == pred:
            val_acc2 += 1

    val_acc2 = val_acc2 / len(val_set_y)
    print(f'With standard normalization the accuracy on the validation set is: {val_acc2}')

    # Find the performance on the validation set with min-max scaling
    val_acc3 = 0
    val_predictions = clf3.predict(scaler2.transform(val_set_x))

    for true, pred in zip(val_set_y, val_predictions):
        if true == pred:
            val_acc3 += 1

    val_acc3 = val_acc3 / len(val_set_y)
    print(f'With min-max scaling the accuracy on the validation set is: {val_acc3}')






