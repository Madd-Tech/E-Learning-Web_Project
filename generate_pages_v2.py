import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

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
        res += f'              <li class="{active_class.strip()}" onclick="window.location.href=\'{link}#portfolio\'">{name}</li>\n'
    res += '            </ul>'
    return res

# The user reverted the filters back to id="portfolio-flters"
old_filters_regex = r'<ul id="portfolio-flters(?:-nav)?">.*?</ul>'

# Replace filters in index.html
new_index_html = re.sub(old_filters_regex, generate_filters_html('All'), html, flags=re.DOTALL)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index_html)

# Template card
card_template = """          <div class="col-lg-4 col-md-6 portfolio-item">
            <div class="portfolio-wrap">
              <img src="assets/img/portfolio/portfolio-{idx}.jpg" class="img-fluid" alt="">
              <div class="portfolio-info">
                <h4>{name} Course {idx}</h4>
                <p>{name}</p>
                <div class="portfolio-links">
                  <a href="assets/img/portfolio/portfolio-{idx}.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox" title="Preview"><i class="bx bx-plus"></i></a>
                  <a href="portfolio-details.html" title="More Details"><i class="bx bx-link"></i></a>
                </div>
              </div>
            </div>
          </div>"""

for name, filename in categories:
    if name == 'All':
        continue
    
    # We use the modified index html as base for other pages
    page_html = re.sub(old_filters_regex, generate_filters_html(name), html, flags=re.DOTALL)
    
    # Generate 3 placeholder cards for this category
    cards = []
    for i in range(1, 4):
        cards.append(card_template.format(name=name, idx=i))
    
    new_items_html = '\n'.join(cards)
    
    # Replace items
    container_regex = r'(<div class="row portfolio-container">).*?(</div>\s*</div>\s*</section>)'
    page_html = re.sub(container_regex, r'\g<1>\n' + new_items_html.replace('\\', '\\\\') + r'\n\g<2>', page_html, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page_html)

print("Pages regenerated!")
