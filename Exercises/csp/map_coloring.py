from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    cities = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    colors = ["red", "green", "blue"]

    problem.addVariables(cities, colors)

    adjacent_cities = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["SA", "Q", "V"],
        "V": ["SA", "NSW"]
    }

    for (city, neighbours) in adjacent_cities.items():
        for neighbour in neighbours:
            problem.addConstraint(AllDifferentConstraint(), [city] + [neighbour])

    print(problem.getSolution())
