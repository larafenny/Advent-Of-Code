import os
from collections import Counter


project_path = os.path.dirname(os.path.abspath((__file__)))

# --------------- First part ------------------
# What is the total distance between your lists?
with open(project_path + "/input/01") as content:
    left_list = []
    right_list = []
    counter = 0
    for pair in content:
        splitted_string = pair.split("   ")
        left_list.append(int(splitted_string[0]))
        right_list.append(int(splitted_string[1]))

    total_distance = sum(abs(l - r) for l, r in zip(sorted(left_list), sorted(right_list)))

    print(f"The total distance is: {total_distance}")  # 2580760

# --------------- Second part ------------------
# What is their similarity score?
    right_occurrence_list = Counter(right_list)
    similarity_score = sum(number * right_occurrence_list[number] for number in left_list)

    print(f"The similarity score is: {similarity_score}")  # 25358365
