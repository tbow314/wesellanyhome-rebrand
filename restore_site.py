import json
import re

# Load the full original content from the step 83 output (JSON)
json_path = r'C:\Users\tbow3\.gemini\antigravity\brain\ab5b8aee-5d0b-4e83-9394-e0e4af5e12d2\.system_generated\steps\83\output.txt'

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    content = data['content']

# 1. Remove the Neighborhood Guide section (HTML)
# This section starts with id="guides" and spans until the next section start.
# Based on the original file:
#   <section id="guides" class="py-16 bg-navy-900" aria-labelledby="guidesHeading">
#   ...
#   </section>
pattern_section = re.compile(r'<!-- ═══════════════════════════════════════════════════════════\s+FREE NEIGHBORHOOD GUIDE\s+═══════════════════════════════════════════════════════════ -->\s+<section id="guides".*?</section>', re.DOTALL)
content = pattern_section.sub('', content)

# 2. Remove the JavaScript logic for the Neighborhood Guide
# Remove the countyNeighborhoods object
pattern_js_obj = re.compile(r'const countyNeighborhoods = \{.*?\};', re.DOTALL)
content = pattern_js_obj.sub('', content)

# Remove the countySelect and neighborhoodSelect listeners
pattern_js_listeners = re.compile(r'const countySelect = document\.getElementById\(\'guideCounty\'\);.*?document\.getElementById\(\'guideForm\'\)\?\.addEventListener\(\'submit\', function \(e\) \{.*?\}\);', re.DOTALL)
content = pattern_js_listeners.sub('', content)

# 3. Fix "Uneven Page Breaks"
# After removing the Guide (Navy background), we have Reviews (Gray-50) followed by Services (Gray-50).
# The Reviews section ends with py-16, and Services starts with py-16.
# I will reduce the padding between them to make the transition more standard.
# I'll replace the class on the Services section and Reviews section.

# Find the Reviews section: <section id="reviews" class="py-16 bg-gray-50" aria-labelledby="reviewsHeading">
# I'll change it to pb-8 (instead of py-16) to reduce bottom space.
content = content.replace('id="reviews" class="py-16 bg-gray-50"', 'id="reviews" class="pt-16 pb-8 bg-gray-50"')

# Find the Services section: <section class="py-16 bg-gray-50" aria-labelledby="servicesHeading">
# I'll change it to pt-8 (instead of py-16) to reduce top space.
content = content.replace('class="py-16 bg-gray-50" aria-labelledby="servicesHeading"', 'class="pt-8 pb-16 bg-gray-50" aria-labelledby="servicesHeading"')

# Write the fixed content
output_path = r'C:\Users\tbow3\OneDrive\Documents\clients\wesellanyhome\index_updated.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Restoration and cleanup complete.")
