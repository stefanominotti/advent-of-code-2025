import re
from utils.runner import aoc_solution

@aoc_solution(day=6, part="A")
def solve_part_a(lines):
    values = []
    for line in lines:
        values.append(re.split(r' +', line.strip()))
    operators = values[-1]
    result = 0
    for idx in range(len(operators)):
        operator = operators[idx].strip()
        if operator == "+":
            partial_result = 0
        elif operator == "*":
            partial_result = 1
        for line in values[:-1]:
            number = int(line[idx].strip())
            if operator == "+":
                partial_result += number
            elif operator == "*":
                partial_result *= number
        result += partial_result
    return result

if __name__ == "__main__":
    solve_part_a()