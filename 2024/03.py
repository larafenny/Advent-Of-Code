import re
import os


project_path = os.path.dirname(os.path.abspath((__file__)))

with open(project_path + "/input/03", 'r') as content:
    text = content.read()


# First part
multiplications = re.findall(r"mul\((\d+),\s*(\d+)\)", text)
total_result = sum(int(tuple[0]) * int(tuple[1]) for tuple in multiplications)
print(total_result)  # 184511516

# Second part
enabled = True  # Status to check if the multiplication is to be considered or not
total_result = 0
regex = r"(do\(\)|don\'t\(\)|mul\((\d+),\s*(\d+)\))"

multiplications = re.finditer(regex, text)
for match in multiplications:
    regex_match = match.group(0)

    if regex_match == "do()":
        enabled = True
    elif regex_match == "don't()":
        enabled = False
    else:
        if enabled:
            x = int(match.group(2))
            y = int(match.group(3))
            total_result += x * y

print(total_result)  # 90044227
