while True:
    column = int(input())
    if column == 0:
        break
    else:
        encrypted_message = input()
        length = len(encrypted_message)
        matrix = []
        for i in range(0, length, column*2):
            matrix.append(encrypted_message[i:i+column])
            matrix.append(encrypted_message[i+column*2-1:i+column-1:-1])
        
        if (length // column) % 2 == 1:
            matrix.pop()
        
        matrix_length = len(matrix)
        
        for h in range(column):
            for j in range(matrix_length):
                print(matrix[j][h], end="")
        print("\n", end="")