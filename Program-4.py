ip = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
countdict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for num in ip:
    for i in range(1, 10):
        if num % i == 0:
            countdict[i] += 1
print(countdict)
