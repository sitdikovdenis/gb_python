# задание 4
n = input("n=")

max_num = n[0]
i = 0
while i < len(n):
    if n[i] > max_num:
        max_num = n[i]
    i += 1

print(max_num)
