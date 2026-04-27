word = input()
trigger = input()
stack = [''] * 1000000
top = -1
for i in range(len(word)):
    top += 1
    stack[top] = word[i]
    if top > len(trigger)-2:
        for j in range(len(trigger)):
            if stack[top-j] != trigger[-(1+j)]:
                break
        else:
            top -= len(trigger)
if top == -1:
    result = "FRULA"
else:
    result = ''.join(stack[:top+1])
print(result)
