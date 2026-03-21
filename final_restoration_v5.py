import json

with open(r'C:\Users\tbow3\.gemini\antigravity\brain\ab5b8aee-5d0b-4e83-9394-e0e4af5e12d2\.system_generated\steps\83\output.txt', 'r', encoding='utf-8') as f:
    data = json.load(f)
    content = data['content']

lines = content.splitlines(True)

# Find the start and end of the Neighborhood Guide section in the lines list
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if 'FREE NEIGHBORHOOD GUIDE' in line:
        # The header starts a few lines before
        start_idx = i - 1
        # Continue back to find the first '══════' line
        while start_idx > 0 and '══════' not in lines[start_idx-1]:
            start_idx -= 1
        # Include the top separator line
        if start_idx > 0: start_idx -= 1
        break

if start_idx != -1:
    # Find the end of that section
    # It followed by id="guides" section
    for i in range(start_idx, len(lines)):
        if '</section>' in lines[i]:
            # The next section header is 'SELLING & BUYING SPLIT'
            # Check if it follows soon
            found_next = False
            for j in range(i+1, min(i+10, len(lines))):
                if 'SELLING & BUYING SPLIT' in lines[j]:
                    found_next = True
                    break
            if found_next:
                end_idx = i + 1
                break

if start_idx != -1 and end_idx != -1:
    print(f"Removing lines {start_idx} to {end_idx}")
    del lines[start_idx:end_idx]

# Padding adjustments
for i in range(len(lines)):
    if 'id="reviews" class="py-16 bg-gray-50"' in lines[i]:
        lines[i] = lines[i].replace('id="reviews" class="py-16 bg-gray-50"', 'id="reviews" class="pt-16 pb-0 bg-gray-50"')
    if 'class="py-16 bg-gray-50" aria-labelledby="servicesHeading"' in lines[i]:
        lines[i] = lines[i].replace('class="py-16 bg-gray-50" aria-labelledby="servicesHeading"', 'class="pt-8 pb-16 bg-gray-50" aria-labelledby="servicesHeading"')

content = "".join(lines)

# Remove JS logic
js_obj_start = 'const countyNeighborhoods = {'
js_obj_end = '};\n\n    const countySelect'
j_s_idx = content.find(js_obj_start)
if j_s_idx != -1:
    j_e_idx = content.find(js_obj_end, j_s_idx)
    if j_e_idx != -1:
        content = content[:j_s_idx] + content[j_e_idx + len('};\n\n    '):]

js_form_start = "document.getElementById('guideForm')?.addEventListener('submit'"
j_f_s_idx = content.find(js_form_start)
if j_f_s_idx != -1:
    j_f_e_idx = content.find('});', j_f_s_idx)
    if j_f_e_idx != -1:
        content = content[:j_f_s_idx] + content[j_f_e_idx + 4:]

with open(r'C:\Users\tbow3\OneDrive\Documents\clients\wesellanyhome\index_updated.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Final restoration with search complete.")
