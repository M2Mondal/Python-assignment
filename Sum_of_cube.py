def sum_of_squares(list):
    
    square_sum = 0
    for num in list:
        square_sum += num ** 2
    return square_sum

numbers_str = input("Enter a list of numbers, separated by commas: ")
numbers_list = [int(num) for num in numbers_str.split(",")]

squares_sum = sum_of_squares(numbers_list)
print(squares_sum)