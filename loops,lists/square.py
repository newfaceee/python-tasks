sum_numbers, square_sum = 0, 0

while True:
    current_number = int(input())
    sum_numbers += current_number
    square_sum += pow(current_number, 2)
    if sum_numbers == 0:
        print(square_sum)
        break
