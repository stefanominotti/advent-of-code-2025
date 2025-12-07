from utils.runner import aoc_solution

@aoc_solution(day=5, part="A")
def solve_part_a(lines):
    ranges = {}
    ingredients = []
    is_ingredient_section = False
    for line in lines:
        if line.strip() == "":
            is_ingredient_section = True
            continue
        if not is_ingredient_section:
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
        else:
            ingredients.append(line.strip())
    sorted_range_keys = sorted(ranges.keys())
    valid_ingredient_count = 0
    for i in ingredients:
        value = 0
        for key in sorted_range_keys:
            if key < int(i):
                value += ranges[key]
            elif value > 0:
                valid_ingredient_count += 1
                break
    return valid_ingredient_count

if __name__ == "__main__":
    solve_part_a()