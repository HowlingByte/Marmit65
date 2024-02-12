document.onreadystatechange = function () {
    revealTitles();
    setupHoverTransitions();
};

function revealTitles() {
    ScrollReveal().reveal('.grid-item-container', {
        delay: 0,
        duration: 800,
        distance: '20px',
        origin: 'bottom',
        easing: 'ease-out',
        interval: 100,
    });
}

function setupHoverTransitions() {
    var gridItemContainers = document.querySelectorAll('.grid-item-container');

    gridItemContainers.forEach(function (container) {
        container.addEventListener('mouseover', function () {
            this.style.transitionDuration = '0.2s';
            this.style.transform = 'scale(1.02)';
        });

        container.addEventListener('mouseout', function () {
            this.style.transitionDuration = '0.2s';
            this.style.transform = 'scale(1)';
        });
    });
}