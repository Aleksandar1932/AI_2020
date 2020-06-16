from collections import Counter

from sklearn.tree import DecisionTreeClassifier

dataset = [[6.3, 2.3, 4.4, 1.3, 2],
		   [6.4, 2.8, 5.6, 2.1, 0],
		   [5.1, 3.3, 1.7, 0.5, 1],
		   [5.1, 3.5, 1.4, 0.2, 1],
		   [4.6, 3.1, 1.5, 0.2, 1],
		   [5.8, 2.7, 5.1, 1.9, 0],
		   [5.5, 3.5, 1.3, 0.2, 1],
		   [5.7, 2.6, 3.5, 1.0, 2],
		   [5.0, 3.5, 1.3, 0.3, 1],
		   [6.3, 2.5, 5.0, 1.9, 0],
		   [6.2, 2.2, 4.5, 1.5, 2],
		   [5.0, 3.4, 1.6, 0.4, 1],
		   [5.7, 4.4, 1.5, 0.4, 1],
		   [4.9, 2.4, 3.3, 1.0, 2],
		   [4.4, 2.9, 1.4, 0.2, 1],
		   [5.5, 2.4, 3.7, 1.0, 2],
		   [5.6, 2.5, 3.9, 1.1, 2],
		   [5.6, 2.8, 4.9, 2.0, 0],
		   [4.8, 3.4, 1.6, 0.2, 1],
		   [5.6, 3.0, 4.5, 1.5, 2],
		   [6.0, 3.0, 4.8, 1.8, 0],
		   [6.3, 3.3, 4.7, 1.6, 2],
		   [4.8, 3.0, 1.4, 0.1, 1],
		   [7.9, 3.8, 6.4, 2.0, 0],
		   [4.9, 3.0, 1.4, 0.2, 1],
		   [4.3, 3.0, 1.1, 0.1, 1],
		   [6.8, 3.2, 5.9, 2.3, 0],
		   [5.6, 2.7, 4.2, 1.3, 2],
		   [5.2, 4.1, 1.5, 0.1, 1],
		   [6.2, 2.9, 4.3, 1.3, 2],
		   [6.5, 2.8, 4.6, 1.5, 2],
		   [5.4, 3.9, 1.3, 0.4, 1],
		   [5.8, 2.6, 4.0, 1.2, 2],
		   [5.4, 3.7, 1.5, 0.2, 1],
		   [4.5, 2.3, 1.3, 0.3, 1],
		   [6.3, 3.4, 5.6, 2.4, 0],
		   [6.2, 3.4, 5.4, 2.3, 0],
		   [5.7, 2.5, 5.0, 2.0, 0],
		   [5.8, 2.7, 3.9, 1.2, 2],
		   [6.4, 2.7, 5.3, 1.9, 0],
		   [5.1, 3.8, 1.6, 0.2, 1],
		   [6.3, 2.5, 4.9, 1.5, 2],
		   [7.7, 2.8, 6.7, 2.0, 0],
		   [5.1, 3.5, 1.4, 0.3, 1],
		   [6.8, 2.8, 4.8, 1.4, 2],
		   [6.1, 3.0, 4.6, 1.4, 2],
		   [5.5, 4.2, 1.4, 0.2, 1],
		   [5.0, 2.0, 3.5, 1.0, 2],
		   [7.7, 3.0, 6.1, 2.3, 0],
		   [5.1, 2.5, 3.0, 1.1, 2],
		   [5.9, 3.0, 5.1, 1.8, 0],
		   [7.2, 3.2, 6.0, 1.8, 0],
		   [4.9, 3.1, 1.5, 0.2, 1],
		   [5.7, 3.0, 4.2, 1.2, 2],
		   [6.1, 2.9, 4.7, 1.4, 2],
		   [5.0, 3.2, 1.2, 0.2, 1],
		   [4.4, 3.2, 1.3, 0.2, 1],
		   [6.7, 3.1, 5.6, 2.4, 0],
		   [4.6, 3.6, 1.0, 0.2, 1],
		   [5.1, 3.4, 1.5, 0.2, 1],
		   [5.2, 2.7, 3.9, 1.4, 2],
		   [6.4, 3.1, 5.5, 1.8, 0],
		   [7.4, 2.8, 6.1, 1.9, 0],
		   [4.9, 3.1, 1.5, 0.1, 1],
		   [5.0, 3.5, 1.6, 0.6, 1],
		   [6.7, 3.1, 4.7, 1.5, 2],
		   [6.4, 3.2, 5.3, 2.3, 0],
		   [6.3, 2.7, 4.9, 1.8, 0],
		   [5.8, 4.0, 1.2, 0.2, 1],
		   [6.9, 3.1, 5.4, 2.1, 0],
		   [5.9, 3.2, 4.8, 1.8, 2],
		   [6.6, 2.9, 4.6, 1.3, 2],
		   [6.1, 2.8, 4.0, 1.3, 2],
		   [7.7, 2.6, 6.9, 2.3, 0],
		   [5.5, 2.6, 4.4, 1.2, 2],
		   [6.3, 2.9, 5.6, 1.8, 0],
		   [7.2, 3.0, 5.8, 1.6, 0],
		   [6.5, 3.0, 5.8, 2.2, 0],
		   [5.4, 3.9, 1.7, 0.4, 1],
		   [6.5, 3.2, 5.1, 2.0, 0],
		   [5.9, 3.0, 4.2, 1.5, 2],
		   [5.1, 3.7, 1.5, 0.4, 1],
		   [5.7, 2.8, 4.5, 1.3, 2],
		   [5.4, 3.4, 1.5, 0.4, 1],
		   [4.6, 3.4, 1.4, 0.3, 1],
		   [4.9, 3.6, 1.4, 0.1, 1],
		   [6.7, 2.5, 5.8, 1.8, 0],
		   [5.0, 3.6, 1.4, 0.2, 1],
		   [6.7, 3.3, 5.7, 2.5, 0],
		   [4.4, 3.0, 1.3, 0.2, 1],
		   [6.0, 2.2, 5.0, 1.5, 0],
		   [6.0, 2.2, 4.0, 1.0, 2],
		   [5.0, 3.4, 1.5, 0.2, 1],
		   [5.7, 2.8, 4.1, 1.3, 2],
		   [5.5, 2.4, 3.8, 1.1, 2],
		   [5.1, 3.8, 1.9, 0.4, 1],
		   [6.9, 3.1, 5.1, 2.3, 0],
		   [5.6, 2.9, 3.6, 1.3, 2],
		   [6.1, 2.8, 4.7, 1.2, 2],
		   [5.5, 2.5, 4.0, 1.3, 2],
		   [5.5, 2.3, 4.0, 1.3, 2],
		   [6.0, 2.9, 4.5, 1.5, 2],
		   [5.1, 3.8, 1.5, 0.3, 1],
		   [5.7, 3.8, 1.7, 0.3, 1],
		   [6.7, 3.3, 5.7, 2.1, 0],
		   [4.8, 3.1, 1.6, 0.2, 1],
		   [5.4, 3.0, 4.5, 1.5, 2],
		   [6.5, 3.0, 5.2, 2.0, 0],
		   [6.8, 3.0, 5.5, 2.1, 0],
		   [7.6, 3.0, 6.6, 2.1, 0],
		   [5.0, 3.0, 1.6, 0.2, 1],
		   [6.7, 3.0, 5.0, 1.7, 2],
		   [4.8, 3.4, 1.9, 0.2, 1],
		   [5.8, 2.8, 5.1, 2.4, 0],
		   [5.0, 2.3, 3.3, 1.0, 2],
		   [4.8, 3.0, 1.4, 0.3, 1],
		   [5.2, 3.5, 1.5, 0.2, 1],
		   [6.1, 2.6, 5.6, 1.4, 0],
		   [5.8, 2.7, 4.1, 1.0, 2],
		   [6.9, 3.2, 5.7, 2.3, 0],
		   [6.4, 2.9, 4.3, 1.3, 2],
		   [7.3, 2.9, 6.3, 1.8, 0],
		   [6.3, 2.8, 5.1, 1.5, 0],
		   [6.2, 2.8, 4.8, 1.8, 0],
		   [6.7, 3.1, 4.4, 1.4, 2],
		   [6.0, 2.7, 5.1, 1.6, 2],
		   [6.5, 3.0, 5.5, 1.8, 0],
		   [6.1, 3.0, 4.9, 1.8, 0],
		   [5.6, 3.0, 4.1, 1.3, 2],
		   [4.7, 3.2, 1.6, 0.2, 1],
		   [6.6, 3.0, 4.4, 1.4, 2]]


def split_subset(s):
	s_x = [row[0:-1] for row in s]
	s_y = [row[-1] for row in s]
	return s_x, s_y


def count_votes(all_votes):
	count_dict = {}
	for i in range(0, 3):
		count_dict[i] = 0

	for vote in all_votes.values():
		count_dict[vote] += 1

	return count_dict


def calc_dominate_vote(votes_count):
	counter = Counter(votes_count.values())
	if counter.most_common(1)[0][1] == 1:
		return "unknown"
	return counter.most_common(1)[0][0]


def create_train_clf(t_x, t_y):
	clf = DecisionTreeClassifier(criterion='entropy', random_state=0)
	clf.fit(t_x, t_y)
	return clf


if __name__ == '__main__':
	# Split the dataset into three subsets
	first_train = dataset[0:int(0.3 * len(dataset))]
	second_train = dataset[int(0.3 * len(dataset)):int(0.6 * len(dataset))]
	third_train = dataset[int(0.6 * len(dataset)):]

	# Split each subset into X(features) and Y(classes)
	first_train_x, first_train_y = split_subset(first_train)
	second_train_x, second_train_y = split_subset(second_train)
	third_train_x, third_train_y = split_subset(third_train)

	# Init DecisionTreeClassifiers and train them
	clf1 = create_train_clf(first_train_x, first_train_y)
	clf2 = create_train_clf(second_train_x, second_train_y)
	clf3 = create_train_clf(third_train_x, third_train_y)

	# Get classifications for custom input
	x = input().split(', ')
	test_case = list(map(float, x[:-1])) + [int(x[-1])]

	votes = {}
	for (i, c) in enumerate([clf1, clf2, clf3]):
		votes[i] = c.predict([test_case[0:-1]])[0]

	# Print the results
	print("Glasovi: {}".format(count_votes(votes)))
	print("Predvidena klasa: {}".format(calc_dominate_vote(votes)))
