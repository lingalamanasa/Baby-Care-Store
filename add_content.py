import os

admin_content = '''
        <div class="dashboard-grid" style="margin-top: 2rem;">
            <div class="panel">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-dark); padding-bottom: 1rem; margin-bottom: 1.5rem;">
                    <h3 style="margin: 0; display: flex; align-items: center; gap: 0.5rem;"><i class="bi bi-exclamation-triangle" style="color: #ef4444;"></i> Low Stock Alerts</h3>
                    <a href="404.html" style="color: var(--accent-blue); text-decoration: none; font-size: 0.9rem; font-weight: 600; transition: 0.2s;" onmouseover="this.style.color='#00f2fe'" onmouseout="this.style.color='var(--accent-blue)'">View Inventory &rarr;</a>
                </div>
                <div style="display: flex; flex-direction: column; gap: 1rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem; background: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.2); border-radius: 12px; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <div style="width: 50px; height: 50px; background: rgba(255,255,255,0.05); border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                                <i class="bi bi-droplet" style="color: #ef4444; font-size: 1.5rem;"></i>
                            </div>
                            <div>
                                <h5 style="margin: 0; font-size: 1rem; color: var(--text-main);">Organic Baby Lotion</h5>
                                <p style="margin: 0; font-size: 0.85rem; color: #ef4444; font-weight: 600;">Only 4 left in stock</p>
                            </div>
                        </div>
                        <button class="btn btn-outline" style="padding: 0.4rem 1rem; font-size: 0.85rem; border-color: #ef4444; color: #ef4444; border-radius: 8px;">Restock</button>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem; background: rgba(245, 158, 11, 0.05); border: 1px solid rgba(245, 158, 11, 0.2); border-radius: 12px; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <div style="width: 50px; height: 50px; background: rgba(255,255,255,0.05); border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                                <i class="bi bi-moon-stars" style="color: #f59e0b; font-size: 1.5rem;"></i>
                            </div>
                            <div>
                                <h5 style="margin: 0; font-size: 1rem; color: var(--text-main);">Silicone Teething Ring</h5>
                                <p style="margin: 0; font-size: 0.85rem; color: #f59e0b; font-weight: 600;">Only 12 left in stock</p>
                            </div>
                        </div>
                        <button class="btn btn-outline" style="padding: 0.4rem 1rem; font-size: 0.85rem; border-color: #f59e0b; color: #f59e0b; border-radius: 8px;">Restock</button>
                    </div>
                </div>
            </div>
            
            <div class="panel">
                <div style="border-bottom: 1px solid var(--border-dark); padding-bottom: 1rem; margin-bottom: 1.5rem;">
                    <h3 style="margin: 0; display: flex; align-items: center; gap: 0.5rem;"><i class="bi bi-globe" style="color: var(--accent-cyan);"></i> Top Selling Regions</h3>
                </div>
                <div style="display: flex; flex-direction: column; gap: 1.5rem;">
                    <div>
                        <div style="display: flex; justify-content: space-between; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem; color: var(--text-main);">
                            <span>North America</span>
                            <span style="color: var(--accent-cyan);">45%</span>
                        </div>
                        <div style="background: var(--bg-dark); height: 8px; border-radius: 4px; overflow: hidden; border: 1px solid var(--border-dark);">
                            <div style="background: linear-gradient(90deg, #00f2fe, #4facfe); width: 45%; height: 100%; border-radius: 4px; box-shadow: 0 0 10px rgba(0, 242, 254, 0.5);"></div>
                        </div>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem; color: var(--text-main);">
                            <span>Europe</span>
                            <span style="color: #10b981;">30%</span>
                        </div>
                        <div style="background: var(--bg-dark); height: 8px; border-radius: 4px; overflow: hidden; border: 1px solid var(--border-dark);">
                            <div style="background: linear-gradient(90deg, #10b981, #34d399); width: 30%; height: 100%; border-radius: 4px; box-shadow: 0 0 10px rgba(16, 185, 129, 0.5);"></div>
                        </div>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem; color: var(--text-main);">
                            <span>Asia Pacific</span>
                            <span style="color: #f59e0b;">25%</span>
                        </div>
                        <div style="background: var(--bg-dark); height: 8px; border-radius: 4px; overflow: hidden; border: 1px solid var(--border-dark);">
                            <div style="background: linear-gradient(90deg, #f59e0b, #fbbf24); width: 25%; height: 100%; border-radius: 4px; box-shadow: 0 0 10px rgba(245, 158, 11, 0.5);"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
'''

customer_content = '''
        <div class="dashboard-grid" style="margin-top: 2rem;">
            <div class="panel">
                <div style="border-bottom: 1px solid var(--border-dark); padding-bottom: 1rem; margin-bottom: 1.5rem;">
                    <h3 style="margin: 0; display: flex; align-items: center; gap: 0.5rem;"><i class="bi bi-tags" style="color: var(--accent-cyan);"></i> Active Coupons</h3>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                    <div style="background: linear-gradient(135deg, rgba(0,242,254,0.1), rgba(79,172,254,0.05)); border: 1px dashed var(--accent-blue); padding: 1.5rem; border-radius: 16px; text-align: center; position: relative; overflow: hidden; transition: 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 20px rgba(0,242,254,0.1)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';">
                        <div style="position: absolute; top: 15px; right: -30px; background: #ef4444; color: white; font-size: 0.65rem; font-weight: 800; padding: 0.2rem 2.5rem; transform: rotate(45deg); box-shadow: 0 2px 5px rgba(0,0,0,0.2);">EXPIRING</div>
                        <h4 style="color: var(--accent-cyan); font-size: 1.8rem; letter-spacing: 2px; margin: 0 0 0.5rem 0; text-shadow: 0 0 10px rgba(0,242,254,0.3);">BABY20</h4>
                        <p style="margin: 0; font-size: 0.9rem; color: var(--text-main); font-weight: 600;">20% OFF your entire order!</p>
                        <p style="margin: 0.5rem 0 0 0; font-size: 0.75rem; color: var(--text-muted);">Valid until Nov 30, 2026</p>
                    </div>
                    <div style="background: rgba(255,255,255,0.02); border: 1px dashed var(--border-dark); padding: 1.5rem; border-radius: 16px; text-align: center; transition: 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.borderColor='var(--text-muted)';" onmouseout="this.style.transform='translateY(0)'; this.style.borderColor='var(--border-dark)';">
                        <h4 style="color: var(--text-main); font-size: 1.5rem; letter-spacing: 2px; margin: 0 0 0.5rem 0;">FREESHIP</h4>
                        <p style="margin: 0; font-size: 0.9rem; color: var(--text-muted); font-weight: 600;">Free express shipping.</p>
                        <p style="margin: 0.5rem 0 0 0; font-size: 0.75rem; color: var(--text-muted);">Valid on orders over $50</p>
                    </div>
                </div>
            </div>
            
            <div class="panel">
                <div style="border-bottom: 1px solid var(--border-dark); padding-bottom: 1rem; margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="margin: 0; display: flex; align-items: center; gap: 0.5rem;"><i class="bi bi-chat-dots" style="color: var(--accent-cyan);"></i> Support Tickets</h3>
                    <a href="404.html" style="color: var(--text-muted); text-decoration: none; font-size: 0.85rem; font-weight: 600;">Open New +</a>
                </div>
                <div style="display: flex; flex-direction: column; gap: 1rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem; background: var(--bg-dark); border-radius: 12px; border: 1px solid var(--border-dark); cursor: pointer; transition: 0.2s;" onmouseover="this.style.borderColor='rgba(255,255,255,0.2)'" onmouseout="this.style.borderColor='var(--border-dark)'">
                        <div>
                            <p style="margin: 0; font-weight: 600; color: var(--text-main);">#TK-8021 <span style="font-size: 0.75rem; font-weight: 400; color: var(--text-muted); margin-left: 0.5rem;">Oct 28</span></p>
                            <p style="margin: 0.25rem 0 0 0; font-size: 0.85rem; color: var(--text-muted);">Question about product ingredients</p>
                        </div>
                        <span style="background: rgba(16,185,129,0.1); color: #10b981; padding: 0.2rem 0.6rem; border-radius: 20px; font-size: 0.7rem; font-weight: 700; border: 1px solid rgba(16,185,129,0.2);">Resolved</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem; background: var(--bg-dark); border-radius: 12px; border: 1px solid var(--border-dark); cursor: pointer; transition: 0.2s;" onmouseover="this.style.borderColor='var(--accent-blue)'" onmouseout="this.style.borderColor='var(--border-dark)'">
                        <div>
                            <p style="margin: 0; font-weight: 600; color: var(--text-main);">#TK-9104 <span style="font-size: 0.75rem; font-weight: 400; color: var(--text-muted); margin-left: 0.5rem;">Yesterday</span></p>
                            <p style="margin: 0.25rem 0 0 0; font-size: 0.85rem; color: var(--text-muted);">Exchange request for order #ORD-001</p>
                        </div>
                        <span style="background: rgba(245,158,11,0.1); color: #f59e0b; padding: 0.2rem 0.6rem; border-radius: 20px; font-size: 0.7rem; font-weight: 700; border: 1px solid rgba(245,158,11,0.2);">Pending</span>
                    </div>
                </div>
            </div>
        </div>
'''

def inject_content(filepath, new_html):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will inject the new HTML right before the </main> closing tag
    if '</main>' in content:
        content = content.replace('</main>', new_html + '\n    </main>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

inject_content('admin-dashboard.html', admin_content)
inject_content('customer-dashboard.html', customer_content)

print("Injected successfully.")
