import json

# Load from step 83
json_path = r'C:\Users\tbow3\.gemini\antigravity\brain\ab5b8aee-5d0b-4e83-9394-e0e4af5e12d2\.system_generated\steps\83\output.txt'
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    content = data['content']

# 1. Remove Neighborhood Guide surgical removal
guide_header = '<!-- ═══════════════════════════════════════════════════════════\n       FREE NEIGHBORHOOD GUIDE\n  ═══════════════════════════════════════════════════════════ -->'
guide_start_tag = '<section id="guides"'
guide_end_tag = '</section>'

# Find the header
h_idx = content.find(guide_header)
if h_idx != -1:
    # Find the section start after the header
    s_idx = content.find(guide_start_tag, h_idx)
    if s_idx != -1:
        # Find the section end after the section start
        e_idx = content.find(guide_end_tag, s_idx)
        if e_idx != -1:
            # Remove from header to the end tag + newline
            # We want to remove the section and the header
            # The next section starts with another header
            content = content[:h_idx] + content[e_idx + len(guide_end_tag):]

# 2. Remove JS logic
# Remove countyNeighborhoods
js_obj_start = 'const countyNeighborhoods = {'
js_obj_end = '};'
j_s_idx = content.find(js_obj_start)
if j_s_idx != -1:
    j_e_idx = content.find(js_obj_end, j_s_idx)
    if j_e_idx != -1:
        content = content[:j_s_idx] + content[j_e_idx + len(js_obj_end):]

# Remove specific guide listeners
js_form_start = "document.getElementById('guideForm')?.addEventListener('submit'"
j_f_s_idx = content.find(js_form_start)
if j_f_s_idx != -1:
    # Find the closing });
    j_f_e_idx = content.find('});', j_f_s_idx)
    if j_f_e_idx != -1:
        content = content[:j_f_s_idx] + content[j_f_e_idx + 3:]

# 3. Padding adjustments for "Even Breaks"
# Reviews is Gray-50, Services is Gray-50.
# Reviews: change py-16 to pt-16 pb-0
content = content.replace('id="reviews" class="py-16 bg-gray-50"', 'id="reviews" class="pt-16 pb-0 bg-gray-50"')
# Services: change py-16 to pt-8 pb-16
content = content.replace('class="py-16 bg-gray-50" aria-labelledby="servicesHeading"', 'class="pt-8 pb-16 bg-gray-50" aria-labelledby="servicesHeading"')

# Write the file
output_path = r'C:\Users\tbow3\OneDrive\Documents\clients\wesellanyhome\index_updated.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final restoration complete.")
