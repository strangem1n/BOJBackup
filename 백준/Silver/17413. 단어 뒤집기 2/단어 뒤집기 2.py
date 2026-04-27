S = input()
stack = [''] * 100000
top = -1
tag = False
for i in range(len(S)):
    if S[i] == "<":
        if top == -1:
            tag = True
            print(S[i], end="")
        else:
            while top > -1:
                print(stack[top], end="")
                top -= 1
            tag = True
            print(S[i], end="")
    elif tag is True:
        print(S[i], end="")
        if S[i] == ">":
            tag = False
    else:
        if S[i] == " ":
            while top > -1:
                print(stack[top], end="")
                top -= 1
            print(" ", end="")
        else:
            top += 1
            stack[top] = S[i]
while top > -1:
    print(stack[top], end="")
    top -= 1
