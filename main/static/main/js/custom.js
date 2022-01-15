if (window.location.hash == '#cart') {
    $('.cart-btn').click()
}
$('.icofont-logout').on('click', function () {
    $('form.logout-form').submit();
});