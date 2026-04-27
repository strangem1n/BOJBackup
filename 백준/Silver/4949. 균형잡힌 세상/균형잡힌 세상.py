def test(string):
    arr = [0]
    for i in range(len(string)):
        if string[i] == '(':
            arr.insert(0, 'small')
        elif string[i] == ')':
            if arr[0] == 'small':
                arr.pop(0)
            else:
                return 'no'
        elif string[i] == '[':
            arr.insert(0, 'large')
        elif string[i] == ']':
            if arr[0] == 'large':
                arr.pop(0)
            else:
                return 'no'
    if len(arr) != 1:
        return 'no'
    else:
        return 'yes'


while True:
    case = input()
    if case == '.':
        break
    else:
        print(test(case))
