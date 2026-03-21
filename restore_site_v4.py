import json

# Load from step 83
json_path = r'C:\Users\tbow3\.gemini\antigravity\brain\ab5b8aee-5d0b-4e83-9394-e0e4af5e12d2\.system_generated\steps\83\output.txt'
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    content = data['content']

lines = content.splitlines(keepends=True)

# Remove lines 819 to 891 (inclusive, 1-indexed)
# 0-indexed: 818 to 890
del lines[818:891]

# Padding adjustments
for i in range(len(lines)):
    if 'id="reviews" class="py-16 bg-gray-50"' in lines[i]:
        lines[i] = lines[i].replace('id="reviews" class="py-16 bg-gray-50"', 'id="reviews" class="pt-16 pb-0 bg-gray-50"')
    if 'class="py-16 bg-gray-50" aria-labelledby="servicesHeading"' in lines[i]:
        lines[i] = lines[i].replace('class="py-16 bg-gray-50" aria-labelledby="servicesHeading"', 'class="pt-8 pb-16 bg-gray-50" aria-labelledby="servicesHeading"')

content = "".join(lines)

# Remove JS logic (surgically)
js_obj_start = 'const countyNeighborhoods = {'
js_obj_end = '};\n\n    const countySelect' # Match the end and the start of the next line to be safe
j_s_idx = content.find(js_obj_start)
if j_s_idx != -1:
    j_e_idx = content.find(js_obj_end, j_s_idx)
    if j_e_idx != -1:
        # Keep the newline and the next line start
        content = content[:j_s_idx] + content[j_e_idx + len('};\n\n    '):]

js_form_start = "document.getElementById('guideForm')?.addEventListener('submit'"
j_f_s_idx = content.find(js_form_start)
if j_f_s_idx != -1:
    # Find the closing }); and the following newline
    j_f_e_idx = content.find('});', j_f_s_idx)
    if j_f_e_idx != -1:
        content = content[:j_f_s_idx] + content[j_f_e_idx + 4:]

output_path = r'C:\Users\tbow3\OneDrive\Documents\clients\wesellanyhome\index_updated.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Surgical restoration complete.")
