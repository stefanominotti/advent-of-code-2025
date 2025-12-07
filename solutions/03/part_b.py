from utils.runner import aoc_solution

@aoc_solution(day=3, part="B")
def solve_part_b(lines):
    total_joltage = 0
    for line in lines:
        joltage = ''
        while len(joltage) < 12:
            value, index = find_next(line, 12 - len(joltage))
            joltage += value
            line = line[index+1:]
        total_joltage += int(joltage)
    return total_joltage

def find_next(line, desired_length):
    index_map = {}
    for index in range(len(line)):
        value = line[index]
        if value not in index_map:
            index_map[value] = [index]
        else:
            index_map[value].append(index)
    sorted_line = sorted(line, reverse=True)
    for i in range(len(sorted_line)):
        value = sorted_line[i]
        valid_index = None
        for index in index_map[value]:
            if len(line) - index - desired_length >= 0:
                valid_index = index
                break
        if valid_index is not None:
            return value, index

if __name__ == "__main__":
    solve_part_b()