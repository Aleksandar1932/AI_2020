import itertools


def get_visibility(skyscrapers_array):
    for i in range(0, len(skyscrapers_array)):
        for j in range(i, len(skyscrapers_array)):
            if skyscrapers_array[j] < skyscrapers_array[i]:
                skyscrapers_array[j] = 0
    return len([sk for sk in skyscrapers_array if sk != 0])


if __name__ == '__main__':
    n = int(input())
    all_permutations = list(itertools.permutations(range(1, n + 1)))
    for i in range(1, n + 1):
        count = 0
        for perm in all_permutations:
            if get_visibility(list(perm)) == i:
                count += 1
        print("For N = {}, count of possible permutations is {}".format(i, count))
