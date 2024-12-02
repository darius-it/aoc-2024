def is_safe(row: list[int]) -> bool:
    if row != sorted(row) and row != sorted(row, reverse=True):
        return False
    
    for index, number in enumerate(row):
        if index + 1 >= len(row): break

        distance_of_entries = abs(int(number) - int(row[index + 1]))
        if distance_of_entries < 1 or distance_of_entries > 3:
            return False
            
    return True

def is_safe_2(row: list[int]):
    if is_safe(row): return True

    for index, _ in enumerate(row):
        row_copy = row.copy()
        del row_copy[index]

        if is_safe(row_copy):
            return True
        
    return False

def aoc2_p1(entries: list[list[int]]):
    safe_entries = 0
    
    for entry in entries:
        if is_safe_2(entry): safe_entries += 1

    print(f"Safe entries {safe_entries}")

def aoc2_p2(entries: list[list[int]]):
    safe_entries = 0

    for entry in entries:
        if is_safe_2(entry): safe_entries += 1

    print(f"Safe entries with damper: {safe_entries}")


if __name__ == "__main__":
    entries = []

    with open("input.txt") as file:
        for line in file.readlines():
            entries.append([int(num) for num in line.split()])  

    aoc2_p1(entries)
    aoc2_p2(entries)
