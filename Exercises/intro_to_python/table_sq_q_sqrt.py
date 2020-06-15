import math


def generate_table(a, b):
    table = {}
    if b < a:
        return table
    while a <= b:
        table[a] = (round(pow(a, 2), 5), round(pow(a, 3), 5), round(math.sqrt(a), 5))
        a = a + 1

    return table


if __name__ == "__main__":
    m = int(input())
    n = int(input())
    x = int(input())

    tablica = generate_table(m, n)

    if len(tablica) != 0 and x in tablica:
        print(f"{tablica[x]} ")

    else:
        print("nema podatoci")

    print(sorted(tablica.items()))
