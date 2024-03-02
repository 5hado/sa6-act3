def find_maximum(numbers, compare_function):

    max = numbers[0]
   
    for num in numbers:
        max = compare_function(num, max)

    return max

numbers = [5, 8, 2, 10, 3]
max_number = find_maximum(numbers, lambda x, y: x if x > y else y)

print(max_number)