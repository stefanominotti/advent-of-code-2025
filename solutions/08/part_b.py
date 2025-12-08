from utils.runner import aoc_solution

@aoc_solution(day=8, part="B")
def solve_part_b(lines):
    boxes = []
    distances = {}
    for idx, line in enumerate(lines):
        x,y,z = map(int, line.strip().split(","))
        if len(boxes) != 0:
            for bidx, box in enumerate(boxes):
                bx, by, bz = box
                dist = ((x - bx)**2  + (y - by)**2  + (z - bz)**2)
                distances[(idx, bidx)] = dist
        boxes.append((x,y,z))

    box_groups = [idx for idx in range(len(boxes))]
    groups_map = {idx: 1 for idx in range(len(boxes))}
    groups_boxes = {idx: [idx] for idx in range(len(boxes))}
    result = 0
    sorted_distances_boxes = sorted(distances.items(), key=lambda item: item[1])
    while len(groups_map) > 1:
        if len(distances) == 0:
            break
        min_pair = sorted_distances_boxes.pop(0)[0]
        box_group1 = box_groups[min_pair[0]]
        box_group2 = box_groups[min_pair[1]]
        if box_group1 != box_group2:
            boxes_in_group2 = groups_boxes[box_group2]
            for bidx in boxes_in_group2:
                box_groups[bidx] = box_group1
                groups_boxes[box_group1].append(bidx)
            groups_map[box_group1] = groups_map[box_group1] + groups_map[box_group2]
            del groups_map[box_group2]
            del groups_boxes[box_group2]
            result = boxes[min_pair[0]][0] * boxes[min_pair[1]][0]
    
    return result

if __name__ == "__main__":
    solve_part_b()