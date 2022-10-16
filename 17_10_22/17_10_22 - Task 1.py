def sum(num):
    s = 0
    for i in range(len(num)):
        s += int(num[i])
    return s


kol = 0

for n in range(1, 100):
    r = bin(n)[2:]
    r = str(r)
    r += str(sum(r) % 2)
    r += str(sum(r) % 2)
    r = int(r, 2)
    if 20 <= r <= 50:
        kol += 1

print(kol)