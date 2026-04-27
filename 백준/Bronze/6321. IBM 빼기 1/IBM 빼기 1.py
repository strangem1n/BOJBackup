n = int(input())
for tc in range(1, n+1):
    computer = input()
    print(f"String #{tc}")
    for i in range(len(computer)):
        next_char = ord(computer[i]) + 1
        if next_char == 91:
            print(chr(65), end="")
        else:
            print(chr(next_char), end="")
    print("\n")
