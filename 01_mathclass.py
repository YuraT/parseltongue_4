import sys
import math

def mean(numbers):
    return sum(numbers)/len(numbers)
def median(numbers):
    numbers = numbers.sort()
    median = (numbers[len(numbers) // 2] + numbers[(len(numbers) // 2) + (len(numbers) % 2)]) / 2
    return median

def main():
    numbers = sys.argv[1:]
    print("Min:", min(numbers))
    print("Max:", max(numbers))
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    

main()