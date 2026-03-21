import json

# Load original content
with open(r'C:\Users\tbow3\.gemini\antigravity\brain\ab5b8aee-5d0b-4e83-9394-e0e4af5e12d2\.system_generated\steps\83\output.txt', 'r', encoding='utf-8') as f:
    data = json.load(f)
    content = data['content']

lines = content.splitlines(True)

# 1. Surgical removal of Neighborhood Guide
# From find_lines.py: Guide is at 629, Selling is at 696.
# Let's find the header blocks more carefully.

def find_header_start(lines, search_text, current_idx):
    # Search backwards from current_idx for the separator line
    idx = current_idx
    while idx > 0:
        if '══════' in lines[idx]:
            # Found one separator. Found the one before it.
            if idx > 0 and '══════' in lines[idx-1]: # This shouldn't happen usually
                pass 
            # Check if there's another separator above
            if idx > 2 and '══════' in lines[idx-2]:
                return idx - 2
            return idx
        idx -= 1
    return current_idx

guide_text_idx = -1
for i, line in enumerate(lines):
    if 'FREE NEIGHBORHOOD GUIDE' in line:
        guide_text_idx = i
        break

if guide_text_idx != -1:
    start_delete = find_header_start(lines, 'FREE NEIGHBORHOOD GUIDE', guide_text_idx)
    
    # End delete should be just before the next header
    selling_text_idx = -1
    for i in range(guide_text_idx, len(lines)):
        if 'SELLING & BUYING SPLIT' in lines[i]:
            selling_text_idx = i
            break
    
    if selling_text_idx != -1:
        end_delete = find_header_start(lines, 'SELLING & BUYING SPLIT', selling_text_idx)
        print(f"Deleting from line {start_delete+1} to {end_delete}")
        del lines[start_delete:end_delete]

# 2. Padding adjustments
for i in range(len(lines)):
    # Reviews
    if 'id="reviews" class="py-16 bg-gray-50"' in lines[i]:
        lines[i] = lines[i].replace('id="reviews" class="py-16 bg-gray-50"', 'id="reviews" class="pt-16 pb-0 bg-gray-50"')
    # Services
    if 'class="py-16 bg-gray-50" aria-labelledby="servicesHeading"' in lines[i]:
        lines[i] = lines[i].replace('class="py-16 bg-gray-50" aria-labelledby="servicesHeading"', 'class="pt-8 pb-16 bg-gray-50" aria-labelledby="servicesHeading"')

content = "".join(lines)

# 3. JS removals
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

# Verify the result has major sections in order
print("Verification:")
print(f"Reviews padding: {'pt-16 pb-0' in content}")
print(f"Services padding: {'pt-8' in content}")
print(f"Neighborhood Guide removed: {'FREE NEIGHBORHOOD GUIDE' not in content}")
print(f"Selling section OK: {'id=\"selling\"' in content}")
print(f"Calculator section OK: {'MORTGAGE CALCULATOR' in content}")
print(f"Team section OK: {'MEET THE TEAM' in content}")

with open(r'C:\Users\tbow3\OneDrive\Documents\clients\wesellanyhome\index_updated.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Definitive restoration complete.")
