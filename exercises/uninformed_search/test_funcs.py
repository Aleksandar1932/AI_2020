from exercises.uninformed_search.snake import move_snake_right

if __name__ == '__main__':
    n = int(input())
    zeleni_jabolki = tuple(tuple(map(int, input().split(','))) for _ in range(n))
    m = int(input())
    crveni_jabolki = tuple(tuple(map(int, input().split(','))) for _ in range(m))

    snake_initial = ((0, 5), (0, 4), (0, 3))

    print(move_snake_right(snake_initial, zeleni_jabolki, crveni_jabolki))
