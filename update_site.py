import json
import re

json_path = r'C:\Users\tbow3\.gemini\antigravity\brain\ab5b8aee-5d0b-4e83-9394-e0e4af5e12d2\.system_generated\steps\83\output.txt'

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    content = data['content']

# 1. Remove the section id="guides"
section_pattern = r'  <!-- ══════════════+[\s\S]+?FREE NEIGHBORHOOD GUIDE[\s\S]+?══════════════+ -->\n  <section id="guides"[\s\S]+?</section>\n\n'
content = re.sub(section_pattern, '', content)

# 2. Remove the JS logic block for Neighborhood Guide
# Remove the block about countyNeighborhoods and event listeners.
js_block_pattern = r'    /\* ── Neighborhood Guide form ── \*/[\s\S]+?\}\);\n\n'
content = re.sub(js_block_pattern, '', content)

# 3. Check for any leftover guide form event listeners
# The previous regex might have missed some if they weren't in that exact block.
# Let's specifically remove the guideForm event listener if it still exists.
guide_form_pattern = r'    document\.getElementById\(\'guideForm\'\)\?\.addEventListener\(\'submit\'[\s\S]+?\}\);\n\n'
content = re.sub(guide_form_pattern, '', content)

with open(r'C:\Users\tbow3\OneDrive\Documents\clients\wesellanyhome\index_updated.html', 'w', encoding='utf-8') as out:
    out.write(content)

print("Refined index.html created.")
