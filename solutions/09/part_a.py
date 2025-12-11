from utils.runner import aoc_solution

@aoc_solution(day=9, part="A")
def solve_part_a(lines):
    boxes = []
    for line in lines:
        x,y = map(int, line.strip().split(","))
        boxes.append((x,y))
    max_dist = None
    max_dist_pair = None
    for idx, box in enumerate(boxes):
        bx, by = box
        for bidx, other_box in enumerate(boxes):
            if bidx == idx:
                continue
            ox, oy = other_box
            dist = abs(bx - ox)**2 + abs(by - oy)**2
            if max_dist is None or dist >= max_dist:
                max_dist = dist
                max_dist_pair = (idx, bidx)
    return (abs(boxes[max_dist_pair[0]][0] - boxes[max_dist_pair[1]][0]) + 1) * (abs(boxes[max_dist_pair[0]][1] - boxes[max_dist_pair[1]][1]) + 1)

if __name__ == "__main__":
    solve_part_a()