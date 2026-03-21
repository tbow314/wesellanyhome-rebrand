import json

with open(r'C:\Users\tbow3\.gemini\antigravity\brain\ab5b8aee-5d0b-4e83-9394-e0e4af5e12d2\.system_generated\steps\83\output.txt', 'r', encoding='utf-8') as f:
    data = json.load(f)
    content = data['content']

lines = content.splitlines(True)

for i, line in enumerate(lines):
    if 'FREE NEIGHBORHOOD GUIDE' in line:
        print(f"Guide at {i+1}: {line.strip()}")
    if 'SELLING & BUYING SPLIT' in line:
        print(f"Selling at {i+1}: {line.strip()}")
    if 'MORTGAGE CALCULATOR' in line:
        print(f"Calculator at {i+1}: {line.strip()}")
    if 'MEET THE TEAM' in line:
        print(f"Team at {i+1}: {line.strip()}")
