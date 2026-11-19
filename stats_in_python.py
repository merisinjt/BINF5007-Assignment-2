import sys

import math

def load_data(filepath: str, column: int) -> tuple[list, int]:
    
    numbers = []
    count = 0

    with open(filepath, 'r') as infile:
        for line_number, line in enumerate(infile, start=1):

            values = line.strip().split("\t")
            count = count + 1

            try:
                num = values[column]

            except IndexError:
                print("Invalid column")
                sys.exit()

            try:
                num = float(num)

                if not math.isnan(num):
                    numbers.append(num)

            except ValueError:
                continue

    return numbers, count


def calculate_average(numbers: list) -> float:
    
    total = sum(numbers)
    avg = total / len(numbers)

    return avg

def calculate_maximum(numbers: list) -> float:
    
    maximum = max(numbers)

    return maximum

def calculate_minimum(numbers: list) -> float:
    
    minimum = min(numbers)

    return minimum
  

def calculate_variance(numbers: list) -> float:
    
    avg = calculate_average(numbers)
    total = 0

    for num in numbers:
        total = total + (num - avg) ** 2

    var = total / (len(numbers)-1)

    return var

def calculate_std_dev(numbers:list)->float:
    var = calculate_variance(numbers)
    std_dev = math.sqrt(var)

    return std_dev

def calculate_median(number:list)->float:
    sorted_numbers = sorted(number)
    n = len(sorted_numbers)

    middle = n // 2

    if n % 2 == 0:
        med = (sorted_numbers[middle - 1] +
               sorted_numbers[middle]) / 2
    else:
        med = sorted_numbers[middle]

    return med

# First file and Column: 3
filepath1 = "C:/Users/Merisin/Downloads/data_file.txt"

numbers, count = load_data(filepath1, 3)

print("Average = %.3f" % count)
print("Average = %.3f" % len(numbers))
print("Average = %.3f" % calculate_average(numbers))
print("Maximum = %.3f" % calculate_maximum(numbers))
print("Minimum = %.3f" % calculate_minimum(numbers))
print("Variance = %.3f" % calculate_variance(numbers))
print("Std Dev = %.3f" % calculate_std_dev(numbers))
print("Median = %.3f" % calculate_median(numbers))



# Second file and Column: 3
filepath2 = "C:/Users/Merisin/Downloads/data_file2.txt"

numbers, count = load_data(filepath2, 3)
print("Average = %.3f" % count)
print("Average = %.3f" % len(numbers))
print("Average = %.3f" % calculate_average(numbers))
print("get_max_and_min = %.3f" % get_max_and_min(numbers))
print("Variance = %.3f" % calculate_variance(numbers))
print("Std Dev = %.3f" % calculate_std_dev(numbers))
print("Median = %.3f" % calculate_median(numbers))

# Third file and Column: 3
filepath3 = "C:/Users/Merisin/Downloads/data_file3.txt"

numbers, count = load_data(filepath3, 3)

print("Average = %.3f" % count)
print("Average = %.3f" % len(numbers))
print("Average = %.3f" % calculate_average(numbers))

# Third file and Column: 10
numbers, count = load_data(filepath3, 10)

# Third file and Column: 1
numbers, count = load_data(filepath3, 1)

print("Average = %.3f" % count)
print("Average = %.3f" % len(numbers))
print("Average = %.3f" % calculate_average(numbers))
print("get_max_and_min = %.3f" % get_max_and_min(numbers))
print("Variance = %.3f" % calculate_variance(numbers))
print("Std Dev = %.3f" % calculate_std_dev(numbers))
print("Median = %.3f" % calculate_median(numbers))


# Second file and Column: 4
numbers, count = load_data(filepath2, 4)
print("Average = %.3f" % count)
print("Average = %.3f" % len(numbers))
print("Average = %.3f" % calculate_average(numbers))
print("get_max_and_min = %.3f" % get_max_and_min(numbers))
print("Variance = %.3f" % calculate_variance(numbers))
print("Std Dev = %.3f" % calculate_std_dev(numbers))
print("Median = %.3f" % calculate_median(numbers))

