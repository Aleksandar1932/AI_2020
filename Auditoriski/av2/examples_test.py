# Testing mapping and list comprehension
from functools import reduce

if __name__ == "__main__":
    list1 = [-1, -2, -3, 1, 2, 3, 4, 5, 6]
    list_result = map(lambda x: x * 10, filter(lambda x: x > 0, list1))
    print(list(list_result))

    sum = reduce(lambda x,y: x + y, map(lambda x: x * 10, filter(lambda x: x > 0, list1)))
    

