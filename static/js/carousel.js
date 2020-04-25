$(document).ready(function () {
    $('.carousel.carousel-slider').carousel({ fullWidth: true, indicators: true });

    let carouselAutoplay = setInterval(function () {
        $('.carousel.carousel-slider').carousel("next");
    }, 4000);

});