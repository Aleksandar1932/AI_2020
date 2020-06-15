if __name__ == '__main__':
    state_1 = "123*****"
    num_steps = 0
    for i in range(0, len(state_1)):
        if state_1[i] != '*':
            fields = (len(state_1) - int(state_1[i])) - i
            num_steps += int(fields / 2) + fields % 2

    print(num_steps)
