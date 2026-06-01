import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update style.css to support portfolio-flters-nav
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.portfolio #portfolio-flters-nav li' not in css:
    css = css.replace('#portfolio-flters', '#portfolio-flters,\n.portfolio #portfolio-flters-nav')
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Prepare the new filters HTML
categories = [
    ('All', 'index.html'),
    ('Web Development', 'course-web-development.html'),
    ('Python Programming', 'course-python-programming.html'),
    ('Data Science & Machine Learning', 'course-data-science.html'),
    ('AI Engineering', 'course-ai-engineering.html'),
    ('Mobile App Development', 'course-mobile-app.html'),
    ('UI/UX', 'course-ui-ux.html')
]

def generate_filters_html(active_name):
    res = '<ul id="portfolio-flters-nav">\n'
    for name, link in categories:
        active_class = ' filter-active' if name == active_name else ''
        # I'll just rely on the CSS updated for #portfolio-flters-nav
        res += f'              <li class="{active_class.strip()}" onclick="window.location.href=\'{link}#portfolio\'">{name}</li>\n'
    res += '            </ul>'
    return res

# The original filters to replace
old_filters_regex = r'<ul id="portfolio-flters">.*?</ul>'

# 3. Extract items
items_regex = r'(<div class="col-lg-4 col-md-6 portfolio-item.*?(?:</div>\s*</div>\s*</div>))'
items = re.findall(items_regex, html, re.DOTALL)

def get_items_for_category(name):
    if name == 'All': return items
    filtered = []
    for item in items:
        # Check <p> content
        p_match = re.search(r'<p>(.*?)</p>', item)
        if p_match:
            p_text = p_match.group(1).strip()
            if name == 'Web Development' and p_text == 'Web Development': filtered.append(item)
            elif name == 'Python Programming' and p_text == 'Python Programming': filtered.append(item)
            elif name == 'Data Science & Machine Learning' and p_text == 'Data Science & Machine Learning': filtered.append(item)
            elif name == 'AI Engineering' and p_text == 'AI Engineering': filtered.append(item)
            elif name == 'Mobile App Development' and p_text == 'App': filtered.append(item)
            elif name == 'UI/UX' and p_text in ['Card', 'Web']: filtered.append(item)
    return filtered

for name, filename in categories:
    new_html = re.sub(old_filters_regex, generate_filters_html(name), html, flags=re.DOTALL)
    
    # Replace items
    # Find the container
    container_regex = r'(<div class="row portfolio-container">).*?(</div>\s*</div>\s*</section>)'
    
    cat_items = get_items_for_category(name)
    new_items_html = '\n'.join(cat_items)
    
    new_html = re.sub(container_regex, r'\g<1>\n' + new_items_html.replace('\\', '\\\\') + r'\n\g<2>', new_html, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_html)

print('Done')
