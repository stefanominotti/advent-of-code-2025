from utils.runner import aoc_solution

@aoc_solution(day=3, part="A")
def solve_part_a(lines):
    total_joltage = 0
    for line in lines:
        max_index_map = {}
        for index in range(len(line)):
            value = line[index]
            if value not in max_index_map or index > max_index_map[value]:
                max_index_map[value] = index
        sorted_line = sorted(line, reverse=True)
        for i in range(len(sorted_line)):
            joltage = None
            for j in range(len(sorted_line)):
                if i == j:
                    continue
                i_val = sorted_line[i]
                j_val = sorted_line[j]
                if i_val == j_val or max_index_map[j_val] > max_index_map[i_val]:
                    joltage = i_val + j_val
                    break
            if joltage is not None:
                total_joltage += int(joltage)
                break

    return total_joltage

if __name__ == "__main__":
    solve_part_a()