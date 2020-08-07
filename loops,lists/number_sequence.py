numbers = [int(x) for x in input().split()]
searching_number = int(input())

indexes = []
for index in range(len(numbers)):
    if numbers[index] == searching_number:
        indexes.append(index)

if len(indexes) == 0:
    print('Отсутствует')
else:
    print(' '.join(map(str, indexes)))
