
list = [24,28,14,11,8,9,9,16,31,65,58,65,71,67,88,76,57,59,43,39,36,49,40,38]


for i in range(len(list)):
    for n in range(60):
        with open("test.csv", 'a') as file:
            print(list[i], file=file)