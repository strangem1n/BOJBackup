while True:
    n = int(input())
    text = f"{n} = "
    test = 0
    
    if n == -1:
        break
    else:
        for i in range(1, n):
            if n % i == 0:
                text += f"{i} + "
                test += i
        if n == test:
            print(text[:-2])
        else:
            print(f"{n} is NOT perfect.")