# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, 
# у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

    #  for example for i = 0 and n = 5, bushes[i - len(bushes)] = bushes[-5] = bushes[0]
    #  so, bushes[i - len(bushes) + 1] = bushes[i + 1], but we do not get "out of array" error
    #  python support negative indexes and i exploited it
    #  0 1 2 3 4
from random import randint

n = int(input("введите кол-во кустов: "))
bushes = [randint(0, 10) for _ in range(n)]
print(*bushes)

biggest = bushes[-1] + bushes[0] + bushes[1]
#  debug text
print("[0]", bushes[-1], bushes[0], bushes[1], "biggest is", biggest)
for i in range(len(bushes))[1:]:  #  starting from index 1 because we found first one as biggest
    sum = bushes[i - 1] + bushes[i] + bushes[i - len(bushes) + 1]
    biggest = (sum if sum > biggest else biggest)
    #  debug text
    print(f"[{i}]", bushes[i - 1], bushes[i], bushes[i - len(bushes) + 1], "sum is", sum, "biggest is", biggest)
print("answer is", biggest)