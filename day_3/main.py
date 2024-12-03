import re

def get_mul_result(mul_string: str):
    sides = mul_string.split(",")
    left_num = int(sides[0].replace("mul(", "").strip())
    right_num = int(sides[1].replace(")", "").strip())

    print("mul: ", mul_string, " left num: ", left_num, " right num: ", right_num)    

    return left_num * right_num

def aoc3_p1(entries: list[str]):
    match_valid_mul_operations = r"mul\(\d+,\s?\d+\)"

    sum = 0
    for entry in entries:
        matches = re.findall(match_valid_mul_operations, entry)

        for match in matches:
            sum += get_mul_result(match)

    print(f"Sum of valid muls: {sum}")

def get_muls_from_string(input: str):
    match_valid_mul_operations = r"mul\(\d+,\s?\d+\)"

    sum = 0
    matches = re.findall(match_valid_mul_operations, input)

    for match in matches:
        sum += get_mul_result(match)

    return sum

def aoc3_p2(entry: str):
    to_skip = r"don't\(\)(.*?)(do\(\)|$)"
    sum = get_muls_from_string(re.sub(to_skip, ' ', entry))
    
    print(f"Sum of valid muls: {sum}")


if __name__ == "__main__":
    entries = []

    with open("input.txt") as file:
        entries = file.readlines()

    string = "" # put it all on one line
    for line in entries:
        string += line.strip()
    
    aoc3_p1(entries)
    aoc3_p2(string)



