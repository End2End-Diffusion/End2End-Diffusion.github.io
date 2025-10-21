var dContents = document.querySelector('d-contents');
var dArticle = document.querySelector('d-article');
var headerWrapper = document.querySelector('.header-wrapper');

// Get the computed style of the element to access the margin
var computedStyle = window.getComputedStyle(dContents);
// Get the top margin as an integer
var marginTop = parseInt(computedStyle.marginTop, 10);
// Calculate the original top offset plus the margin-top
var originalOffsetTop = dContents.offsetTop;
var originalOffsetLeft = dContents.offsetLeft;
var originalWidth = dContents.offsetWidth; // This should include padding if box-sizing is border-box

// Calculate hero section height (header + some buffer)
var heroHeight = headerWrapper ? headerWrapper.offsetHeight + 100 : 400;

// Function to handle the resize event
function onResize() {
    // Recalculate original left and width on resize
    originalOffsetLeft = dContents.offsetLeft;
    originalWidth = dContents.offsetWidth; // This should include padding if box-sizing is border-box
    heroHeight = headerWrapper ? headerWrapper.offsetHeight + 100 : 400;
}

// Add the resize event listener
window.addEventListener('resize', onResize);

window.addEventListener('scroll', function() {
    if (window.innerWidth > 1000) {
        var scrollPosition = window.pageYOffset || document.documentElement.scrollTop;
        var dArticleBottom = dArticle.offsetTop + dArticle.offsetHeight;
        var dContentsActualTop = scrollPosition > originalOffsetTop ? scrollPosition : originalOffsetTop;
        var dContentsBottom = dContentsActualTop + dContents.offsetHeight;

        // Show TOC only after scrolling past hero section
        if (scrollPosition > heroHeight) {
            dContents.classList.add('visible');
        } else {
            dContents.classList.remove('visible');
        }

        if (dContentsBottom >= dArticleBottom) {
            // Make d-contents invisible
            dContents.style.visibility = 'hidden';
        } else {
            // Make d-contents visible
            dContents.style.visibility = 'visible';
        }

        // Adjust the condition to account for margin-top
        if (scrollPosition + marginTop >= originalOffsetTop && scrollPosition > heroHeight) {
            dContents.style.position = 'fixed';
            dContents.style.top = '20px';  // Small offset from top
            dContents.style.left = originalOffsetLeft + 'px'; // Maintain the original horizontal position
            dContents.style.width = originalWidth + 'px'; // Maintain the original width
        } else {
            dContents.style.position = '';
            dContents.style.top = '';
            dContents.style.left = '';
            dContents.style.width = ''; // Allow the width to be automatic
        }
    } else {
        // On mobile/tablet devices, don't apply the fixed positioning
        dContents.style.position = '';
        dContents.style.top = '';
        dContents.style.left = '';
        dContents.style.width = ''; // Allow the width to be automatic
        dContents.classList.remove('visible'); // Hide on smaller screens
    }


});


// Function to determine which section is in view
function getActiveSection() {
    // Query for both section tags and divs with IDs (for sections)
    var sections = document.querySelectorAll('section, div[id="quantitative"], div[id="qualitative"], div[id="latent-analysis"], div[id="imagenet"], div[id="conclusion"]');
    var scrollPosition = window.pageYOffset || document.documentElement.scrollTop;

    for (var i = 0; i < sections.length; i++) {
        if (sections[i].offsetTop <= scrollPosition + 100 && sections[i].offsetTop + sections[i].offsetHeight > scrollPosition + 100) {
            return sections[i].id;
        }
    }
    return null;
}

// Function to update the navigation items
function updateNavigation() {
    var activeSection = getActiveSection();
    var navLinks = document.querySelectorAll('d-contents nav a');

    navLinks.forEach(function(navLink) {
        if (navLink.getAttribute('href') === '#' + activeSection) {
            navLink.classList.add('active-nav-item');
        } else {
            navLink.classList.remove('active-nav-item');
        }
    });
}

// Add the scroll event listener
window.addEventListener('scroll', updateNavigation);

// Initialize width and position
onResize();
// Initial update
updateNavigation();
