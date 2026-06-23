/**
 * Tab switching functionality for Quickstart section
 */

function initTabs() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetTab = button.getAttribute('data-tab');

            // Remove active class from all buttons and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));

            // Add active class to clicked button and corresponding content
            button.classList.add('active');
            const targetContent = document.getElementById(targetTab);
            if (targetContent) {
                targetContent.classList.add('active');
            }
        });
    });

    // Activate first tab by default
    if (tabButtons.length > 0) {
        tabButtons[0].click();
    }
}

/**
 * Add copy buttons to all code blocks
 */
function initCopyButtons() {
    // Find all code blocks in quickstart examples
    const codeBlocks = document.querySelectorAll('.quickstart-example pre');

    codeBlocks.forEach((pre, index) => {
        // Create wrapper if it doesn't exist
        if (!pre.parentElement.classList.contains('code-block-wrapper')) {
            const wrapper = document.createElement('div');
            wrapper.className = 'code-block-wrapper';
            pre.parentNode.insertBefore(wrapper, pre);
            wrapper.appendChild(pre);
        }

        // Create copy button
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-button';
        copyButton.setAttribute('aria-label', 'Copy code to clipboard');
        copyButton.setAttribute('title', 'Copy code');

        // Add click handler
        copyButton.addEventListener('click', async () => {
            const code = pre.querySelector('code').textContent;

            try {
                await navigator.clipboard.writeText(code);

                // Visual feedback - just change icon via CSS class
                copyButton.classList.add('copied');
                copyButton.setAttribute('title', 'Copied!');

                // Reset after 2 seconds
                setTimeout(() => {
                    copyButton.classList.remove('copied');
                    copyButton.setAttribute('title', 'Copy code');
                }, 2000);
            } catch (err) {
                console.error('Failed to copy code:', err);
                // Keep the icon but update tooltip on error
                copyButton.setAttribute('title', 'Failed to copy');
                setTimeout(() => {
                    copyButton.setAttribute('title', 'Copy code');
                }, 2000);
            }
        });

        // Add button to wrapper
        pre.parentElement.appendChild(copyButton);
    });
}

// Initialize everything when DOM is loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        initTabs();
        initCopyButtons();
    });
} else {
    initTabs();
    initCopyButtons();
}
