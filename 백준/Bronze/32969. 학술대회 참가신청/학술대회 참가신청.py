article = list(input().split())
for a in article:
    if a.lower() in ["bigdata", "public", "society"]:
        print("public bigdata")
        break
else:
    print("digital humanities")