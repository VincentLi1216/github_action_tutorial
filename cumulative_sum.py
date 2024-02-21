
def calculate_cumulative_sum(numbers):
    cumulative_sum = 0
    for number in numbers:
        cumulative_sum += number
        print(f"Cumulative sum is now: {cumulative_sum}")

numbers = [1, 2, 3, 4, 5]
calculate_cumulative_sum(numbers)
