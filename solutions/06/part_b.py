import re
from utils.runner import aoc_solution

@aoc_solution(day=6, part="B")
def solve_part_a(lines):
    lines = list(lines)
    groups = []
    current_group = []
    for idx in reversed(range(len(lines[0]))):
        current_column = []
        for line in lines:
            current_column.append(line[idx].strip())
        current_group.append(current_column)
        if current_column[-1] != "":
            groups.append(current_group)
            current_group = []

    result = 0
    for group in groups:
        operator = group[-1][-1]
        if operator == "+":
            group_result = 0
        elif operator == "*":
            group_result = 1
        for column in group:
            number_str = "".join(column[:-1])
            if number_str == "" and operator == "*":
                number = 1
            elif number_str == "" and operator == "+":
                number = 0
            else:
                number = int(number_str)
            if operator == "+":
                group_result += number
            elif operator == "*":
                group_result *= number
        result += group_result
    return result

if __name__ == "__main__":
    solve_part_a()