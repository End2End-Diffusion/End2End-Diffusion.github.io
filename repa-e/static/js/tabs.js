// Tab switching functionality for REPA-E quickstart section
function switchTab(tabId) {
    // Hide all tab contents
    var contents = document.getElementsByClassName('tab-content');
    for (var i = 0; i < contents.length; i++) {
        contents[i].classList.remove('active');
    }

    // Remove active class from all buttons
    var buttons = document.getElementsByClassName('tab-button');
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove('active');
    }

    // Show selected tab
    document.getElementById(tabId).classList.add('active');

    // Set active button
    event.target.classList.add('active');

    // Re-highlight code syntax
    if (typeof Prism !== 'undefined') {
        Prism.highlightAll();
    }
}
