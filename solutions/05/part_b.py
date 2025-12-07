from utils.runner import aoc_solution

@aoc_solution(day=5, part="B")
def solve_part_a(lines):
    ranges = {}
    for line in lines:
        if line.strip() == "":
            break
        start_str, end_str = line.split("-")
        start = int(start_str)
        end = int(end_str) + 1
        if start not in ranges:
            ranges[start] = 1
        else:
            ranges[start] += 1
        if end not in ranges:
            ranges[end] = -1
        else:
            ranges[end] -= 1
    sorted_range_keys = sorted(ranges.keys(), reverse=True)
    valid_ingredient_count = 0
    value = 0
    for key in sorted_range_keys:
        previous_value = value
        value += ranges[key]
        if previous_value >= 0 and value < -0:
            valid_ingredient_count += key
        elif previous_value < 0 and value >= 0:
            valid_ingredient_count -= key

    return valid_ingredient_count

if __name__ == "__main__":
    solve_part_a()