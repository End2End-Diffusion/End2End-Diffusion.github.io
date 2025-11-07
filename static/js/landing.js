document.addEventListener('DOMContentLoaded', () => {
    // Dark mode toggle functionality
    const themeToggle = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;

    // Check for saved theme preference or auto-detect from system
    let currentTheme = localStorage.getItem('theme');
    if (!currentTheme) {
        // Auto-detect from system preference
        currentTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    htmlElement.setAttribute('data-theme', currentTheme);

    // Toggle theme
    themeToggle.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';

        htmlElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
    });

    // Listen for system theme changes (optional: auto-switch if user hasn't set preference)
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        // Only auto-switch if user hasn't manually set a preference
        if (!localStorage.getItem('theme')) {
            htmlElement.setAttribute('data-theme', e.matches ? 'dark' : 'light');
        }
    });

    // Filter functionality
    const filterButtons = document.querySelectorAll('.filter-btn');
    const articles = document.querySelectorAll('.article-list article');
    let currentFilter = 'all';

    function runFilters() {
        articles.forEach(article => {
            const category = article.getAttribute('data-category');

            const categoryMatch = (currentFilter === 'all' || currentFilter === category);

            if (categoryMatch) {
                article.style.display = 'block';
            } else {
                article.style.display = 'none';
            }
        });
    }

    filterButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            currentFilter = e.target.getAttribute('data-filter');

            filterButtons.forEach(btn => btn.classList.remove('active'));
            e.target.classList.add('active');

            runFilters();
        });
    });

    // Image error handling
    document.querySelectorAll('img').forEach(img => {
        img.addEventListener('error', function() {
            if (!this.dataset.error) {
                this.dataset.error = true;
                const altText = this.alt ? encodeURIComponent(this.alt) : 'Image+Not+Found';
                this.src = `https://placehold.co/600x400/eeeeee/999999?text=${altText}`;
            }
        });
    });
});
