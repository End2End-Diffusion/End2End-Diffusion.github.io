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
    const articleList = document.querySelector('.article-list');
    let currentFilter = 'all';
    let blogPostsLoaded = false;

    function runFilters() {
        const articles = articleList.querySelectorAll('article');
        articles.forEach(article => {
            const category = article.getAttribute('data-category');
            const categoryMatch = (currentFilter === 'all' || currentFilter === category);
            article.style.display = categoryMatch ? 'block' : 'none';
        });
    }

    // Fetch blog posts from /blog/ and inject as article cards
    function loadBlogPosts() {
        if (blogPostsLoaded) return Promise.resolve();
        return fetch('blog/')
            .then(r => r.text())
            .then(html => {
                const doc = new DOMParser().parseFromString(html, 'text/html');
                const posts = doc.querySelectorAll('.post-list li');
                posts.forEach(li => {
                    const card = li.querySelector('.post-card');
                    if (!card) return;
                    const href = 'blog/' + card.getAttribute('href');
                    const title = (card.querySelector('.post-title') || {}).textContent || '';
                    const subtitle = (card.querySelector('.post-subtitle') || {}).textContent || '';
                    const date = (card.querySelector('.post-date') || {}).textContent || '';
                    const number = (card.querySelector('.post-number') || {}).textContent || '';
                    const badge = card.querySelector('.status-badge');
                    const badgeText = badge ? badge.textContent : '';

                    const article = document.createElement('article');
                    article.setAttribute('data-category', 'blog');
                    article.setAttribute('data-title', title.toLowerCase());
                    article.innerHTML = `
                        <a href="${href}" class="publication-card block">
                            <div class="article-container">
                                <div class="article-category">
                                    <div class="flex items-center">
                                        <div class="article-icon w-5 h-5 text-gray-700 mr-2 shrink-0">
                                            <i class="fas fa-pen-nib" style="font-size: 0.85rem; color: var(--text-secondary);"></i>
                                        </div>
                                        <span class="category-label">Blog ${badgeText ? '· ' + badgeText : ''}</span>
                                    </div>
                                </div>
                                <div class="article-title-cell">
                                    <h3 class="article-title">${title}</h3>
                                </div>
                                <div class="article-date">
                                    <span class="date-label">${date}</span>
                                </div>
                                <div class="article-description">
                                    <p class="article-desc">${subtitle}</p>
                                </div>
                            </div>
                        </a>
                    `;
                    articleList.appendChild(article);
                });
                blogPostsLoaded = true;
            })
            .catch(() => { /* silently fail if blog not available */ });
    }

    filterButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            currentFilter = e.target.getAttribute('data-filter');

            filterButtons.forEach(btn => btn.classList.remove('active'));
            e.target.classList.add('active');

            if (currentFilter === 'blog' || currentFilter === 'all') {
                loadBlogPosts().then(runFilters);
            } else {
                runFilters();
            }
        });
    });

    // Load blog posts on initial page load so they show under "All"
    loadBlogPosts().then(runFilters);

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
