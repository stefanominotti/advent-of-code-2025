from utils.runner import aoc_solution

@aoc_solution(day=1, part="A")
def solve_part_a(lines):
    current = 50
    password = 0
    for line in lines:
        direction = line[0]
        amount = int(line[1:])
        
        if direction == 'L':
            current = (current - amount + 100) % 100
        elif direction == 'R':
            current = (current + amount) % 100
            
        if current == 0:
            password += 1

    return password

if __name__ == "__main__":
    solve_part_a()