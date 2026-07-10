import os
import re

custom_logo_html = '''
            <div style="display: flex; align-items: center; justify-content: center; gap: 0.5rem;">
                <div style="background: var(--dark); border-radius: 8px; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #2C3E50, #1a252f);">
                    <i class="bi bi-layers-half" style="color: #00f2fe; font-size: 1.4rem;"></i>
                </div>
                <span style="font-weight: 800; font-size: 1.4rem; color: var(--text-main); letter-spacing: 1px;">STACKLY</span>
            </div>
'''

for f in ['admin-dashboard.html', 'customer-dashboard.html']:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # 1. Fix the .header background to match dark theme
        # The .header is defined in style_v3.css or inline. But in our dark theme block:
        # Let's add .header { background: transparent !important; box-shadow: none !important; }
        if '.header h2' in content:
            content = content.replace('.header h2 {', '.header { background: transparent !important; box-shadow: none !important; }\n        .header h2 {')

        # 2. Fix the .sidebar z-index so it covers everything when open
        # The sidebar z-index is set in the mobile media query. We can just add a global rule:
        if '.sidebar {' in content:
            # Add z-index: 1050 !important; to .sidebar globally and in dark theme block
            content = content.replace('.sidebar {\n            background: var(--bg-dark);', '.sidebar {\n            background: var(--bg-dark);\n            z-index: 1050 !important;')

        # 3. Replace the logo.webp in the sidebar with the custom logo
        logo_regex = re.compile(r'<div class="sidebar-logo">.*?<a href="[^"]+"[^>]*>.*?<img src="assets/images/logo\.webp"[^>]*>.*?</a>.*?</div>', re.DOTALL)
        
        def replace_sidebar_logo(match):
            href = 'admin-dashboard.html' if f == 'admin-dashboard.html' else 'customer-dashboard.html'
            return f'''<div class="sidebar-logo">
            <a href="{href}" style="text-decoration: none; display: block;">
                {custom_logo_html}
            </a>
        </div>'''
        
        content = logo_regex.sub(replace_sidebar_logo, content)
        
        # 4. In customer-dashboard, there is a .stat-badge which is also white!
        if '.stat-badge {' in content:
            content = content.replace('.stat-badge { background: var(--white);', '.stat-badge { background: var(--card-dark); border-color: var(--border-dark);')
            
        # Also need to add .stat-badge to dark theme overrides
        if '.stat-card, .reco-card, .white-card {' in content:
            content = content.replace('.stat-card, .reco-card, .white-card {', '.stat-card, .reco-card, .white-card, .stat-badge {')
            content = content.replace('.stat-card:hover, .reco-card:hover, .white-card:hover {', '.stat-card:hover, .reco-card:hover, .white-card:hover, .stat-badge:hover {')

        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
