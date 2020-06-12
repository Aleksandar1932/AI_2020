from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.callbacks import CSVLogger
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def read_dataset(file_path):
	""" Read the dataset and return the features and encoded classes

	:param file_path: path to the file that contains the dataset
	:type file_path: str
	:return: features and encoded classes
	:rtype: np.array, np.array
	"""
	features = []
	classes = []
	with open(file_path) as f:
		_ = f.readline()
		while True:
			line = f.readline().strip()
			if line == '':
				break
			parts = line.split(';')
			features.append(list(map(float, parts[:-1])))
			classes.append(one_hot_encoding(int(parts[-1])))
	return np.array(features), np.array(classes)


def one_hot_encoding(sample):
	""" Encodes the ranking into class (with one-hot encoding)
	bad quality -> [1, 0, 0]
	medium quality -> [0, 1, 0]
	good quality -> [0, 0, 1]

	:param sample: one ranking value
	:type sample: int
	:return: one-hot encoded class
	:rtype: list(int)
	"""
	if sample < 6:
		return [1, 0, 0]
	elif sample == 6:
		return [0, 1, 0]
	else:
		return [0, 0, 1]


def plot_graph_loss(file_name, model_name):
	""" Plots validation and train loss
	:param file_name: name of the csv file containing values for validation and train loss functions
	:type file_name: str
	:param model_name: name of the model
	:type model_name: str
	:return: None
	"""
	values = pd.read_table(file_name, sep=',')
	data = pd.DataFrame()
	data['epoch'] = list(values['epoch'].values + 1) + list(values['epoch'].values + 1)
	data['loss name'] = ['training'] * len(values) + ['validation'] * len(values)
	data['loss'] = list(values['loss'].values) + list(values['val_loss'].values)
	sns.set(style='darkgrid', context='poster', font='Verdana')
	f, ax = plt.subplots()
	sns.lineplot(x='epoch', y='loss', hue='loss name', style='loss name', dashes=False, data=data, palette='Set2')
	ax.set_ylabel('Loss')
	ax.set_xlabel('Epoch')
	ax.legend().texts[0].set_text('')
	plt.title(model_name)
	plt.show()


if __name__ == '__main__':
	features, classes = read_dataset("winequality-white.csv")
	train_x, train_y = (features[0:int(len(features) * 0.7)], classes[0:int(len(classes) * 0.7)])
	val_x, val_y = (features[int(len(features) * 0.7):int(len(features) * 0.8)],
					classes[int(len(classes) * 0.7):int(len(classes) * 0.8)])
	test_x, test_y = (features[int(len(features) * 0.8):], classes[int(len(classes) * 0.8):])

	model = Sequential()
	model.add(Dense(32, input_shape=(11,)))
	model.add(Dense(64, input_shape=(11,)))
	model.add(Dense(3))

	optimizer = Adam(lr=0.01)
	model.compile(optimizer=optimizer, loss=categorical_crossentropy, metrics=['accuracy'])
	csv_logger = CSVLogger('log.csv')
	history = model.fit(x=train_x, y=train_y, validation_data=(val_x, val_y), batch_size=128, epochs=500, verbose=1,
			  callbacks=[csv_logger])


	results = model.evaluate(test_x, test_y, batch_size=128)

	loss_train = history.history['accuracy']
	loss_val = history.history['val_accuracy']
	epochs = range(1, 501)
	plt.plot(epochs, loss_train, 'g', label='Training accuracy')
	plt.plot(epochs, loss_val, 'b', label='validation accuracy')
	plt.title('Training and Validation accuracy')
	plt.xlabel('Epochs')
	plt.ylabel('Accuracy')
	plt.legend()
	plt.show()
