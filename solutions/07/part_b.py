from utils.runner import aoc_solution

@aoc_solution(day=7, part="B")
def solve_part_a(lines):
    lines = [list(line.replace("S", "1")) for line in lines]
    # Traverse and mark traversed split as X
    for i in range(len(lines)):
        if i == 0:
            continue
        line = lines[i]
        for j in range(len(line)):
            if line[j] == "^":
                for k in reversed(range(i)):
                    if lines[k][j] == "^" or lines[k][j] == "X":
                        break
                    if lines[k][j] == "1":
                        if j - 1 >= 0 and line[j - 1] == ".":
                            line[j - 1] = "1"
                        if j + 1 < len(line) and line[j + 1] == ".":
                            line[j + 1] = "1"
                        line[j] = "X"
                        break
    # Propagate value upwards 
    for i in reversed(range(len(lines))):
        line = lines[i]
        for j in range(len(line)):
            if line[j] != "X":
                continue
            value = 0
            if j - 1 >= 0 and line[j - 1].isdigit():
                value += int(line[j - 1])
            if j + 1 < len(line) and line[j + 1].isdigit():
                value += int(line[j + 1])
            for k in reversed(range(i)):
                if lines[k][j] == "^" or lines[k][j] == "X":
                    break
                if lines[k][j].isdigit():
                    lines[k][j] = str(value)
    
    for val in lines[0]:
        if val.isdigit():
            return val

if __name__ == "__main__":
    solve_part_a()