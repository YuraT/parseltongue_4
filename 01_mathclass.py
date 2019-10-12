import sys
import math

def mean(numbers):
    return sum(numbers)/len(numbers)
def median(numbers):
    length = len(numbers)
    numbers.sort()
    median = (numbers[(length + 1) // 2] + numbers[((length + 1) // 2) - ((length + 1) % 2)]) / 2
    return median
def mode(numbers):
    max_count = 0
    for number in numbers:
        if numbers.count(number) > max_count:
            max_count = numbers.count(number)
    if max_count != 1:
        occurences_average = []
        for number in numbers:
            if numbers.count(number) == max_count and occurences_average.count(number) == 0:
                occurences_average.append(number)
        return mean(occurences_average)
    return "no mode"
def math_range(numbers):
    return max(numbers) - min(numbers)


def main():
    numbers = []
    for i in sys.argv[1:]:
        numbers.append(int(i))
    print("Min:", min(numbers))
    print("Max:", max(numbers))
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))
    print("Range:", math_range(numbers))

main()

print()
#using statistics
from statistics import mean
from statistics import median
from statistics import mode
numbers = []
for i in sys.argv[1:]:
    numbers.append(int(i))

print("Min:", min(numbers))
print("Max:", max(numbers))
print("Mean:", mean(numbers))
print("Median:", median(numbers))
print("Mode:", mode(numbers))
print("Range:", max(numbers) - min(numbers))