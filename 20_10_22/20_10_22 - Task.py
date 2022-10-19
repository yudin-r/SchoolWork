s = ('2' * 2) + ('3' * 15) + ('4' * 10)
sum = 0

while ("42" in s) or ("32" in s):
    if "42" in s:
        s = s.replace("42", "51", 1)
    else:
        s = s.replace("32", "61", 1)

# print(s) debug
for i in range(len(s)):
    sum += int(s[i])

print(sum)  # ans = 89
