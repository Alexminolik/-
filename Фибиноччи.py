#Последовательнось Фибиначчи до n-го числа
n = int(input())
l = [0, 1]

for i in range(0, 20+1):
    l.append(l[i]+l[i+1])
print(l)
