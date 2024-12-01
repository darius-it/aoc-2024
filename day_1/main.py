def aoc1_p1(left: list[str], right: list[str]):
    left.sort()
    right.sort()

    total_sum = 0
    for i in range(0, len(left)):
        total_sum += abs(int(left[i]) - int(right[i]))

    print(f"Result of Part 1: {total_sum}")

def aoc1_p2(left: list[str], right: list[str]):
    right_occurences = {}

    for entry in right:
        if entry in right_occurences.keys():
            right_occurences[entry] += 1
        else:
            right_occurences[entry] = 1

    sim_score = 0
    for num in left:
        if num in right_occurences.keys():
            sim_score += (int(num) * int(right_occurences[num]))
        # skip adding 0 times something

    print(f"Similarity score: {sim_score}")

if __name__ == "__main__":
    left_side_lines = []
    right_side_lines = []

    with open("input.txt") as file:
        for line in file.readlines():
            sides = line.split()
            left_side_lines.append(sides[0])
            right_side_lines.append(sides[1])

    aoc1_p1(left_side_lines, right_side_lines) # part 1
    aoc1_p2(left_side_lines, right_side_lines) # part 2