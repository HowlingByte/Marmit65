document.onreadystatechange = function () {
    if (document.readyState !== "complete") {
        document.querySelector("body").style.visibility = "hidden";
        document.querySelector("#overlay").style.visibility = "visible";
    } else {
        document.querySelector("body").style.visibility = "visible";
        playAnimation();
        revealTitles();
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