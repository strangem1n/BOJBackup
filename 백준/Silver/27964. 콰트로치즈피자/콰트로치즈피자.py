n = int(input())
arr = list(input().split())
if n < 4:
    print('sad')
else:
    pizza = set()
    for cheese in arr:
        if cheese[-6:] == 'Cheese':
            pizza.add(cheese)
    if len(pizza) > 3:
        print('yummy')
    else:
        print('sad')
