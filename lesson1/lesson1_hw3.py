# задание 3
n = input("n=")
n = int(n)

print(int(n) + int("%d%d" % (n, n)) + int("%d%d%d" % (n, n, n)))
