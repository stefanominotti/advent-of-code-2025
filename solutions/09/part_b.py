from utils.runner import aoc_solution

@aoc_solution(day=9, part="B")
def solve_part_b(lines):
    boxes = []
    for line in lines:
        x,y = map(int, line.strip().split(","))
        boxes.append((x,y))
    perimeter_x = {}
    perimeter_y = {}
    for idx in range(len(boxes)):
        x1, y1 = boxes[idx]
        if idx + 1 >= len(boxes):
            x2, y2 = boxes[0]
        else:
            x2, y2 = boxes[idx + 1]
        if x1 == x2:
            if x1 not in perimeter_x:
                perimeter_x[x1] = set()
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if y not in perimeter_y:
                    perimeter_y[y] = set()
                perimeter_y[y].add(x1)
                perimeter_x[x1].add(y)

        elif y1 == y2:
            if y1 not in perimeter_y:
                perimeter_y[y1] = set()
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if x not in perimeter_x:
                    perimeter_x[x] = set()
                perimeter_x[x].add(y1)
                perimeter_y[y1].add(x)

    areas = {}
    for idx, box in enumerate(boxes):
        bx, by = box
        for bidx, other_box in enumerate(boxes):
            if bidx == idx or bidx < idx:
                continue
            ox, oy = other_box
            area = (abs(bx-ox) + 1) * (abs(by-oy) + 1)
            areas[(idx, bidx)] = area

    sorted_areas_boxes = sorted(areas.items(), key=lambda item: item[1], reverse=True)
    for pair, area in sorted_areas_boxes:
        bx, by = boxes[pair[0]]
        ox, oy = boxes[pair[1]]
        is_valid = True
        if abs(bx - ox) >= abs(by - oy):
            for y in range(min(by, oy) + 1, max(by, oy)):
                if y in perimeter_y:
                    for x in perimeter_y[y]:
                        if min(bx, ox) < x < max(bx, ox):
                            is_valid = False
                            break
                if not is_valid:
                    break
            if is_valid:
                return area
        else:
            for x in range(min(bx, ox) + 1, max(bx, ox)):
                if x in perimeter_x:
                    for y in perimeter_x[x]:
                        if min(by, oy) < y < max(by, oy):
                            is_valid = False
                            break
                if not is_valid:
                    break
            if is_valid:
                return area
        
if __name__ == "__main__":
    solve_part_b()