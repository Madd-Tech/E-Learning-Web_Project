import os, glob, re

root_dir = r'c:\Materi matkul\Web Design\1125170080'
html_files = glob.glob(os.path.join(root_dir, '*.html')) + glob.glob(os.path.join(root_dir, 'courses', '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    is_course = 'courses' in filepath
    prefix = '../' if is_course else ''
    
    # Replace header div
    content = re.sub(
        r'<div\s+data-component=["\']components/header\.html["\'].*></div>',
        f'<script src="{prefix}components/header.js"></script>',
        content
    )
    
    # Replace footer div
    content = re.sub(
        r'<div\s+data-component=["\']components/footer\.html["\'].*></div>',
        f'<script src="{prefix}components/footer.js"></script>',
        content
    )
    
    # Remove component loader script
    content = re.sub(
        r'<!-- Component Loader -->\s*<script src="[\./]*assets/js/component-loader\.js"></script>',
        '',
        content
    )
    
    content = re.sub(
        r'<script src="[\./]*assets/js/component-loader\.js"></script>',
        '',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print('Replacement complete.')
