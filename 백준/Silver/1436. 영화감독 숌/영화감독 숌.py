n = int(input())
movie = []

a = 665

while True:
    try:
        print(movie[n-1])
        break
    except IndexError:
        a += 1
        if "666" in str(a):
            movie.append(a)