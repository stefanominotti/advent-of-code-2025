import math
from utils.runner import aoc_solution

@aoc_solution(day=1, part="B")
def solve_part_b(lines):
    current = 50
    password = 0
    for line in lines:
        direction = line[0]
        amount = int(line[1:])

        password += amount // 100
        amount = amount % 100

        starting_current = current
        if direction == 'L':
            current = current - amount
            if current < 0:
                current = 100 + current
                if starting_current != 0:
                    password += 1
            elif current == 0:
                password += 1
        elif direction == 'R':
            current = current + amount
            if current >= 100:
                current = current - 100
                password += 1

        current = current
    return password

if __name__ == "__main__":
    solve_part_b()