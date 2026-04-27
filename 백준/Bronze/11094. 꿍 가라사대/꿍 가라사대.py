n = int(input())
for _ in range(n):
    command = input()
    if command[:10] == "Simon says":
        print(command[10:])