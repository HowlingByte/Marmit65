document.onreadystatechange = function () {
    if (document.readyState !== "complete") {
        document.querySelector("body").style.visibility = "hidden";
        document.querySelector("#overlay").style.visibility = "visible";
    } else {
        document.querySelector("body").style.visibility = "visible";
        playAnimation();
        revealTitles();
        setupHoverTransitions();
    }
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

function playAnimation() {
    document.querySelector("#overlay").classList.add("slide-out-overlay");
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

document.addEventListener("DOMContentLoaded", function () {
    var links = document.querySelectorAll("a");

    links.forEach(function (link) {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            var overlay = document.querySelector("#overlay");
            overlay.classList.add("slide-in-overlay");

            overlay.addEventListener("animationend", function () {
                window.location.href = link.href;
            });
        });
    });
});
