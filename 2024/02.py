import os


project_path = os.path.dirname(os.path.abspath(__file__))

distances = [1, 2, 3]
total_safe = 0


def check_safe_level(numbers):
    is_ordered = numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True)
    if not is_ordered:
        return False

    diffs = [abs(numbers[index] - numbers[index + 1]) for index in range(len(numbers) - 1)]
    return set(diffs).issubset(set(distances))


def check_modify_level(numbers):
    for i in range(len(numbers)):
        new_numbers = numbers[:i] + numbers[i+1:]
        if check_safe_level((new_numbers)):
            return True
    return False


with open(project_path + '/input/02', 'r') as content:
    for row in content:
        row = row.replace('\n', '').split(' ')
        numbers = [int(number) for number in row]

        if check_safe_level(numbers) or check_modify_level(numbers):
            total_safe += 1
        else:
            print(f"{numbers}")
    print(total_safe)  # 516
