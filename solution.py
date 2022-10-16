def countingValleys(steps, path):

    pos = 0
    pos_lst = [pos]
    for letter in path:
        if letter == 'D':
            pos -= 1
            pos_lst.append(pos)
        elif letter == 'U':
            pos += 1
            pos_lst.append(pos)

    valleys = 0

    for i in range(0, len(pos_lst)-1):
        if pos_lst[i] == 0:
            if pos_lst[i+1] == -1:
                valleys += 1

    return valleys
