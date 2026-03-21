import json

# Absolute path to the JSON output from Step 83
json_path = r'C:\Users\tbow3\.gemini\antigravity\brain\ab5b8aee-5d0b-4e83-9394-e0e4af5e12d2\.system_generated\steps\83\output.txt'
# Output path in the workspace
output_path = r'C:\Users\tbow3\OneDrive\Documents\clients\wesellanyhome\index.html'

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    content = data['content']
    with open(output_path, 'w', encoding='utf-8') as out:
        out.write(content)
print(f"Extracted index.html to {output_path}")
