import os
import re

# Dark theme CSS for dashboards
dark_theme_css = '''
        /* Dark Theme Variables & Base */
        :root {
            --bg-dark: #0A0F1C;
            --card-dark: #131B2F;
            --border-dark: #1E293B;
            --text-main: #F8FAFC;
            --text-muted: #94A3B8;
            --accent-cyan: #00F2FE;
            --accent-blue: #4FACFE;
        }
        body {
            background-color: var(--bg-dark);
            color: var(--text-main);
            font-family: 'Inter', sans-serif;
        }
        
        /* Sidebar Styles */
        .sidebar {
            background: var(--bg-dark);
            border-right: 1px solid var(--border-dark);
        }
        .sidebar-menu a {
            color: var(--text-muted);
        }
        .sidebar-menu a:hover {
            background: rgba(255, 255, 255, 0.05);
            color: var(--text-main);
        }
        .sidebar-menu a.active {
            background: rgba(0, 242, 254, 0.1);
            color: var(--accent-cyan) !important;
            border-left: 4px solid var(--accent-cyan) !important;
        }
        .sidebar-menu a.active i {
            color: var(--accent-cyan) !important;
        }

        /* Main Content */
        .header h2 {
            color: var(--text-main);
        }
        .header p {
            color: var(--text-muted);
        }

        /* Cards */
        .stat-card, .reco-card, .white-card {
            background: var(--card-dark) !important;
            border: 1px solid var(--border-dark) !important;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2) !important;
        }
        .stat-card:hover, .reco-card:hover, .white-card:hover {
            border-color: rgba(0, 242, 254, 0.3) !important;
            box-shadow: 0 8px 32px rgba(0, 242, 254, 0.1) !important;
            transform: translateY(-2px);
        }
        .stat-card h3, .stat-card h5 {
            color: var(--text-main) !important;
        }
        .stat-card p {
            color: var(--text-muted);
        }
        .stat-card .stat-icon {
            background: rgba(255, 255, 255, 0.05) !important;
            color: var(--text-main) !important;
        }

        /* Mobile Header */
        @media (max-width: 991px) {
            .mobile-header {
                background: var(--bg-dark) !important;
                border-bottom: 1px solid var(--border-dark) !important;
                padding: 1rem 1.5rem !important;
            }
            .mobile-menu-btn {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid var(--border-dark);
                border-radius: 8px;
                padding: 0.4rem 0.6rem;
                display: flex !important;
                align-items: center;
                justify-content: center;
                color: var(--text-main) !important;
            }
            
            /* Floating Action Button (FAB) for mobile menu */
            .fab-menu {
                display: flex !important;
                position: fixed;
                bottom: 30px;
                left: 30px;
                width: 60px;
                height: 60px;
                border-radius: 50%;
                background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
                color: #fff;
                align-items: center;
                justify-content: center;
                font-size: 1.8rem;
                box-shadow: 0 10px 25px rgba(0, 242, 254, 0.4);
                z-index: 1001;
                cursor: pointer;
                transition: transform 0.2s ease;
            }
            .fab-menu:active {
                transform: scale(0.95);
            }
        }
        .fab-menu { display: none; }
'''

fab_html = '''
    <!-- Floating Action Button for Mobile -->
    <div class="fab-menu" onclick="document.querySelector('.sidebar').classList.toggle('active')">
        <i class="bi bi-list"></i>
    </div>
'''

for f in ['admin-dashboard.html', 'customer-dashboard.html']:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Inject the dark theme CSS just before </style>
        content = content.replace('</style>', dark_theme_css + '\n    </style>')
        
        # Inject the FAB right before </body>
        content = content.replace('</body>', fab_html + '\n</body>')
        
        # Also let's update some specific text colors that might be hardcoded
        content = content.replace('color: var(--dark);', 'color: var(--text-main);')
        content = content.replace('color: var(--gray);', 'color: var(--text-muted);')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
