from utils.runner import aoc_solution

@aoc_solution(day=2, part="A")
def solve_part_a(lines):
    input = next(lines)
    ranges = input.split(",")

    result = 0
    for range_ in ranges:
        start_str, end_str = range_.split("-")

        start = int(start_str)
        end = int(end_str)

        for number in range(start, end + 1):
            number_str = str(number)
            if number_str[:len(number_str)//2] == number_str[len(number_str)//2:]:
                result += number

    return result

if __name__ == "__main__":
    solve_part_a()