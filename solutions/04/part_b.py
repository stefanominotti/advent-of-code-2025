from utils.runner import aoc_solution

@aoc_solution(day=4, part="B")
def solve_part_b(lines):
    lines = list(lines)
    rollpapers = 0
    to_check = set()
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "@":
                to_check.add((i, j))
    while len(to_check) > 0:
        new_to_check = set()
        removed = set()
        for i, j in to_check:
            if lines[i][j] != "@":
                continue
            next_rollpapers = 0
            adjacent_positions = set()
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni = i + di
                    nj = j + dj
                    if ni < 0 or ni >= len(lines) or nj < 0 or nj >= len(line):
                        continue
                    if lines[ni][nj] == "@":
                        next_rollpapers += 1
                        adjacent_positions.add((ni, nj))
            if next_rollpapers < 4:
                removed.add((i, j))
                rollpapers += 1
                for ni, nj in adjacent_positions:
                        if (ni, nj) not in removed:
                            new_to_check.add((ni, nj))
        to_check = new_to_check
        for i, j in removed:
            lines[i] = lines[i][:j] + "X" + lines[i][j+1:]
    return rollpapers

if __name__ == "__main__":
    solve_part_b()