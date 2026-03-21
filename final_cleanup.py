# Surgical deletion script for final index_updated.html
with open(r'C:\Users\tbow3\OneDrive\Documents\clients\wesellanyhome\index_updated.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Neighborhood Guide header is at 629.
# Section ends at 693.
# Remove 627 to 694 (0-indexed: 626 to 694)
# Header block: lines 627-631 in 1-indexed?
# Let's count back from 629.
# 627: <!-- ═════════
# 628: (Empty)
# 629: FREE NEIGHBORHOOD GUIDE
# 630: ═══════════ -->

# We want to remove 627 to 693.
final_lines = []
for i, line in enumerate(lines):
    # 1-indexed range [627, 693] -> 0-indexed [626, 693)
    if 626 <= i < 693:
        continue
    final_lines.append(line)

content = "".join(final_lines)

# Remove JS logic (again, surgically)
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

print("Final surgery complete.")
