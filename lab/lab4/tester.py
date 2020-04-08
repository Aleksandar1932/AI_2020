if __name__ == '__main__':
    # AllDifferent in block:
    for v_delim in range(0, 9, 3):
        for h_delim in range(0, 9, 3):
            for coord in [((y * 9) + x) for x in range(h_delim, h_delim + 3) for y in range(v_delim, v_delim + 3)]:
                print(coord)
