from utils.runner import aoc_solution

@aoc_solution(day=4, part="A")
def solve_part_a(lines):
    lines = list(lines)
    rollpapers = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != "@":
                continue
            next_rollpapers = 0
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
            if next_rollpapers < 4:
                rollpapers += 1
    return rollpapers

if __name__ == "__main__":
    solve_part_a()