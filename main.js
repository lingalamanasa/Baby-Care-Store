document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileBtn && navLinks) {
        mobileBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = mobileBtn.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('bi-list');
                icon.classList.add('bi-x');
            } else {
                icon.classList.remove('bi-x');
                icon.classList.add('bi-list');
            }
        });
    }

    // Header scroll effect
    const header = document.querySelector('header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.style.boxShadow = '0 5px 20px rgba(0,0,0,0.1)';
                header.style.padding = '0.5rem 0';
            } else {
                header.style.boxShadow = '0 2px 15px rgba(0,0,0,0.05)';
                header.style.padding = '1rem 0';
            }
        });
    }

    // Role-based Login Simulation
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const role = document.getElementById('roleSelect').value;
            if (role === 'admin') {
                window.location.href = 'admin-dashboard.html';
            } else {
                window.location.href = 'customer-dashboard.html';
            }
        });
    }

    // Add 404 links redirection logic for all 'Know More', 'Read More', etc buttons
    const checkLinks = () => {
        const links = document.querySelectorAll('a');
        links.forEach(link => {
            const text = link.textContent.trim().toLowerCase();
            const href = link.getAttribute('href');
            
            // Match specific texts or social media
            if (text === 'know more' || text === 'read more' || text === 'learn more' || 
                link.classList.contains('social-link')) {
                if (!href || href === '#' || href === '') {
                    link.setAttribute('href', '404.html');
                }
            }
        });
    };
    checkLinks();

    // Scroll Reveal Animations
    const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });
});
