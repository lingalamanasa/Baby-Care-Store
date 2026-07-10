import os

for f in ['admin-dashboard.html', 'customer-dashboard.html']:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Replace the opening tag
        content = content.replace('<header class="header">', '<div class="header">')
        
        # Replace the closing tag. But wait, we need to only replace the closing tag of the header we just opened.
        # Since there's only one header, we can just replace </header> with </div>
        content = content.replace('</header>', '</div>')
        
        # In dark theme block we added .header { ... }
        # Let's ensure it has position: relative just in case
        if '.header { background: transparent !important;' in content:
            content = content.replace('.header { background: transparent !important;', '.header { position: relative !important; width: auto !important; background: transparent !important;')

        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
