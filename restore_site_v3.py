import json

# Load from step 83
json_path = r'C:\Users\tbow3\.gemini\antigravity\brain\ab5b8aee-5d0b-4e83-9394-e0e4af5e12d2\.system_generated\steps\83\output.txt'
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    content = data['content']

# Split into lines (preserving newline character)
lines = content.splitlines(keepends=True)

final_lines = []
skip = False
for i, line in enumerate(lines):
    # Detect start of Neighborhood Guide
    if 'FREE NEIGHBORHOOD GUIDE' in line:
        skip = True
        continue
    
    # Detect end of Neighborhood Guide section
    # The guide section ends with a </section> followed by a newline and then the SELLING header
    if skip and '</section>' in line:
        # Check if the next non-empty line is the next header
        found_next = False
        for j in range(i+1, min(i+10, len(lines))):
            if 'SELLING & BUYING SPLIT' in lines[j]:
                found_next = True
                break
        if found_next:
            skip = False
            continue

    if not skip:
        # Padding adjustments
        if 'id="reviews" class="py-16 bg-gray-50"' in line:
            line = line.replace('id="reviews" class="py-16 bg-gray-50"', 'id="reviews" class="pt-16 pb-0 bg-gray-50"')
        if 'class="py-16 bg-gray-50" aria-labelledby="servicesHeading"' in line:
            line = line.replace('class="py-16 bg-gray-50" aria-labelledby="servicesHeading"', 'class="pt-8 pb-16 bg-gray-50" aria-labelledby="servicesHeading"')
        final_lines.append(line)

# JS removal is easier with joined content
content = "".join(final_lines)

# Remove JS
js_obj_start = 'const countyNeighborhoods = {'
js_obj_end = '};'
j_s_idx = content.find(js_obj_start)
if j_s_idx != -1:
    j_e_idx = content.find(js_obj_end, j_s_idx)
    if j_e_idx != -1:
        content = content[:j_s_idx] + content[j_e_idx + len(js_obj_end):]

js_form_start = "document.getElementById('guideForm')?.addEventListener('submit'"
j_f_s_idx = content.find(js_form_start)
if j_f_s_idx != -1:
    j_f_e_idx = content.find('});', j_f_s_idx)
    if j_f_e_idx != -1:
        content = content[:j_f_s_idx] + content[j_f_e_idx + 3:]

output_path = r'C:\Users\tbow3\OneDrive\Documents\clients\wesellanyhome\index_updated.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Line-by-line restoration complete.")
