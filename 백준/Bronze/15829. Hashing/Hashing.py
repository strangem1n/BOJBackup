l = int(input())
text = list(input())
result = 0
count = 0
for i in text:
    a = ord(i) - 96
    result += a * (31 ** count)
    count += 1
mod_result = result % 1234567891
print(mod_result)