def swap(digit, pos1, pos2):
    digit[pos1 - 1], digit[pos2 - 1] = digit[pos2 - 1], digit[pos1 - 1]

    return digit

List = [23, 65, 19, 90]
pos1 = 1
pos2 = 3

result = swap(List, pos1, pos2)
print("List after swapping:", result)








