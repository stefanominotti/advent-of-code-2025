from utils.runner import aoc_solution

@aoc_solution(day=7, part="A")
def solve_part_a(lines):
    lines = [list(line) for line in lines]
    result = 0
    for i in range(len(lines)):
        if i == 0:
            continue
        line = lines[i]
        for j in range(len(line)):
            if line[j] == "^":
                for k in reversed(range(i)):
                    if lines[k][j] == "^":
                        break
                    if lines[k][j] == "S":
                        if j - 1 >= 0 and line[j - 1] == ".":
                            line[j - 1] = "S"
                        if j + 1 < len(line) and line[j + 1] == ".":
                            line[j + 1] = "S"
                        result += 1
                        break
    return result

if __name__ == "__main__":
    solve_part_a()