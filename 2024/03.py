import re
import os


project_path = os.path.dirname(os.path.abspath((__file__)))

with open(project_path + "/input/03", 'r') as content:
    text = content.read()

multiplications = re.findall(r"mul\((\d+),\s*(\d+)\)", text)
total_result = sum(int(tuple[0]) * int(tuple[1]) for tuple in multiplications)
