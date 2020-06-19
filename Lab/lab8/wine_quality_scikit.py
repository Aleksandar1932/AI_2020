from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier


def read_dataset(path):
	ds = []
	with open(path) as f:
		_ = f.readline()
		while True:
			line = f.readline().strip()
			if line == '':
				break
			parts = line.split(';')
			features = [float(p) for p in parts[:-1]]
			class_label = one_hot_encoding(int(parts[-1]))
			parts = features + [class_label]
			ds.append(parts)
	return ds


def one_hot_encoding(sample):
	if sample < 6:
		return [1, 0, 0]
	elif sample == 6:
		return [0, 1, 0]
	else:
		return [0, 0, 1]


def split_dataset(ds):
	tr = ds[:int(len(ds) * 0.7)]
	v = ds[int(len(ds) * 0.7):int(len(ds) * 0.8)]
	te = ds[int(len(ds) * 0.8):]
	return tr, v, te


def split_subset(subset):
	subset_x = [row[:-1] for row in subset]
	subset_y = [row[-1] for row in subset]
	return subset_x, subset_y


def calculate_accuracy(pred, exact):
	correct_samples = 0
	for (p, e) in zip(pred, exact):
		if list(p) == list(e):
			correct_samples += 1
	return correct_samples / len(pred)


if __name__ == '__main__':
	dataset = read_dataset('/home/aleksandar/PycharmProjects/AI_2020/Auditoriski/av10/winequality-white.csv')
	train, val, test = split_dataset(dataset)
	train_x, train_y = split_subset(train)
	val_x, val_y = split_subset(val)
	test_x, test_y = split_subset(test)

	clf = MLPClassifier(hidden_layer_sizes=(22,), activation='tanh', learning_rate_init=0.001, max_iter=600,
						random_state=0)

	clf.fit(train_x, train_y)

	# Print accuracy on test set
	print("Accuracy on test set: {}".format(
		calculate_accuracy(clf.predict(test_x), test_y)
	))
