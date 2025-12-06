from utils.runner import aoc_solution

@aoc_solution(day=2, part="B")
def solve_part_b(lines):
    input = next(lines)
    ranges = input.split(",")

    result = 0
    for range_ in ranges:
        start_str, end_str = range_.split("-")

        start = int(start_str)
        end = int(end_str)

        for number in range(start, end + 1):
            number_str = str(number)
            if is_invalid(number_str):
                result += number

    return result

def is_invalid(number_str):
    valid_substring_lengths = [i for i in range(1, len(number_str)) if len(number_str) % i == 0]
    for length in valid_substring_lengths:
        substring = number_str[:length]
        repetitions = len(number_str) // length
        if substring * repetitions == number_str:
            return True
    return False

if __name__ == "__main__":
    solve_part_b()