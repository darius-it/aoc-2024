def aoc1_p1():
    left = []
    right = []

    with open("input.txt") as file:
        for line in file.readlines():
            sides = line.split()
            left.append(sides[0])
            right.append(sides[1])

    left.sort()
    right.sort()

    total_sum = 0
    for i in range(0, len(left)):
        total_sum += abs(int(left[i]) - int(right[i]))

    print(f"Result of Part 1: {total_sum}")

def aoc1_p2():
    left = []
    right = []
    right_occurences = {}

    with open("input.txt") as file:
        for line in file.readlines():
            sides = line.split()
            left.append(sides[0])
            right.append(sides[1])

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
    aoc1_p1() # part 1
    aoc1_p2() # part 2